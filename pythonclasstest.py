class test():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def subtraction(self):
        print(self.num1-self.num2)
    def addition(self):
        print(self.num1+self.num2)

number = test(1,2)
print (number.subtraction())
number.num1 = 2
print (number.addition())