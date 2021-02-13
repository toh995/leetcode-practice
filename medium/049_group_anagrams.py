class Solution:
    # group by sorted string
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = [word]
            else:
                groups[sorted_word].append(word)

        return list(groups.values())


    # group by character count
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            # form the key
            key = [0]*26
            for char in word:
                key[ord(char) -97] += 1
            key = tuple(key)

            # check if key exists in groups
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)

        return list(groups.values())
