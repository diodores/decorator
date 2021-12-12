from dec import log, decorator

@decorator
@log
def summator(a, b, c):
    return a + b + c

f = summator(2, 4, 5)

