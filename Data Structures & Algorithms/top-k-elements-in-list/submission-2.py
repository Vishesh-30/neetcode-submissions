class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(list)
        nums = sorted(nums)
        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        # print(hmap)
        listt = []
        # Sort the items based on their frequency (value) in descending order
        sorted_items = sorted(hmap.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            listt.append(sorted_items[i][0])


        return listt
