#to check if the number is prime or not
def is_prime(n):
     if n < 2:
         return False
     for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
             return False 
     return True

# for prime numbers less than 20
for num in range (2,20):
    if is_prime(num):
        print(num)

