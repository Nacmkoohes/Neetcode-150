import bisect

class TimeMap:
    def __init__(self):
        self.store = {} #key=string, value=list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
            res= ""
            #values=[] is a list of [value, timestamp] pairs
            values=self.store.get(key, [])

            #binary search
            l=0
            r=len(values)-1
            while l <= r:
                mid = (l + r) // 2
                # Check if the timestamp at mid is less than or equal to the target timestamp
                if values[mid][1] <= timestamp:
                   res = values[mid][0]
                   l=mid + 1
                else:
                    r = mid - 1
            return res 


