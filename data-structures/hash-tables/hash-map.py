class MyHashMap(object):
    hash_map = None
    def __init__(self):
        self.hash_map = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hash_map[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_map:
            return int(self.hash_map.get(key))
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hash_map:
            self.hash_map.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)