# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Just use the aproach of changing the pointers/links instead of the values

# Approach
<!-- Describe your approach to solving the problem. -->
To reverse the order of the pointers:
* The first note (head) must become the tail
* The nth node must become the len-n node
* The Last node must becone the first (head)


# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
Since the list is iterated just one time, the complexity is O(n)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
Just two extra variables are created (one to store the next Node and other to store previous next node)

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt=None
        while(head is not None):
            #Stores the next value since it will be changed
            temp=head.next
            head.next=nxt

            #On the next iteration the actual node will be turned into the 'next'
            nxt=head

            #Since temp has the next node it will iterate through the nodes
            head=temp
            
        return(nxt)

```