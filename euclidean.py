def main() :
    nu = int(input("Enter the number: "))
    num = int(input("Enter the number: "))
    if nu > num :
        a = nu
        b = num
    else:
        a = num
        b = nu
    print(gcd(a, b))

def gcd(a, b) :
    if b <= 0:
        return a
    else :
        return(gcd(b, a % b))

if __name__ == "__main__":
    main()