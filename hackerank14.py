class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None  # Initialize maximumDifference
    # Add your code here
    
    def computeDifference(self):
        min_num = min(self.__elements)
        max_num = max(self.__elements)
        self.maximumDifference = abs(max_num - min_num)
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)