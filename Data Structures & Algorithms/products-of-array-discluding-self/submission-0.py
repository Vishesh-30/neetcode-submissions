class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i, _ in enumerate(nums):
            pre = nums[0:i]
            suf = nums[i+1:len(nums)]
            # print(pre,suf)
            p_p = 1
            for i in pre:
                p_p *= i
            s_p = 1
            for i in suf:
                s_p *= i
            res.append(p_p*s_p)
            # print(pre,suf)
        return res