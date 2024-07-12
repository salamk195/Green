number = int(input("enter your number"))
for i in range(2,int(number / 2)):
        if(number % i) == 0:
            print(str(number) + " is not prime")
        else:
              print(str(number) + "is a prime number")
