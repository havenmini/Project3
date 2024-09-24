M = int(input("Enter your marks :"))


if (M<=100 and M>=80):
    print ("Congratulations! You have passed in Distniction.")

elif(M<80 and M>=60):
    print("Congratulations! You have passed in first Division.")

elif(M<60 and M>=45):
    print("Congratulations! You have passed in Second Division.")

elif(M<45 and M>=35):
    print("Congratulations! You have passed in Third Division.")

else:
    print("Please try again. You have failed.")

print("Thank you for visiting our site")
