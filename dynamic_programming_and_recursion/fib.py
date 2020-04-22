def fib(n):
    # FIRST PASS => NO Memoization

    # write a base of case of n being zero or one
    # check if n is zero or one
    if n == 0 or n == 1:
        # return n in that case
        return n

    # otherwise, return the sum of recursive call
    # to fib passing in n minus one and n minus two
    return fib(n - 1) + fib(n - 2)
