from addition import Addition
# You don't need to change the import statement
# now you can use Addition.add() function from the addition module like this:
# res = Addition.add(100, 150)
# the Addition.add() function takes in two parameters `num1` and `num2` and return the sum of `num1` and `num2`


# Please create and implement a Calculator class, which makes use of the `addition` module.
# Your Calculator should achieve these goals:
# - It should implement `Addition.add()`, `subtract()`, `multiply()` and `divide()` methods.
# - It cannot use addition, subtraction, multiplication and division operators (`+`, `-`, `*` and `/`) directly.
#   Instead, it should be only based on the `Addition.add()` function from the `addition` module.
# - To simplify the problem, you may expect input for the multiply() and divide() methods are all non-integers,
#   and will always be valid, i.e. all non-negative integers and no 0 as divisor.

# the class definition and a sample class method `Addition.add()` is provided below
class Calculator:

    # a sample add() method in our calculator is shown below
    # you may learn from it and implement the other methods
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from addition module

    # implement a class method `subtract()` that takes in num1 and num2 and return num1 - num2
    # your `subtract()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    @classmethod
    def subtract(cls, num1, num2):
        return Addition.add(num1, -num2)

    # implement a class method `multiply()` that takes in num1 and num2 and return num1 * num2
    # your `multiply()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 and num2 are always non-negative integers
    @classmethod
    def multiply(cls, num1, num2):
        if num1 == 0 or num2 == 0:
            return 0

        result = num1
        for _ in range(1, num2):
            result = Addition.add(result, num1)

        return result

    # implement a class method `divide()` that takes in num1 and num2 and return num1 // num2
    # your `divide()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 is always a non-negative integer, and num2 is always a positive integer
    @classmethod
    def divide(cls, num1, num2):
        if num1 == 0 or num2 == 0:
            return 0

        result = 0
        left = num1
        # while Addition.add(left, -num2) >= 0:
        while left >= num2:
            result = cls.add(result, 1)
            left = cls.subtract(left, num2)

        return result


# print('1+1=' + str(Calculator.add(1, 2)))
# print('2-1=' + str(Calculator.subtract(2, 1)))
# print('2*3=' + str(Calculator.multiply(2, 3)))
# print('3*2=' + str(Calculator.multiply(3, 2)))
# print('3*1=' + str(Calculator.multiply(3, 1)))
# print('1*3=' + str(Calculator.multiply(1, 3)))
# print('5*4=' + str(Calculator.multiply(5, 4)))
# print('0*4=' + str(Calculator.multiply(0, 4)))
# print('4*0=' + str(Calculator.multiply(4, 0)))
print('4/0=' + str(Calculator.divide(4, 0)))
print('0/4=' + str(Calculator.divide(0, 4)))
print('1/4=' + str(Calculator.divide(1, 4)))
print('4/1=' + str(Calculator.divide(4, 1)))
print('4/2=' + str(Calculator.divide(4, 2)))
print('6/2=' + str(Calculator.divide(6, 2)))
print('9/3=' + str(Calculator.divide(9, 3)))
print('3/3=' + str(Calculator.divide(3, 3)))
print('25/4=' + str(Calculator.divide(25, 4)))
