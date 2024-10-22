class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, value):
       
        new_node = Node(key, value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self, key):
        
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove(self, key):
        
        node = self.find(key)
        if node is None:
            return False
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        return True

    def items(self):
        
        current = self.head
        while current:
            yield current.key, current.value
            current = current.next

class HashTable:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor = 0.75
        self.shrink_factor = 0.25
        self.table = [DoublyLinkedList() for _ in range(self.capacity)]

    def _hash_function(self, key):
        
        A = 0.618033  # Golden ratio fraction approximation
        fractional_part = (key * A) % 1
        return int(self.capacity * fractional_part)

    def insert(self, key, value):
        
        index = self._hash_function(key)
        bucket = self.table[index]
        node = bucket.find(key)

        if node:
            node.value = value  # Update if key exists
        else:
            bucket.insert(key, value)  # Insert new node
            self.size += 1

        if self.size / self.capacity > self.load_factor:
            self._resize(self.capacity * 2)

    def get(self, key):
       
        index = self._hash_function(key)
        node = self.table[index].find(key)
        if node:
            return node.value
        else:
            raise KeyError(f"Key {key} not found!")

    def remove(self, key):
        
        index = self._hash_function(key)
        removed = self.table[index].remove(key)

        if removed:
            self.size -= 1
            if self.capacity > 8 and self.size / self.capacity < self.shrink_factor:
                self._resize(self.capacity // 2)
        else:
            raise KeyError(f"Key {key} not found!")

    def _resize(self, new_capacity):
        
        old_table = self.table
        self.capacity = new_capacity
        self.table = [DoublyLinkedList() for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for key, value in bucket.items():
                self.insert(key, value)  

    def print_table(self):
        
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: ", end="")
            for key, value in bucket.items():
                print(f"[{key}: {value}] ", end="")
            print()

def dynamic_insert():
    hash_table = HashTable()
    while True:
        print("\nHash Table Operations:")
        print("1. Insert")
        print("2. Get")
        print("3. Remove")
        print("4. Print Hash Table")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter key to insert: "))
            value = int(input("Enter value to insert: "))
            hash_table.insert(key, value)
            print(f"Inserted ({key}, {value})")

        elif choice == '2':
            key = int(input("Enter key to get value: "))
            try:
                value = hash_table.get(key)
                print(f"Value for key {key} is {value}")
            except KeyError as e:
                print(e)

        elif choice == '3':
            key = int(input("Enter key to remove: "))
            try:
                hash_table.remove(key)
                print(f"Removed key {key}")
            except KeyError as e:
                print(e)

        elif choice == '4':
            print("Hash Table:")
            hash_table.print_table()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    dynamic_insert()
