'use strict';

const $ = id => document.getElementById(id);
const escapeHTML = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const plain = value => String(value ?? '').replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/\*\*|`/g, '');
const text = value => escapeHTML(plain(value === 'unknown' || !value ? 'Not recorded' : value));
const labels = {active:'Active',waiting:'Blocked',submitted:'Awaiting review',in_review:'In review',accepted:'Accepted',not_started:'Not started',stopped:'Stopped',unclassified:'Unclassified',closed:'Closed',open:'Open'};
const queueLabels = {
  blocked:['blocked','Blocked'], needs_you:['needs_you','Needs you'], ready:['ready','Ready'],
  in_review:['in_review','In review'], waiting:['waiting','Awaiting review'], done:['accepted','Done'], closed:['closed','Closed']
};
const queuePill = state => { const [color,label] = queueLabels[state] || ['unclassified','Unclassified']; return pill(color,label); };
const ownerOf = value => { const word = plain(value).trim().split(/[\s,.;:]+/)[0] || ''; return /^[a-z][a-z'’-]*$/i.test(word) ? word : ''; };
const pill = (value, label) => `<span class="pill ${escapeHTML(value)}">${escapeHTML(label || labels[value] || value)}</span>`;
const keyAttr = record => `data-record="${escapeHTML(record.path)}"`;
let data = null, view = 'work', loading = false, selected = null, lastSuccess = null, sourceRequest = 0;

function dateLabel(value, includeTime = false) {
  if (!value) return 'Not recorded';
  const date = new Date(typeof value === 'number' ? value * (value < 1e12 ? 1000 : 1) : /^\d{4}-\d{2}-\d{2}$/.test(value) ? `${value}T12:00:00` : value);
  if (Number.isNaN(date.getTime())) return String(value);
  return date.toLocaleString(undefined, includeTime ? {month:'short',day:'numeric',hour:'numeric',minute:'2-digit'} : {month:'short',day:'numeric',year:'numeric'});
}

function records() { return data?.records.records || []; }
function recordByPath(path) { return records().find(r => r.path === path); }
function switchView(next) {
  view = next;
  document.querySelectorAll('[data-view]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.view === view)));
  for (const name of ['work','tasks','connections']) $(`${name}View`).hidden = name !== view;
  if (view === 'connections') renderGraph();
}

function renderMetrics() {
  const open = records().filter(r => r.record_status === 'open');
  const due = open.filter(r => r.check_status === 'due');
  const you = open.filter(r => r.waiting_on_you);
  const blocked = open.filter(r => r.blocked);
  const review = open.filter(r => r.work_status === 'in_review' || r.queue_state === 'in_review');
  const ready = open.filter(r => r.queue_state === 'ready');
  const metrics = [
    ['open','Open work',open.length,`${ready.length} ready for an agent · ${open.filter(r=>r.work_status==='active').length} active now`],
    ['you','Waiting on you',you.length,you.length ? 'Your decision or answer unblocks these' : 'Nothing needs your decision'],
    ['blocked','Blocked',blocked.length,blocked.length ? 'A named dependency stops each one' : 'No blocked work'],
    ['due','Checks due',due.length,`On or before ${dateLabel(data.records.as_of)} · ${review.length} in review`]
  ];
  $('metrics').innerHTML = metrics.map(([filter,label,count,note]) => `<button class="metric" data-metric="${filter}"><span class="label">${label}</span><strong class="${(filter==='due'||filter==='you') && count ? 'amber' : ''}">${count}</strong><small>${escapeHTML(note)}</small></button>`).join('');
  $('recordCount').textContent = records().length;
  $('taskCount').textContent = (data.tasks.tasks || []).filter(t => t.kind === 'task').length;
  $('edgeCount').textContent = data.records.edges.length;
}

function actionableNow(r) {
  // Work a reader can act on today: blocked, owed to the principal, agent-ready,
  // a check already due, or a record that needs repair.
  return !!(r.issues.length
    || [r.work_status, r.record_status].includes('unclassified')
    || r.queue_state === 'needs_you'
    || r.queue_state === 'blocked'
    || r.queue_state === 'ready'
    || (r.record_status === 'open' && r.check_status === 'due'));
}

function filteredRecords() {
  const search = $('search').value.trim().toLowerCase();
  return records().filter(r => {
    const needsAttention = r.issues.length || [r.work_status,r.record_status].includes('unclassified');
    const recordMatch = $('recordFilter').value === 'all' || r.record_status === $('recordFilter').value;
    const stateMatch = !$('statusFilter').value || r.work_status === $('statusFilter').value;
    const queueValue = $('queueFilter').value;
    const queueMatch = !queueValue || (queueValue === 'actionable' ? actionableNow(r) : r.queue_state === queueValue);
    const dueMatch = !$('dueFilter').value || (r.record_status === 'open' && r.check_status === $('dueFilter').value);
    const searchMatch = !search || plain([r.title,r.path,r.work_owner,r.next,r.dependency,r.work_scope,r.work].join(' ')).toLowerCase().includes(search);
    return searchMatch && (needsAttention || (recordMatch && stateMatch && queueMatch && dueMatch));
  }).sort((a,b) => {
    const rank = r => r.issues.length ? 0 : r.queue_state === 'blocked' ? 1 : r.queue_state === 'needs_you' ? 2 : r.queue_state === 'ready' ? 3 : r.queue_state === 'in_review' ? 4 : r.queue_state === 'waiting' ? 5 : r.record_status === 'closed' ? 7 : 6;
    const position = r => (r.queue_state === 'waiting' || r.queue_state === 'ready') ? String(r.next_check_date || '9999') : '';
    return rank(a) - rank(b) || position(a).localeCompare(position(b)) || String(a.next_check_date || '9999').localeCompare(String(b.next_check_date || '9999')) || a.title.localeCompare(b.title);
  });
}

function renderRecords() {
  const visible = filteredRecords();
  $('resultsCount').textContent = `${visible.length} of ${records().length} records · ${$('queueFilter').value === 'actionable' ? 'actionable now, needs you and blocked first' : 'filtered view'}`;
  $('recordList').innerHTML = visible.length ? visible.map(r => `<article class="record${r.blocked ? ' attentionBlocked' : r.waiting_on_you ? ' attentionYou' : ''}">
    <div><p class="area">${text(r.area)}</p><button class="recordTitle" ${keyAttr(r)}>${text(r.title)}</button><div class="badges">${queuePill(r.queue_state)}${pill(r.work_status)}${r.issues.length ? pill('issue',`${r.issues.length} source issue${r.issues.length===1?'':'s'}`) : ''}</div></div>
    <div class="next">${r.blocked ? `<p class="blockedLine"><strong>Blocked</strong> ${text(r.dependency)}</p>` : ''}${r.waiting_on_you ? '<p class="youLine">Waiting on you</p>' : ''}${r.queue_state==='in_review' ? `<p class="reviewLine">In review · check ${escapeHTML(r.next_check_date ? dateLabel(r.next_check_date) : 'date not recorded')}</p>` : ''}<p class="nextLabel">Next action</p><p class="nextText">${text(r.next)}</p></div>
    <div class="recordMeta"><p><strong class="${r.check_status==='due' && r.record_status==='open'?'dueText':''}">${r.record_status==='closed' ? 'Record closed' : r.next_check_date ? `${r.check_status==='due'?'Check due':'Next check'} ${escapeHTML(dateLabel(r.next_check_date))}` : 'No check date'}</strong></p><p>Record updated ${escapeHTML(dateLabel(r.updated))}</p><button class="textbutton" ${keyAttr(r)}>View record →</button></div>
  </article>`).join('') : '<div class="empty">No records match these filters. Select Reset to see open work.</div>';
}

function taskState(task) {
  const states = {started:['active','Turn started'],started_stale:['waiting','Older start · activity unknown'],completed:['accepted','Turn finished'],aborted:['stopped','Turn interrupted'],unknown:['unclassified','Activity unknown']};
  return states[task.state] || states.unknown;
}

function renderTasks() {
  const source = data.tasks;
  $('taskNotice').textContent = source.notice || 'Reads saved local task metadata. Current execution is not verified.';
  if (!source.available) {
    $('taskList').innerHTML = '<div class="empty">The local task source is unavailable. Work records are still shown in their own view.</div>';
    return;
  }
  const all = source.tasks || [];
  const top = all.filter(t => t.kind === 'task');
  const children = all.filter(t => t.kind === 'worker');
  const shown = [];
  for (const task of top) {
    shown.push(task);
    if ($('showWorkers').checked) shown.push(...children.filter(c => c.parent_id === task.id));
  }
  if ($('showWorkers').checked) shown.push(...children.filter(c => !top.some(t => t.id === c.parent_id)));
  $('taskList').innerHTML = shown.length ? shown.map(task => {
    const [color,label] = taskState(task);
    const parent = all.find(t => t.id === task.parent_id);
    return `<article class="task ${task.kind==='worker'?'worker':''}"><div><a href="${escapeHTML(task.href)}">${text(task.title)} ↗</a><p>${task.kind==='worker' ? `Worker · ${parent ? `parent: ${text(parent.title)}` : 'parent task outside this view'}` : `${text(task.section || 'Local project task')}`}</p></div><div class="taskMeta">${pill(color,label)}<p>${task.state_at ? `Event saved ${escapeHTML(dateLabel(task.state_at,true))}` : `Metadata updated ${escapeHTML(dateLabel(task.updated_at,true))}`}</p></div></article>`;
  }).join('') : '<div class="empty">No tasks were found within the documented source scope.</div>';
}

function connectionRow(edge) {
  const source = recordByPath(edge.source), target = recordByPath(edge.target);
  if (!source || !target) return '';
  return `<div class="connection"><button ${keyAttr(source)}>${text(source.title)}</button><span> ${edge.kind==='dependency'?'depends on':'→'} </span><button ${keyAttr(target)}>${text(target.title)}</button></div>`;
}

function renderGraph() {
  if (!data) return;
  const focus = $('graphFocus').value;
  const edges = data.records.edges.filter(e => !focus || e.source === focus || e.target === focus);
  const connected = new Set(edges.flatMap(e => [e.source,e.target]));
  if (focus) connected.add(focus);
  const nodes = records().filter(r => connected.has(r.path));
  const width=1120, height=Math.max(650,nodes.length * 54), centerX=560, centerY=height/2;
  const positions = new Map(nodes.map((r,i) => {
    const angle = (i / nodes.length) * Math.PI * 2 - Math.PI/2;
    return [r.path,{x:centerX+Math.cos(angle)*420,y:centerY+Math.sin(angle)*(height/2-55)}];
  }));
  const shortenLines = title => {
    const words=plain(title).split(' '); let a='',b='';
    while(words.length && (a+' '+words[0]).trim().length <= 28) a=(a+' '+words.shift()).trim();
    if(!a) a=words.shift().slice(0,27)+'…';
    b=words.join(' '); if(b.length>29) b=b.slice(0,27)+'…';
    return [a,b];
  };
  $('graph').setAttribute('viewBox',`0 0 ${width} ${height}`);
  $('graph').innerHTML = `<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#89aa98"/></marker></defs>` + edges.map(e => {
    const a=positions.get(e.source), b=positions.get(e.target);
    if(!a || !b)return '';
    const dx=b.x-a.x,dy=b.y-a.y, boundary=Math.min(98/Math.max(Math.abs(dx),.001),28/Math.max(Math.abs(dy),.001));
    const x=b.x-dx*boundary,y=b.y-dy*boundary;
    return `<path class="graphEdge" marker-end="url(#arrow)" d="M${a.x},${a.y} Q${centerX},${centerY} ${x},${y}"><title>${escapeHTML(e.kind)}</title></path>`;
  }).join('') + nodes.map(r => {
    const p=positions.get(r.path), [a,b]=shortenLines(r.title);
    return `<g class="graphNode ${r.record_status==='closed'?'closed':''}" tabindex="0" role="button" aria-label="View ${escapeHTML(r.title)}" ${keyAttr(r)} transform="translate(${p.x-98},${p.y-28})"><title>${text(r.title)}</title><rect width="196" height="56" rx="7"/><text x="98" y="${b?24:33}" text-anchor="middle">${escapeHTML(a)}${b?`<tspan x="98" dy="17">${escapeHTML(b)}</tspan>`:''}</text></g>`;
  }).join('');
  $('graph').hidden = !nodes.length;
  $('connectionList').innerHTML = edges.length ? edges.map(connectionRow).join('') : '<div class="empty">No direct links between current records are recorded for this selection.</div>';
  const isolated=records().filter(r => !data.records.edges.some(e => e.source===r.path || e.target===r.path));
  $('isolated').textContent = `${isolated.length} records have no direct links to another current record. They may link to older decisions or supporting files. No relationship is inferred from a shared folder.`;
}

