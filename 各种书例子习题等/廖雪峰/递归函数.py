def foo(n):
    if n == 1:
        return 1
    return n * foo(n-1)


print(foo(5))

