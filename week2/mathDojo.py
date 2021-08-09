class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for j in nums:
            self.result += j
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for j in nums:
            self.result -= j
        return self

    def printResult(self):
        print(self.result)

# create an instance:
md = MathDojo()
# to test:
md.add(2).add(2,5,1).subtract(3,2).printResult()
md.subtract(5,3).add(0,434,204).subtract(30000,223432).printResult()
md.add(234.43).add(2,5,932432.322).subtract(3,2).printResult()
# print(x)	# should print 5
# run each of the methods a few more times and check the result!