function renderCoverage() {
  const source = data.records, coverage = source.coverage;
  const issues = [...source.issues, ...(data.tasks.issues || []).map(i => typeof i==='string'?{message:i}:i)];
  $('issueCount').textContent = issues.length ? `${issues.length} source issue${issues.length===1?'':'s'}` : 'No source errors';
  $('coverageBody').innerHTML = `<p><strong>Work records.</strong> ${coverage.current_records} current records from ${coverage.markdown_files} Markdown files. Reads ${source.sources.map(p=>`<code>${escapeHTML(p)}</code>`).join(", ")} within this project. Closed records remain available through the Record filter.</p><p><strong>Queue positions.</strong> Derived locally from the recorded status, next actor and blocked input. ${coverage.needs_you_open_records} open records wait on the principal, ${coverage.blocked_open_records} are blocked and ${coverage.in_review_open_records} are in review. ${data.finance_url ? 'Finance records appear on the <a href="/finances/">finance dashboard</a>. ' : ''}A card shows what the work is, its status, its next action and what is stopping it.</p><p><strong>Dates.</strong> Check dates use ${escapeHTML(source.as_of)} as the local calendar date. No date means no usable checkpoint is recorded; it does not mean overdue. ${source.warnings.length} records have checkpoint warnings. Changes appear after the source is saved and this page refreshes.</p><p><strong>Tasks.</strong> ${escapeHTML(data.tasks.notice || 'Source unavailable.')} Source checked ${escapeHTML(dateLabel(data.tasks.observed_at,true))}.</p><p><strong>Connections.</strong> The graph uses direct inline Markdown links between current records, including closed records. Arrows show the direction of the source link. Supporting files, reference-style links and unlinked relationships are outside this graph.</p>${issues.length ? `<p><strong>Source issues</strong></p><ul>${issues.map(i=>`<li>${i.path?`<code>${escapeHTML(i.path)}</code>: `:''}${text(i.message || i)}</li>`).join('')}</ul>`:''}`;
}

