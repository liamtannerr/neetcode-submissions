class TimeMap:

    def __init__(self):

        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        keyList = self.keys.get(key, [])
        res = ""

        l = 0
        r = len(keyList) - 1

        while l <= r:
            m = (l + r) // 2
            if keyList[m][1] <= timestamp:
                res = keyList[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
        
