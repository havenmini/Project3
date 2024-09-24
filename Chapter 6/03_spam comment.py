c1 = "hello dai k chha"
c2 = "hello dai khana bhayo"
c3 = "good morning"

message = input("Enter your comment :")

if((c1 in message) or (c2 in message) or (c3 in message)):
    print ("this comment is a spam")

else:
    print("this comment is not a spam")