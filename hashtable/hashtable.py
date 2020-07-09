class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
class HashTable:
    def __init__(self, capacity = MIN_CAPACITY):
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
        self.capacity = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        return len(self.capacity)

    def get_load_factor(self):
        return self.size/ len(self.capacity)

    def fnv1(self, key):
        #Constants
        FNV_prime = 0x00000100000001B3
        offset_basis = 0xcbf29ce484222325
        hash = offset_basis
        for char in key:
            hash ^= ord(char) #(the ^ is the XOR)
            hash *= FNV_prime
            # Flip lines the 2 lines above for fnv1_64 implementation
            hash &= 0xffffffffffffffff
        return hash

    def hash_index(self, key):
        return self.fnv1(key) % len(self.capacity)

    def get(self, key):
        i = self.hash_index(key)

        if self.capacity[i] is None:
            return None
        else:
            for keyval in self.capacity[i]:
                if keyval[0] == key:
                    return keyval[1]
                    
            return None


    def put(self, key, value):
        i = self.hash_index(key)

        if self.capacity[i] is not None:
            for keyval in self.capacity[i]:
                if keyval[0] == key:
                    keyval[1] = value
                    if self.get_load_factor() > 0.7:
                        self.resize(len(self.capacity) * 2)
                    break
            else:
                self.capacity[i].append([key, value])
                self.size += 1
                if self.get_load_factor() > 0.7:
                    self.resize(len(self.capacity) * 2)
        
        else:
            self.capacity[i] = []
            self.capacity[i].append([key, value])
            self.size += 1
            if self.get_load_factor() > 0.7:
                        self.resize(len(self.capacity)*2)


    def delete(self, key):
        i = self.hash_index(key)
        
        if self.capacity[i] is not None:
            for keyval in self.capacity[i]:
                if keyval[0] == key:
                    keyval[1] = None
                    self.size -= 1
                    if self.get_load_factor() < 0.2:
                        if len(self.capacity) // 2 > 8:
                            self.resize(len(self.capacity)//2)
        else:
            print("Warning: No key found")
        
    def resize(self, new_capacity):
        ht2 = HashTable(capacity=new_capacity)
        
        for i in range(len(self.capacity)):
            if self.capacity[i]:
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
    print(ht.get_load_factor())
    # ht.resize(len(ht.capacity) * 2)
    new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
    # print(ht.get_load_factor())
    print("")