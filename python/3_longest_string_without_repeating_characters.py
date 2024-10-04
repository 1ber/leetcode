from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        start,end=0,0

        current_string=""
        for nr,c in enumerate(s):
            p=s.find(c)
            if(p>-1 and p<nr):
                start=p+1
            end=end+1
                
        return(s[start:end+1])

def main():
    s=Solution()
    print(s.lengthOfLongestSubstring("dvdf"))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    main()
