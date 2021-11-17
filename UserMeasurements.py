''' Briggs '''


repeatCal = True
while repeatCal:
    def userMeasurements(height, weight, age):
        def hSize(hatSize):
            print("Your hat size is",round(hatSize,2),"inches.")
            return
        def jSize(adjustJacket, count, jacket):
            if age < 40:
                print("Your jacket size is",round(jacket,2),"inches.")
            else:
                if age >= 40 and age%10 == 0:
                    for i in range(0,(age//10)-4,1):
                        count += 1
                    jacketSize = adjustJacket*count + jacket
                    print("Since you are",age,"years old, your jacket size is",round(jacketSize,2),"inches.")
                else:
                    if age >= 40 and age%10 != 0:
                        for i in range(0,(age//10)-4,1):
                            count += 1
                        jacketSize = adjustJacket*count + jacket
                        print("Since your age is not divisible by ten evenly, your jacket size is",round(jacketSize,2),"inches.")
                        return
        def wSize(adjustWaist, countTwo, waist):
            if age <= 29:
                print("Your waist size is",round(waist,3),"inches.")
            else:
                if age >= 30 and age%2 == 0:
                    for i in range(30,age+2,2):
                        countTwo+=1
                    waistSize = adjustWaist*countTwo + waist
                    print("Since you are",age,"years old, your waist size is",round(waistSize,2),"inches.")
                else:
                    if age >= 31 and age%2 != 0:
                        for i in range(31,age+2,2):
                            countTwo+=1
                        waistSize = adjustWaist*countTwo + waist
                        print("Since your age is not divisible by 2 evenly, your waist size is",round(waistSize,2),"inches.")
                        return
        hSize((weight/height)*2.9)
        jSize(1/8, 0, (height*weight)/288)
        wSize(1/10, 0, weight/5.7)
    userMeasurements(int(input("How tall are you in inches? ")), int(input("How much do you weigh in pounds? ")), int(input("How many years old are you? ")))
    invalidRepeatResponse = True
    while invalidRepeatResponse:
        askUserToRepeat = input("Want to repeat the calculation? (Y or N) ")
        askUserToRepeat = askUserToRepeat.lower()
        if askUserToRepeat == 'y':
            repeatCal = True
            invalidRepeatResponse = False
        elif askUserToRepeat == 'n':
            repeatCal = False
            invalidRepeatResponse = False
        else:
            print("Please choose Y or N")
            invalidRepeatResponse = True