function renderMarkdown(body,path) {
  const html=marked.parse(body,{gfm:true});
  const fragment=DOMPurify.sanitize(html,{
    ALLOWED_TAGS:['p','br','hr','h1','h2','h3','h4','h5','h6','ul','ol','li','blockquote','pre','code','em','strong','del','s','a','table','thead','tbody','tr','th','td','input','details','summary'],
    ALLOWED_ATTR:['href','title','start','type','checked','disabled'],
    ALLOW_DATA_ATTR:false,RETURN_DOM_FRAGMENT:true
  });
  const slugs=new Map();
  for(const heading of fragment.querySelectorAll('h1,h2,h3,h4,h5,h6')) {
    const base=heading.textContent.toLowerCase().trim().replace(/[^\p{L}\p{N} _-]/gu,'').replace(/ /g,'-');
    const count=slugs.get(base)||0; slugs.set(base,count+1);
    heading.id=`record-${base}${count?`-${count}`:''}`;
  }
  for(const input of fragment.querySelectorAll('input')) { input.type='checkbox'; input.disabled=true; }
  for(const a of fragment.querySelectorAll('a')) {
    const href=a.getAttribute('href');
    if(!href)continue;
    try {
      if(href.startsWith('#')) {
        a.href=`#record-${decodeURIComponent(href.slice(1))}`;
        a.dataset.anchor=decodeURIComponent(href.slice(1));
      } else if(!/^[a-z][a-z0-9+.-]*:/i.test(href) && !href.startsWith('/') && !href.includes('\\')) {
        const base=new URL(path.split('/').map(encodeURIComponent).join('/'),'https://project.invalid/');
        const target=new URL(href,base);
        const targetPath=decodeURIComponent(target.pathname.slice(1));
        const record=recordByPath(targetPath);
        if(target.origin==='https://project.invalid' && record) {
          a.href=record.source_url;
          a.dataset.record=targetPath;
          a.dataset.fragment=decodeURIComponent(target.hash.slice(1));
        } else { a.removeAttribute('href'); a.title='This supporting file is outside the current record view.'; }
      } else if(!/^https?:|^mailto:/i.test(href)) {
        a.removeAttribute('href');
      } else { a.rel='noreferrer'; }
    } catch { a.removeAttribute('href'); }
  }
  return fragment;
}

