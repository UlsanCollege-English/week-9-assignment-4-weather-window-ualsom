[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZPg02Otg)
# HW04 — Weather Window: Sliding Maximum

**Story intro (new theme):**  
A **weather station** shows the **highest temperature** in the **last k days** for each day. Compute this sliding maximum fast.

**Technical description**  
- **Input:** list `nums` of integers (temperatures), integer `k`.  
- **Output:** list of integers: maximum for each window of size `k`.  
- **Rules:**  
  - If `k <= 0` or `nums` is empty, return `[]`.  
  - If `k > len(nums)`, return `[max(nums)]`.  
- **Expected complexity:** **Time** `O(n log k)` using a **max-heap** via negatives and **lazy deletion**; **Space** `O(k)`.

---

## Minimal prompts (you drive the 8 Steps)
- State the problem in your own words.  
- Define inputs/outputs clearly.  
- Design with a heap of pairs `(-value, index)`; pop while index is outside the window.  
- Code it, test small cases, and reason about `O(n log k)`.

---

## Hints
- Store `(-nums[i], i)` to simulate a max-heap.  
- When moving the window, pop from heap while `top_index <= i - k`.  
- Append `-heap[0][0]` as the current max.

---

## How to run tests
python -m pytest -q



---

## FAQ
- **Q:** Why not deque? **A:** Today we practice heaps; use a heap solution.  
- **Q:** How to handle `k==1`? **A:** The answer is the original list.  
- **Q:** Duplicates? **A:** Allowed. Use indices to validate freshness.  
- **Q:** Complexity? **A:** `O(n log k)` time, `O(k)` space.  
- **Q:** stdin? **A:** No. Implement a function the tests import.  
- **Q:** Grading? **A:** Tests must pass.  
- **Q:** Reading failures? **A:** Check which window and expected max.
