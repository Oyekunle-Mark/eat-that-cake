# modify the function signature to take a default parameter cache
# which defaults to an empty dict
def fib(n, cache={}):
    # FIRST PASS => NO Memoization
    # SECOND PASS => With Memoization

    # write a base of case of n being zero or one
    # check if n is zero or one
    if n == 0 or n == 1:
        # return n in that case
        return n

    # check if n is in cache
    if n in cache:
        # return value of key n in cache
        return cache[n]

    # initialize nth_fib to the return value recursive call
    # to fib passing in n minus one and n minus two
    nth_fib = fib(n - 1) + fib(n - 2)

    # populate the cache with a key value pair of n and nth_fib
    cache[n] = nth_fib

    # return nth_fib
    return nth_fib


# third pass would be to code up an iterative solution to the problem
def fib_iter(n):
    # write a base of case of n being zero or one
    # check if n is zero or one
    if n == 0 or n == 1:
        # return n in that case
        return n

    # initialize prev_prev to zero
    prev_prev = 0
    # initialize prev to one
    prev = 1

    # loop through range of n minus one
    for _ in range(n - 1):
        # To get nth fibonacci ... do n-1 iterations.
        # initialize current to the sum of prev and prev_prev
        current = prev + prev_prev
        # initialize prev_prev to prev
        prev_prev = prev
        # initialize prev to current
        prev = current

    # return current
    return current
