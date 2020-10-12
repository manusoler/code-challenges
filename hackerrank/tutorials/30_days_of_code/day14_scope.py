class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = 0
        for e1 in self.__elements:
            for e2 in self.__elements:
                self.maximumDifference = abs(
                    e1-e2) if abs(e1-e2) > self.maximumDifference else self.maximumDifference

# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
