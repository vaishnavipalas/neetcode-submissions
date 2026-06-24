class TimeMap:

    def __init__(self):

        self.time_map = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append([value, timestamp])
        else:
            self.time_map[key] = [[value, timestamp]]
        print(self.time_map)
        

    def get(self, key: str, timestamp: int) -> str:
        print(key, timestamp)

        if key not in self.time_map:
            return ''

        curr_list = self.time_map[key]

        if not curr_list:
            return ''

        lo = 0
        hi = len(curr_list) -1


        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if curr_list[mid][1] == timestamp:
                return curr_list[mid][0]

            elif curr_list[mid][1] < timestamp:
                lo = mid + 1
            else:
                hi = mid - 1
            
        return curr_list[hi][0] if hi >= 0 else '' 
