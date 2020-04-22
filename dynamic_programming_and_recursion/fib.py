# modify the function signature to take a default parameter cache
# which defaults to an empty dict
def fib(n):
    # FIRST PASS => NO Memoization
    # SECOND PASS => With Memoization

    # write a base of case of n being zero or one
    # check if n is zero or one
    if n == 0 or n == 1:
        # return n in that case
        return n

    # check if n is in cache
        # return value of key n in cache

    # otherwise, return the sum of recursive call
    # to fib passing in n minus one and n minus two
    return fib(n - 1) + fib(n - 2)

    # initialize nth_fib to the return value recursive call 
    # to fib passing in n minus one and n minus two
    # populate the cache with a key value pair of n and nth_fib
    # return nth_fib
