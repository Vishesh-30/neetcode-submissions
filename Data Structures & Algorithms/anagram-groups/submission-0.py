class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i, _ in enumerate(strs):
            sortedS = ''.join(sorted(_))
            # print(sortedS)
            hmap[sortedS].append(_)
        return list(hmap.values())
