#input
Name = input("Enter Name: ")
Roll_Number = int(input("Enter Roll_Number: "))
sub1 = int(input("Enter the marks obtained on English: "))
sub2 = int(input("Enter the marks obtained on Nepali: "))
sub3 = int(input("Enter the marks obtained on Computer: "))
sub4 = int(input("Enter the marks obtained on Economic: "))
sub5 = int(input("Enter the marks obtained on Account: "))
sub6 = int(input("Enter the marks obtained on Social Studies & Life Skill: "))

#processing.
Total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
print("Total: {}".format(Total))

Avg = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6)/6
print("Avg: {}".format(Avg))

#RESULT.
if sub1 < 40:
    print("RESULT: FAILED!!")
elif sub2 < 40:
    print("RESULT: FAILED!!")
elif sub3 < 40:
    print("RESULT: FAILED!!")
elif sub4 < 40:
    print("RESULT: FAILED!!")
elif sub5 < 40:
    print("RESULT: FAILED!!")
elif sub6 < 40:
    print("RESULT: FAILED!!")
else: 
     print("RESULT: PASS!!")

#REMARKS.
if sub1 < 40:
    print("REMARK: NEED TO WORK MORE ON ENGLISH.")
elif sub2 < 40:
    print("REMARK: NEED TO WORK MORE ON NEPALI.")
elif sub3 < 40:
    print("REMARK: NEED TO WORK MORE ON COMPUTER.")
elif sub4 < 40:
    print("REMARK: NEED TO WORK MORE ON ECONOMICS.")
elif sub5 < 40:
     print("REMARK: NEED TO WORK MORE ON ACCOUNT.")
elif sub6 < 40:
     print("REMARK: NEED TO WORK MORE ON SOCIAL STUDIES & LIFE SKILL.")
else: 
     print("REMARK: EXCELLENT!!")


