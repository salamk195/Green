number = int(input("enter your number"))
for i in range(2,int(number / 2)):
         if (number % i) == 0:
           print(number, "is not a prime number")
         else:
           print(number, "is a prime number")
