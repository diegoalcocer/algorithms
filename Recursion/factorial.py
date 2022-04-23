import questionary

'''
    The factorial of a positive integer n, denoted n!, is defined as the product of the integers from 1 to n. 
    If n = 0, then n! is defined as 1 by convention. More formally, for any integer n ≥ 0
    For example, 5! = 5 · 4 · 3 · 2 · 1 = 120.
'''

def calculate_factorial():
    number = int(questionary.text("Please enter a number to caculate it's factorial:").ask())    
    return number, factorial(number)

def factorial(number):
    # if number is 0, then factorial of number is 1 by convention
    if number == 0:
        return 1
    # n! = n * (n-1)!
    res = number*factorial(number-1)
    return res
    
fact={0:1}
def factorial_memoization(number):
    if number in fact:
        return fact[number]
    fact[number] = number*factorial_memoization(number-1)
    return fact[number]

if __name__ == '__main__':
    result = calculate_factorial()
    print(f'{result[0]}! = {result[1]}')