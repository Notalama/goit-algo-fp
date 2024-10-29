class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def insertion_sort(head):
    if head is None or head.next is None:
        return head

    sorted_list = None
    current = head
    while current:
        next_node = current.next
        sorted_list = sorted_insert(sorted_list, current)
        current = next_node
    return sorted_list

def sorted_insert(head, new_node):
    if head is None or head.data >= new_node.data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

def merge_sorted_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        merged_list = head1
        merged_list.next = merge_sorted_lists(head1.next, head2)
    else:
        merged_list = head2
        merged_list.next = merge_sorted_lists(head1, head2.next)
    return merged_list

def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()
    
list1 = Node(5)
list1.next = Node(3)
list1.next.next = Node(1)

list2 = Node(4)
list2.next = Node(2)

# Реверсування списку
list1 = reverse_list(list1)
print("Реверсований список:", end=" ")
print_list(list1)

# Сортування списку
list1 = insertion_sort(list1)
print("Відсортований список:", end=" ")
print_list(list1)

# Об'єднання списків
merged_list = merge_sorted_lists(list1, list2)
print("Об'єднаний список:", end=" ")
print_list(merged_list)