async function showDetail(path,open=true,fragment='') {
  const r=recordByPath(path); if(!r)return;
  selected=path;
  const request=++sourceRequest;
  $('detailTitle').textContent=plain(r.title);
  $('detailBody').innerHTML=`<p class="path">${escapeHTML(path)}</p><p id="recordStatus" role="status">Reading the complete record…</p><button id="retryRecord" data-record="${escapeHTML(path)}" hidden>Retry record</button><div id="recordContent" hidden><h3>Front matter</h3><dl id="recordMetadata" class="recordMetadata"></dl><article id="recordMarkdown" class="recordMarkdown"></article><details id="rawRecord"><summary>Markdown source</summary><pre id="sourceText" class="sourceText"></pre><a href="${escapeHTML(r.source_url)}">Open source file in this tab</a></details></div>`;
  if(open && !$('detail').open)$('detail').showModal();
  try {
    const response=await fetch(`${r.source_url}&format=json`,{cache:'no-store',signal:AbortSignal.timeout(12000)});
    if(!response.ok)throw new Error(`The source reader returned ${response.status}. The file may have moved or become unavailable.`);
    const record=await response.json();
    if(request!==sourceRequest || selected!==path || !$('detail').open)return;
    $('recordMetadata').innerHTML=Object.entries(record.metadata).map(([key,value])=>`<dt>${escapeHTML(key)}</dt><dd>${escapeHTML(typeof value==='object' && value!==null ? JSON.stringify(value,null,2) : String(value))}</dd>`).join('') || '<dd>No readable front matter.</dd>';
    $('recordMarkdown').replaceChildren(renderMarkdown(record.body,path));
    $('sourceText').textContent=record.source;
    $('recordContent').hidden=false;
    $('recordStatus').textContent=record.issues.length ? record.issues.join(' ') : 'Complete record · saved Markdown';
    if(fragment)document.getElementById(`record-${fragment}`)?.scrollIntoView();
  } catch(error) {
    if(request!==sourceRequest || selected!==path || !$('detail').open)return;
    $('recordStatus').textContent=`Could not open this record. ${error.name==='TimeoutError'?'The local reader did not respond in time.':error.message} Retry after checking the local file.`;
    $('retryRecord').hidden=false;
  }
}

