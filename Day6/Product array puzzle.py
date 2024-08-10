class Solution:
    def productExceptSelf(self, nums):
        l=[]
        if nums.count(0)>1:
            return [0]*len(nums)
        if nums.count(0)==1:
            prod=1
            for i in nums:
                if i!=0:
                    prod*=i
            for i in nums:
                if i!=0:
                    l.append(0)
                else:
                    l.append(prod)
            return l
        else:
            prod=1
            for i in nums:
                prod*=i
            for i in nums:
                l.append(prod//i)
            return l
