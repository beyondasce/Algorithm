def fib(n):
    a = 0
    b = 1
    while n > 0:
         a,b = b,a+b
         n -= 1
    return a

def fib_gui(n):
    if n <= 0:
       return 0
    if n == 1:
       return 1
    return fib_gui(n-1) + fib_gui(n-2)

if __name__ == "__main__":
    for i in range(5):
        print(fib(i))
        print(fib_gui(i))
