from typing import List

class Solution:
     def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        b=prices[0]
        
        for p in prices[1:]:
            if(p<b):
                b=p
            
            profit=p-b
            if(profit>max_profit):
                max_profit=profit
        
        return(max_profit)

def main():
    s=Solution()
    
    print(s.maxProfit( [7,1,5,3,6,4] ) )
    print(s.maxProfit( [7,6,4,3,1] ) )
    print(s.maxProfit( [3,3,5,0,0,3,1,4] ) )
    print(s.maxProfit( [2,6,1,3,2,4] ) )

if __name__ == "__main__":
    main()

