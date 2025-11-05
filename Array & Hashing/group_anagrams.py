class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for word in strs:
            #make them like eachother if they are anagrams
            key=''.join(sorted(word))
            if key in hashmap:
                hashmap[key].append(word)
            #if key not already created by first time you see a word you make it a key
            else:
                hashmap[key] = [word]
        return list(hashmap.values())