import math
import argparse

def prime(num:int) -> bool:
    if num > 1:
       for i in range(2,num//2):
           if (num % i) == 0:
               return False
       else:
           return True
    else:
        return False

def main(size:int) -> None:
    for i in range(size):
        num = 2**2**i + 1
        print(f"2^2^{i} : {num} : {prime(num)}")


if __name__ == "__main__":
    ## Printing all the fermat primes 2^2^n
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for main')
    args = parser.parse_args()
    main(args.integers[0])
