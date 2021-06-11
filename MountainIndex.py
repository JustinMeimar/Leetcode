
class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        left, right = 0, len(arr)-1

        while True:
            
            mid = (left+right)//2
            if mid == len(arr) -1:
                #edge case
                return len(arr)-1

            if arr[mid-1] < arr[mid] > arr[mid+1]:
                #found peak
                return mid
            
            elif arr[mid] > arr[mid+1]:
                right -=1 

            elif arr[mid] < arr[mid+1]:
                left += 1


    
k = Solution()
print(k.peakIndexInMountainArray([1,2,3,7,6,4,3,1]))