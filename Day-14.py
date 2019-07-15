class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = -10000

	# Add your code here
    def computeDifference(self):

        for i in range(0, len(a)):
            for j in range(i + 1, len(a)):
                abs_diff = abs(a[i] - a[j])

                if abs_diff > self.maximumDifference:
                    self.maximumDifference = abs_diff
                    
        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
