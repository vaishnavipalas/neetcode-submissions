class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        end = '#'
        currindex = 0
        for s in strs:
            result += s
            currindex += len(s)
            end += str(currindex)
            end += '-'
        
        result += end
        print(result)
        return result


    def decode(self, s: str) -> List[str]:
        hash_i = s.rfind('#')
        beginning = s[:hash_i]
        end = s[hash_i+1:]
        print(beginning)
        print(end)
        indices = end.split("-")
        prev = 0
        result = []
        for word in indices:
            if word:
                curr_end = int(word)
                result.append(beginning[prev:curr_end])
                prev = curr_end
        return result
