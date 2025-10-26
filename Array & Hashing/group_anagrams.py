from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            ordered_word=''.join(sorted(word))
            if ordered_word in hashmap:
                hashmap.append(word)
            else:
                hashmap[ordered_word]=[word]
        return list(hashmap.values())
        
        