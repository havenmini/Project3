English = int(input("Enter English Subject marks: "))
Nepali = int(input("Enter Nepali Subject marks: "))
Maths = int(input("Enter Maths Subject marks: "))
Science = int(input("Enter Science Subject marks: "))
Social = int(input("Enter Social Subject marks: "))
Eco = int(input("Enter Eco Subject marks: "))
Account = int(input("Enter Account Subject marks: "))

percentage = (English+Nepali+Maths+Science+Social+Eco+Account)/7

if(English>=35 and Nepali>=35 and Maths>=35 and Science>=35 and Social>=35 and Eco>=35 and Account>=35):
    print ("You have passed in ", percentage)

else:
    print("You have failed")
