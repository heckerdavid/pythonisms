class Node:
    '''
    linked list node
    '''
    def __init__(self, value=None, next_=None) -> None:
        self.value = value
        self.next = next_



class LinkedList:
    """
    Singly linked list
    """

    def __init__(self, values=None) -> None:
        self.head = None
        self.length = 0

        if values:
            for value in reversed(values):
                self.insert(value)

    def __str__(self) -> str:
        """{ a } -> { b } -> { c } -> None"""
        string = ''
        current = self.head

        while current:
            string += '{ ' + str(current.value) + ' } -> '
            current = current.next


        return string + 'None'

    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return generator()

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError

        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        return current.value
    
    def __setitem__(self, index, value):
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        current.value = value


    def __eq__(self, __o: object) -> bool:
        return list(self) == list(__o)

    def insert(self, value: any) -> None:
        """Inserts given value to linked list head O(1)"""
        self.head = Node(value, self.head)
        self.length += 1


    def insert_before(self, pivot, value) -> None:
        self.length += 1
        current = self.head
        previous = self.head

        if self.head.value == pivot:
            self.head = Node(value, self.head)
            return None

        while current:
            if current.value == pivot:
                previous.next = Node(value, current)
                return None
            previous = current
            current = current.next
        raise Exception(f'{pivot} not in list.')


    def insert_after(self, pivot, value):
        self.length += 1
        current = self.head
        previous = self.head

        while current:
            if current.value == pivot:
                current.next = Node(value, current.next)
                return None
            previous = current
            current = current.next

    def kth_from_the_end(self, k):
        finder = self.head
        follower = self.head
        length = 0

        if finder is None or k < 0:
            return

        while finder.next:
            length += 1
            finder = finder.next

        if k > length:
            return f'{k} is larger than the length of this list'

        for _ in range(length - k):
            follower = follower.next

        return follower.value


    def append(self, value) -> None:
        self.length += 1
        current = self.head
        if current is None:
                self.head = Node(value)
        while current:
            if current.next is None:
                current.next = Node(value)
                break
            current = current.next


    def includes(self, value: any) -> bool:
        """Indicates whether that value exists as a Nodes value somewhere within the list."""
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False


    def delete(self, value) -> str:
        """Removes first instance of given value from list. O(n)"""

        current = self.head
        previous = self.head

        while current:
            if current.value == value:
                previous.next = current.next
                self.length -= 1
                return f'{current.value} deleted from list.'
            previous = current
            current = current.next
        return f'Cannot delete {value}; {value} not found in list.'


    def get_length(self, node, working_length=0) -> int:
        if node is None:
            return working_length
        return self.get_length(node.next, working_length + 1)

