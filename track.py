
class Track:
    def __init__(self, length):
        self.length = length
        self.lane1 = []
        self.lane2 = []
        self.range = range(0, length)
        for _ in self.range:
            self.lane1.append("_")
            self.lane2.append("_")
        self.lane1.append("|")
        self.lane2.append("|")
