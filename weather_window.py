"""
HW04 — Weather Window: Sliding Maximum

Implement sliding_window_max(nums, k) -> list
"""

import heapq

def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []
    if k > len(nums):
        return [max(nums)]

    # Python’s heapq is a min-heap, so we store (-value, index)
    heap = []
    result = []

    for i, num in enumerate(nums):
        # Push current element
        heapq.heappush(heap, (-num, i))

        # Remove elements that are outside the current window
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)

        # Once the first window is formed, start recording results
        if i >= k - 1:
            result.append(-heap[0][0])

    return result


# Example manual runs
if __name__ == "__main__":
    print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
    print(sliding_window_max([9, 11], 2))                     # [11]
    print(sliding_window_max([4, 2, 12, 3, 8, 7, 9], 2))      # [4, 12, 12, 8, 8, 9]
    print(sliding_window_max([], 3))                          # []
    print(sliding_window_max([2, 1], 5))                      # [2]
