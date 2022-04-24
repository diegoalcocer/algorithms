import sys
import fire
import questionary

# __________________________
#  - Fibonacci algorithms -
# --------------------------

def fib(n):
    ''' Calculates fib using a naive recursive approach.
    To calculate fib(n) we call it recursively 2 times: the first time for (n-1) and the other for (n-2)
    This is the correct solution, but it is not optimized
    '''
    # fib(1) = fib(2)= 1
    if n<=2:
        f=1
    else:
        # fib(n) = fib(n-1) + fib(n-2)
        f = fib(n-1) + fib(n-2)
    return f

fib_memo = {}
def fib_memoization(n):
    ''' Calculates fib using memoization.
    To calculate fib(n) we call it recursively for fib(n-1) and to calculate the fib(n-2) we re-use the solutions already calculated for fib(n-1)
    The time complexity is linear
    '''
    #if we know fib(n) (it was saved in the dictionary fib_memo) we return it
    if n in fib_memo:
        return fib_memo[n]

    # if we don't know the answer, we calculate it, using the same logic as in the naive approach
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)    
    # We save the solution in the dictionary fib_memo, so that we can later remember it and re-use it
    fib_memo[n] = f
    return f

fib_bot ={}
def fib_bottomUp(n):
    '''Calculates fib using the bottom-up approach.
    To calculate fib(n) we use the for iterator to start from the base cases - fib(1) = fib(2)= 1 - and we build our way up
    The time complexity is linear
    '''
    for k in range(1, n+1):
        # fib(1) = fib(2)= 1
        if k <= 2:
            f = 1
        else:
            # fib(n) = fib(n-1) + fib(n-2). Since we do a bottom up approach
            # we know that we always have the 2 previous values in memory
            f = fib_bot[k-1] + fib_bot[k-2]
        fib_bot[k] = f
    return fib_bot[n]


# __________________________
#  - CLI (fire and questionary) -
# --------------------------

def main_menu():
    action = questionary.select("What algorithm would you like to use to get the fibonacci number?",
    choices=["Naive Recursive","Memoized", "Bottom-up", "Exit"]).ask()
    return action

def run(number=0):
    action = main_menu()
    if number == 0:
        n = int(questionary.text("Number: ").ask())
    else:
        n = number

    if action == "Naive Recursive":
        res = fib(n)
        time_complexity = "Naive Recursive has a time complexity = θ(2**n)"
    elif action == "Memoized":
        res = fib_memoization(n)
        time_complexity = "Memoized has a time complexity = θ(n)"        
    elif action == "Bottom-up":
        res = fib_bottomUp(n)
        time_complexity = "Bottom-up has a time complexity = θ(n)"
    else:
        sys.exit("See you soon. Cheers!!")

    print(f'fib({n}) = {res}')
    print(f'{time_complexity}')


if __name__ == "__main__":
    fire.Fire(run)