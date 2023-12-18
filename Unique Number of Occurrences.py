import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}

        for num in arr:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        # get the values of the hash_map
        hash_map_values = hash_map.values()

        # check the set of the hash_map_values
        # if the set version equals to hash_map_values itself
        # return True, otherwise return False
        if collections.Counter(hash_map_values) == collections.Counter(list(set(hash_map_values))):
            return True
        else:
            return False