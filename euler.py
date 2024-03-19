def main():
    n = 5
    print("euler({}) = {:.5f}".format(n, euler(n)))
    print("{} square is : {} ".format(n, sqare(n)))

def fact(k) :
    if k <= 1 :
        return 1
    else:
        return k * fact(k - 1)


def euler(n) :
    if n <= 0 :
        return 1
    else:
        return 1/(fact(n)) + euler(n - 1)
    
<<<<<<< HEAD
def sqare(n):
    return n * n
    
=======
>>>>>>> feature/issue3


if __name__ == "__main__":
    main()