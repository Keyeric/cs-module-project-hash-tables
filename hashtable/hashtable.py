class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # if capacity < MIN_CAPACITY:
        #     capacity = MIN_CAPACITY
        self.capacity = [None] * capacity
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        """
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        items = 0
        for item in self.capacity:
            if item is not None:
                items += 1
        return items/ len(self.capacity)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        """

        #Constants
        FNV_prime = 0x00000100000001B3
        offset_basis = 0xcbf29ce484222325
        hash = offset_basis
        for char in key:
            hash ^= ord(char)
            hash *= FNV_prime
            # Flip lines the 2 lines above for fnv1_64 implementation
            hash &= 0xffffffffffffffff
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % len(self.capacity)
        # return self.djb2(key) % self.capacity

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        i = self.hash_index(key)

        if self.capacity[i] is None:
            return None
        else:
            for keyval in self.capacity[i]:
                if keyval[0] == key:
                    return keyval[1]
                    
            return None

    def get_size(self):
        return self.size

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        i = self.hash_index(key)

        if self.capacity[i] is not None:
            for keyval in self.capacity[i]:
                if keyval[0] == key:
                    keyval[1] = value
                    break
            else:
                self.capacity[i].append([key, value])
                self.size += 1
        
        else:
            self.capacity[i] = []
            self.capacity[i].append([key, value])
            self.size += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        i = self.hash_index(key)
        
        if self.capacity[i] is not None:
            for keyval in self.capacity[i]:
                if keyval[0] == key:
                    keyval[1] = None
                    self.size -= 1
        else:
            print("Warning: No key found")
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        
        ht2 = HashTable(capacity=new_capacity)
        
        for i in range(len(self.capacity)):
            for keyval in self.capacity[i]:
                ht2.put(keyval[0], keyval[1])
        self.capacity = ht2.capacity

        
        # prev_capacity = self.capacity
        # self.capacity = [None] * new_capacity
        # for i in range(new_capacity):
        #     print(f"i in range: {i}")
        #     if self.capacity[i] is None:
        #         continue
        #     for keyval in self.capacity[i]:
        #         self.put(keyval[0], keyval[1])


if __name__ == "__main__":
    ht = HashTable(8)
    

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    print(ht.get_size())
    print(ht.get_load_factor())
    ht.resize(len(ht.capacity) * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    print(ht.get_size())
    print(ht.get_load_factor())
    print("")