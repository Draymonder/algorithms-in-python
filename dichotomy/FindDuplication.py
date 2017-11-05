def FindDuplication(nums):
        res = set()
        ret = []
        for num in nums:
            if num in res:
                ret.append(num)
            res.add(num)
        return ret 


a = FindDuplication([1, 1, 2, 3, 4, 4, 5, 6, 5])
print(a)
