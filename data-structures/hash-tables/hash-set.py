'''
    Important:
    1. You cannot access sets by index. You need to iterate using a loop.
    2. To create a new set you need to typecast a dict to a set like this - set({})
    3. Use discard instead of remove to not have an object not found error.
'''

class MyHashSet(object):
    hash_set = None
    def __init__(self):
        self.hash_set = set({})

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash_set.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash_set.discard(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.hash_set:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)