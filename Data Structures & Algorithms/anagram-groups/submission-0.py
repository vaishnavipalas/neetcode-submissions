class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getkey(word):

            key = [0] * 26

            for char in word:
                key[ord(char) - ord('a')] += 1
            
            return str(key)
        
        groups = dict()

        for s in strs:
            key = getkey(s)

            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        result = []
        for key in groups:
            result.append(groups[key])
        
        return result

        