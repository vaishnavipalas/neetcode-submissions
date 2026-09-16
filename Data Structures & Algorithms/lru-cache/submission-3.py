class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # keep track of the size capacity of the cache
        self.max_capacity = capacity

        # access the keys with a hashmap for O(1) lookup
        self.cache = {}
        # reference size of cache by doign len(cache)
        # keep track of usage with linked list
        self.lru = ListNode(0, 0)
        self.mru = ListNode(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        prev = self.mru.prev
        prev.next = node
        node.prev = prev
        node.next = self.mru
        self.mru.prev = node

        

    def get(self, key: int) -> int:
        # if the passed in key exists, return the corresponding value
        # else, return -1
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1


        # need to not only return the value, but also update it as the latest used
        

    def put(self, key: int, value: int) -> None:
        new_node = ListNode(key, value)
        
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(new_node)
            self.cache[key] = new_node

        else:
            self.cache[key] = new_node
            self._insert(new_node)

            if len(self.cache) > self.max_capacity:
                least_used = self.lru.next
                self._remove(least_used)
                del self.cache[least_used.key]


        
        # if the key exists, update the value of the key + update as latest used
        # else
        # add key value pair to the cache
            # if after adding size > capacity:
                # remove the least recently used key
                # "used" means a get or a put operation was used
        
