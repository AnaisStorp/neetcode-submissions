class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        counts = Counter(nums)
        heap = []
        for val, freq in counts.items():
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappop(heap)      # evict the weakest of the k survivors
        return [val for _, val in heap]      