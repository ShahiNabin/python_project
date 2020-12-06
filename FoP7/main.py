import time


def elapsed_time(f) -> object:
    def wrapper(num):
        t1 = time.time()
        f(num)  # do the stuff defined in the passed function
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')

    return wrapper


@elapsed_time  # decorator takes loopFactorial() and wrape it with elapsed_time() function
def loopFactorial(num) -> object:
    fac = 1
    for i in range(1, num + 1):
        fac = fac * i
    print("Factorial of ", num, " is ", fac)


@elapsed_time
def ifFactorial(num) -> object:
    print(type(num))
    if num == 1:
        return num
    else:
        return num * ifFactorial(num - 1)


def main():
    number = int(input("Please, enter a number: "))
    print('---')
    ifFactorial(number)
    print('---')
    loopFactorial(number)

if __name__ == '__main__': main()
