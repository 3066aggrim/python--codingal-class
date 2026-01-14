sub1 = int(input("please enter the marks of english"))
sub2 = int(input("please enter the marks of science"))
sub3 = int(input("please enter the marks of social"))
sub4 = int(input("please enter the marks of maths"))
sub5 = int(input("please enter the marks of computer"))
sub6 = int(input("please enter the marks of nepali"))
sub7 = int(input("please enter the maeks of C.arts"))
sub8 = int(input("please enter the marks of local curriculum"))
sub9 = int(input("please enter the marks of H.P.E"))

total = sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8+sub9
average = total/9

if average >= 91 and average <= 100:
    print("your score is A++😘😘😘😘")

elif average >= 81 and average <= 80:
    print("your score is A+💕💕💕💕")

elif average >= 71 and average <= 79:
    print("your score is A😍😍😍😍")

elif average >= 60 and average <= 70:
    print("your score is B+🫡🫡🫡")

elif average >= 49 and average <= 59:
    print("your score is B😊😊😊")

elif average >= 38 and average <= 48:
    print("your score is C+🤦‍♂️🤦‍♂️🤦‍♂️")

elif average >= 27 and average <= 37:
    print("your score is C😒😒😒")

elif average >= 0 and average <= 26:
    print("your score is too low to be  shown☹️☹️☹️")
