# Loop: <plan title>

This file is the instruction set for a `/loop` run of the plan at `<path to plan>`. It adds no authority: every item runs under a grant the plan names. To leave an item out, delete it before the start.

Start the loop with:

```
/loop Follow <path to this file>. Continue until the loop reaches an exit.
```

## Ships as

The plan's `Ships as` checks are the finish line. Do not copy them here; read them from the plan.

Done check: `<one command that runs every auto check and exits 0 only when all pass>`

## Pre-run gate

Answer every row, or move the check or unit that needs it to a named later plan, before the loop starts.

| Input | Needed by | Owner | Answer, or where the check moved |
| --- | --- | --- | --- |
| <decision, credential, account action or human-only step> | <check, unit or item> | <person> | <answer / later plan> |

## Terms

- **Plan**: <path>. Write each result under "Run log" in the plan or the unit's record. <Staging rule.>
- **Workspace**: <branch or worktree, created from the shared revision>.
- **Test run**: <command>.
- **Deploy**: <the verified deploy rule, if the plan deploys>.
- **Time**: read the clock before you write a time.

## Rules for every iteration

1. Read the project's agent instructions, this file and the plan.
2. Find the first eligible item. Read each unit's state from its own record.
3. Do the item completely, under its grant. Do not ask the principal between the steps of an item.
4. Have each return reviewed by the receiver its grant names. Close each record its receiver accepted in this iteration, unless a review commitment remains open.
5. Run the done check. Record the result and the time.
6. Put a question for the principal on the escalation list in the plan. Continue with the next item that does not depend on the answer.
7. When the next item waits for a time, schedule the next iteration.

## Exits

End the loop at one of three exits. Write it in the plan's `Current position` as `Exit:` with the time.

- **finished**: the done check passes, each observer check has its observer's words, and every unit is accepted, stopped or transferred. Run the last item. It ends the loop.
- **parked**: every remaining item needs an input that no grant supplies, such as a secret or a human check this file does not cover. Write each input, its owner and the exact command that resumes this loop. Set `plan_status: waiting`. Report the shippable unit as not reached. Do not write a new loop file for the remainder.
- **stopped**: the stop conditions below block every remaining item, or no item remains eligible while the done check fails. Write what occurred and who decides next. Set `plan_status: waiting`; the principal sets `stopped` if they end the plan.

## Stop conditions

Escalate an item that meets one of these, and continue with items that do not depend on it. Stop the loop when these block every remaining item.

- <an item needs a change outside its grant>
- <a deploy changes something the item did not predict, and the revert fails>
- <a tolerance the principal set is reached>

## Items

### 0. Set up

1. Create the workspace. Run the test run and the done check. Record both as the baseline.

### 1. <item>

<Steps, the grant it runs under, the predicted change, and how the result is checked.>

### Last. Close-out

1. Run the done check. It must pass. Collect the words of each observer check.
2. Hold the plan's close-out in `Review`: what was supposed to happen, what happened, why they differ, what changes next time, and the delegation measures.
3. Give every result one destination verdict: shipped, with outside evidence; held, with reason and owner; or abandoned, with reason.
4. Close each unit record that is still open and accepted, unless a review commitment remains open.
5. Set `plan_status: accepted`, or `in_review` while a review commitment remains. Record `Closure` only when none remains. Write `Exit: finished`.
6. End the loop.

## What this loop does not do

- <work excluded by the grants, and ideas that belong in the plan's Later list>
