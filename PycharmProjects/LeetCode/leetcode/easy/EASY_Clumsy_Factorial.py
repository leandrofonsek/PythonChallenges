"""
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.
"""

number = 10
operation_counter=1
expression=""
for i in reversed(range(number+1)):

    if i == 0 or i == number:
        continue

    if i == number - 1:
        expression = str(number) + " * " + str(i)
        print(expression)
        operation_counter = operation_counter + 1
        continue

    if operation_counter == 1:
        expression = expression + " * " + str(i)
        operation_counter = operation_counter + 1
    elif operation_counter == 2:
        expression = expression + " // " + str(i)
        operation_counter = operation_counter + 1
    elif operation_counter == 3:
        expression = expression + " + " + str(i)
        operation_counter = operation_counter + 1
    elif operation_counter == 4:
        expression = expression + " - " + str(i)
        operation_counter = 1


print(eval(expression))