class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        cnt=Counter(nums)
        for i in (cnt):
            if cnt[i]>1:
                l.append(i)
        return l
