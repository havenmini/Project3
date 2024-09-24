number= int(input("Enter a number: "))

for i in range(2, number):
    if(number%i) == 0:
        print("Number is not prime")
        break

else:
    print("Number is prime")