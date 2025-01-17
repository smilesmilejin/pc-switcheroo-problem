# DO NOT MODIFY THE NODE CLASS
class Node:

    def __init__(self, value, next=None):
        self.value = value
        # if next is None, this is the last element in the list
        self.next = next

    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and self.value == other.value
                    and self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")


def shuffle(head):
    # If list is empty or has one element there is no need to shuffle
    if head is None or head.next is None:
        return head

    # Set up variables to keep track of the new and old positions
    old_head = head
    # The second element becomes the new head
    new_head = old_head.next
    # The old head will be the second element in the new list
    new_second = old_head

    # Recursively shuffle the remaining elements (starting with the third)
    new_second.next = shuffle(old_head.next.next)
    new_head.next = new_second

    return new_head


# Input: a->b->c->d->e->f
# Output: b->a->d->c->f->e
list_1 = Node('a', Node('b', Node('c', Node('d', Node('e', Node('f'))))))
expected = Node('b', Node('a', Node('d', Node('c', Node('f', Node('e'))))))
assert shuffle(list_1) == expected

# Input: a->b->c->d->e
# Output: b->a->d->c->e
list_2 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('b', Node('a', Node('d', Node('c', Node('e')))))
assert shuffle(list_2) == expected

# Input: 7->2
# Output: 2->7
list_3 = Node(7, Node(2))
expected = Node(2, Node(7))
assert shuffle(list_3) == expected

# Input: a
# Output: a
list_4 = Node('a')
expected = Node('a')
assert shuffle(list_4) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
