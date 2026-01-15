medical_cause = (
    input("do your children had medical issuses during the semester? (yes or no)"))
attendence = int(input("please enter the students attendence"))

if medical_cause == "yes":
    print("he/she may join exams")

else:
    if attendence >= 75 or attendence <= 100:
        print(" he/she may attend exams")

    else:
        print("he/she may not attend exams")
