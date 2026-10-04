# Longest Consecutive Sequence: Mentoring Notes

**Problem:** https://neetcode.io/problems/longest-consecutive-sequence/question
**Requirement:** O(n) time
**Status:** Accepted, O(n) proven (submission-7). Code cleanup still pending.

---

## How the submissions evolved

| Submission | Change | Result / issue |
|---|---|---|
| 0 | Hash map + max; from every number, scan forward up to `max_num` | No `break`, so it scans the full range every time. Crashes on empty input |
| 1 | Added empty-input guard | Same complexity problem |
| 2 | Added `break` when the run ends | Better, but still O(n²) on `[1, 2, ..., n]` because every number starts a walk |
| 3 | `count = 1` for single-element input | TLE. Still O(n²) |
| 4/5 | **Walk only if `x - 1` is not in the map** | Accepted, but still O(n²) with duplicates: `[1, 1, ..., 1, 2, ..., k]` |
| 6 | Iterate `dic.keys()` instead of `nums` | Bug: kept `nums[i]` while `i` was now a value, not an index |
| 7 | Fixed to use `num` directly | **Accepted and O(n)** |

---

## Key insights (in the order they were found)

1. **Find repeated work by tracing by hand.** Tracing `[1, 2, 3, 4, 5]` showed that the walk from 2 repeats part of the walk from 1, the walk from 3 repeats part of the walk from 2, and so on: 5 + 4 + 3 + 2 + 1 lookups, which is O(n²).
2. **"Skip if already visited" depends on order.** For `[3, 4, 5, 1, 2]`, 3 is processed before 1, so its walk is still repeated. The rule needs to be **order-independent**.
3. **The rule that works: a number starts a walk only if `x - 1` is absent.** Then x must be the first number of its sequence. Found by filling in an `x` / `is x-1 present?` / `should start?` table.
4. **Iterate over unique values, not the raw input.** Otherwise each duplicate of a start value repeats the same walk.
5. **Built-ins are fine in interviews if you know their cost.** Every mainstream language has an iterable hash set (`set`, `HashSet`, `unordered_set`, `Set`).

### Mistakes worth remembering
- Thought the walk from 5 would be the longest. Walks go **forward** (`x+1`), so 5's walk is the shortest.
- "I dry-ran one example and got exactly n lookups." One example isn't a proof, and the count was wrong (it's 2k, not n).
- First counting attempt said each number can be landed on "at most 2n times". That bound would make it O(n²). The correct bound is **once**.
- Submission-6: after changing the loop from indices to values, `nums[i]` was left in place. When you change what a loop variable means, check every place it's used.

---

## Complexity proof (derived by me)

Let n be the input size, k the number of unique values, and s the number of sequences.

- Building the set: **O(n)**
- Start checks (`x - 1` lookups): once per unique value, so **k**
- Walks: each sequence has exactly one start, so there are **s** walks.
  - Each non-start number is landed on **exactly once**, by the walk from its own sequence's start. A walk from any other start can't reach it because walks stop at the first missing number, and different sequences are separated by a gap. That gives **k − s** successful lookups.
  - Each walk ends with exactly one failed lookup, so **s** failed lookups.
  - Walk lookups total: (k − s) + s = **k**
- **Total:** n + 2k ≤ 3n, which is **O(n) time**. **O(n) space** for the set.

---

## Open tasks

- [ ] **Cleanup** (target ~8–10 lines):
  - `dict` of `True` → which structure is meant for "is it present?"
  - Is `max_num` needed now that the loop `break`s? What loop type fits "keep going while the next number exists"?
  - The `temp_cnt = 1` inside `else`: does it do anything?
  - Update `count` once after each walk, not on every step
  - Can a different starting value for `count` remove the empty-input special case?
- [ ] **Optional second approach:** memoization (store a result for every number a walk touches, then reuse it). Compare it with the start-check approach.

---

## General takeaways

- **If it "feels close to O(n)", look for the worst-case input:** sorted, all duplicates, descending.
- **Nested loops can still be O(n)** when each element is processed a bounded number of times in total (amortized analysis). This comes up again in sliding window, two pointers, and monotonic stack problems.
- **Only start work from a canonical starting point** (here, "no `x - 1`"). Watch for the same pattern elsewhere.
- **Prove complexity with a counting argument**, not a dry run.
