class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lastIdx = len(nums)-1
        if(target > nums[lastIdx]): #處理邊界值(比這陣列都大或小)
            return lastIdx+1
        elif(target == nums[lastIdx]):
            return lastIdx
        elif(target <= nums[0]):
            return 0            
        return Solution.binSearch(nums,target,0,lastIdx)
    def binSearch(nums,target,head,end):
        mid = int((head+end)/2)
        if(nums[mid] == target):
            return mid
        elif(nums[mid]<target<nums[mid+1]):
            return mid+1
        elif(nums[mid]<target):
            return Solution.binSearch(nums,target,mid,end)
        else:
            return Solution.binSearch(nums,target,head,mid)