async function refresh() {
  if(loading)return;
  loading=true; $('refresh').disabled=true;
  try {
    const response=await fetch('/operations/api/overview',{cache:'no-store',signal:AbortSignal.timeout(12000)});
    if(!response.ok)throw new Error(`The local reader returned ${response.status}.`);
    data=await response.json(); lastSuccess=new Date();
    $('projectLabel').textContent=`Project · ${data.records.root}`;
    document.title=`Operations · ${data.project?.name || data.records.root.split(/[\\/]/).filter(Boolean).pop()} · Perspicuity`;
    $('error').hidden=true;
    $('freshness').textContent=`Read at ${lastSuccess.toLocaleTimeString(undefined,{hour:'numeric',minute:'2-digit',second:'2-digit'})}`;
    renderMetrics(); renderRecords(); renderTasks(); renderCoverage();
    const priorFocus=$('graphFocus').value;
    $('graphFocus').innerHTML='<option value="">All connected records</option>'+records().map(r=>`<option value="${escapeHTML(r.path)}">${text(r.title)}</option>`).join('');
    if(recordByPath(priorFocus))$('graphFocus').value=priorFocus;
    if(view==='connections')renderGraph();
  } catch(error) {
    $('error').hidden=false;
    $('error').textContent=`Refresh failed. ${data?'The last successful view remains below. ':''}${error.name==='TimeoutError'?'The local reader did not respond in time.':error.message} Check that the local service is running.`;
    $('freshness').textContent=lastSuccess ? `Stale · last read ${lastSuccess.toLocaleTimeString()}` : 'Local source unavailable';
  } finally { loading=false; $('refresh').disabled=false; }
}

