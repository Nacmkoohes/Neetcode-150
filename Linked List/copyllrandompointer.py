class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        #hashmap to hold old nodes and their corresponding new nodes
        old_to_new = {}

       # Create new nodes and map them
        while current:
            node = Node(x=current.val)
            old_to_new[current] = node
            current = current.next

        
        current = head
        # Set next and random pointers for new nodes
        while current:
            new_node = old_to_new[current]
            new_node.next = old_to_new[current.next] if current.next else None
            new_node.random = old_to_new[current.random] if current.random else None
            current = current.next

        return old_to_new[head]
