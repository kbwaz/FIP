class CacheManager:
    def __init__(self):
        # Initialize the cache as an empty dictionary
        self.cache = {}

    def store(self, key, value):
        """
        Store a value in the cache with the specified key.
        
        :param key: The key under which the value should be stored.
        :param value: The value to be stored in the cache.
        """
        self.cache[key] = value

    def retrieve(self, key):
        """
        Retrieve a value from the cache by its key.
        
        :param key: The key of the value to retrieve.
        :return: The cached value if found, otherwise None.
        """
        return self.cache.get(key)

    def invalidate(self, key):
        """
        Invalidate a cache entry by its key.
        
        :param key: The key of the cache entry to invalidate.
        """
        if key in self.cache:
            del self.cache[key]

    def clear_cache(self):
        """
        Clear all entries in the cache.
        """
        self.cache.clear()

