from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#https://leetcode.com/problems/reverse-linked-list/
def create_list( values:List[int]) -> ListNode:
    if(len(values)==0):
        return(None)

    head=ListNode(values[0])
    current_node=head
    for v in values[1:]:
        current_node.next=ListNode(v)
        current_node=current_node.next
    return(head)

def print_list(n: ListNode)->None:
    while(n is not None):
        print(n.val)
        n=n.next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt=None
        while(head is not None):
            temp=head.next
            head.next=nxt
            nxt=head
            head=temp
            
        return(nxt)

def main():
    s=Solution()
    print_list(s.reverseList( create_list( [1,2,3,4,5] ) ) )
    print_list(s.reverseList( create_list( [1,2] ) ) )
    print_list(s.reverseList( create_list( [] ) ) )


if __name__ == "__main__":
    main()

