import math
import time

def is_prime(num):
    if n <=1:
        return False
    if n %2 ==0:
        return n == 2
    
    max_div = math.floor(math.sqrt(n))
    for i  in range(3,1+max_div, 2):
        if n %i ==0:
            return False
    return True

def find_prime_in_range(start, end):
    t0 = time.time()
    count = 0
    
    for n in range(start, end+1):
        if is_prime(n):
            count+= 1
    t1 = time.time()
     
    time_taken = t1- t0
    print("total prime numbers in this range are: ", count)
    print("time reqiuired to find all prime number in range is :", time_taken)
