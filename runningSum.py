class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i,n in enumerate(nums):  
            if i == 0:
                output.append(n)
            else:
                output.append(output[i-1]+n)
        return output