document.addEventListener('click',event=>{
  const anchor=event.target.closest('[data-anchor]'); if(anchor){event.preventDefault();document.getElementById(`record-${anchor.dataset.anchor}`)?.scrollIntoView();return;}
  const record=event.target.closest('[data-record]'); if(record){event.preventDefault();showDetail(record.dataset.record,true,record.dataset.fragment||'');}
  const tab=event.target.closest('[data-view]'); if(tab)switchView(tab.dataset.view);
  const metric=event.target.closest('[data-metric]'); if(metric){
    resetFilters(); $('recordFilter').value='open';
    if(metric.dataset.metric==='due')$('dueFilter').value='due';
    else if(metric.dataset.metric==='you')$('queueFilter').value='needs_you';
    else if(metric.dataset.metric==='blocked')$('queueFilter').value='blocked';
    switchView('work'); renderRecords();
  }
});
document.addEventListener('keydown',event=>{const node=event.target.closest('.graphNode');if(node && ['Enter',' '].includes(event.key)){event.preventDefault();showDetail(node.dataset.record);}});
function resetFilters(){ $('search').value='';$('recordFilter').value='open';$('statusFilter').value='';$('dueFilter').value='';$('queueFilter').value='actionable'; }
for(const id of ['search','recordFilter','statusFilter','dueFilter','queueFilter'])$(id).addEventListener('input',()=>data && renderRecords());
$('clearFilters').addEventListener('click',()=>{resetFilters();if(data)renderRecords();});
$('refresh').addEventListener('click',refresh);
$('showWorkers').addEventListener('change',()=>data && renderTasks());
$('graphFocus').addEventListener('change',renderGraph);
$('closeDetail').addEventListener('click',()=>$('detail').close());
$('detail').addEventListener('close',()=>{sourceRequest++;});
$('coverageJump').addEventListener('click',()=>{$('coverage').open=true;$('coverage').scrollIntoView({behavior:'smooth'});});
document.addEventListener('visibilitychange',()=>{if(!document.hidden && $('auto').checked && !$('detail').open)refresh();});
setInterval(()=>{if($('auto').checked && !document.hidden && !$('detail').open)refresh();},15000);
refresh();
