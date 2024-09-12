from typing import List

class Solution:
    def  twoSum(self, nums: List[int], target: int) -> List[int]:
        values_indexes={}

        for i, n in enumerate(nums):
            remainder=target-n
            if(remainder in values_indexes):
                return(i,values_indexes[remainder])
            else:
                values_indexes[n]=i

def main():
    s=Solution()
    print(s.twoSum([2,7,11,15], 9) )
    print( s.twoSum( [3,2,4], 6 ) )
    print( s.twoSum( [3,3], 6 ) )

if __name__ == "__main__":
    main()

