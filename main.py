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
    # Your solution here!
    # pass

    # even num: every time change
    # odd num: last item self.next is None

    # new_head = head

    # set current with head


    # while current exists:
        # if current and current.next both exists
            # switch start with current.next (current, current.next = current, current.next)

            # first_node = current
            # second_node = current.next

            # if second_node = head:
                # new_head = current.next

            # first_node.next = second_node.next
            # second_node.next = first_node


            # move the pointer by two nodes

            # current = current.next.next

    # return new_head

    # print('####### print linked list')

    # current = head

    # while current:
    #     print(current.value)
    #     current = current.next

    # new_head = head

    current = head
    first_switch = True
    prev = None

    while current and current.next:
        first_node = current
        second_node = current.next

        first_node.next = second_node.next
        second_node.next = first_node

        if prev:
            prev.next = second_node

        # print(f'first_node is now value: {second_node.value}, and now point to node with value: {first_node.value}')


        if first_switch:
            head = second_node
            first_switch = False
            # print(f'head is now value: {head.value},  and now point to node with value: {head.next.value}')

        # current = current.next.next
        # if first_node.next:
            # print(f'current is moved to value: {first_node.next.value}')

        current = first_node.next
        prev = first_node

        # print('####### print linked list')
        # current_temp = head
        # while current_temp:
        #     print(current_temp.value)
        #     current_temp= current_temp.next

    return head


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
