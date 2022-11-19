print("What do you want to be reminded for?")
print("1. Workout" ,"2. Classes time table", "3. Day time table", "4. Meeting Schedule",sep="\n")
x=int(input("Choose a number:"))
if x==1:
    print("Do you want a workout reminder on sunday?:", "1. Yes (Monday-Sunday)","2. No  (Monday-Saturday)","(Any other option other than 1 or 2 will be taken as 2)",sep="\n")
    a1=int(input("Choose one option:"))
    if a1==1:
        a_mon=input("What is your workout schedule for Monday?:")
        a_tues=input("What is your workout schedule for Tuesday?:")
        a_wed=input("What is your workout schedule for Wednesday?:")
        a_thurs=input("What is your workout schedule for Thursday?:")
        a_fri=input("What is your workout schedule for Friday?:")
        a_sat=input("What is your workout schedule for Saturday?:")
        a_sun=input("What is your workout schedule for Sunday?:")
    else:
        a_mon6=input("What is your workout schedule for Monday?:")
        a_tue6=input("What is your workout schedule for Tuesay?:")
        a_wed6=input("What is your workout schedule for Wednesday?:")
        a_thu6=input("What is your workout schedule for Thursday?:")
        a_fri6=input("What is your workout schedule for Friday?:")
        a_sat6=input("What is your workout schedule for Saturday?:")
elif x==2:
    a2=int(input("How much classes do you want to add in a day?:"))
    xx=1
    while xx<=a2:
        print("On what time is your", xx, " st class?")
        a_time=input("Enter a valid time in numerics:")
        print("Which class do you have in", xx, "period?")
        a_class=input("Enter the name of the period:")
        xx+=1























































'''
    elif a2==2:
        a_time2=int(input("What will be the class time/period:"))
        a_class2=input("Which class do you have on this time?:")
        a_time3=int(input("What will be the class time/period:"))
        a_class3=input("Which class do you have on this time?:")
    elif a2==3:
        a_time4=int(input("What will be the class time/period:"))
        a_class4=input("Which class do you have on this time?:")
        a_time5=int(input("What will be the class time/period:"))
        a_class5=input("Which class do you have on this time?:")
        a_time6=int(input("What will be the class time/period:"))
        a_class6=input("Which class do you have on this time?:")
    elif a2==4:
        a_time7=int(input("What will be the class time/period:"))
        a_class7=input("Which class do you have on this time?:")
        a_time8=int(input("What will be the class time/period:"))
        a_class8=input("Which class do you have on this time?:")
        a_time9=int(input("What will be the class time/period:"))
        a_class9=input("Which class do you have on this time?:")
        a_time10=int(input("What will be the class time/period:"))
        a_class10=input("Which class do you have on this time?:")
    elif a2==5:
        a_time11=int(input("What will be the class time/period:"))
        a_class11=input("Which class do you have on this time?:")
        a_time12=int(input("What will be the class time/period:"))
        a_class12=input("Which class do you have on this time?:")
        a_time13=int(input("What will be the class time/period:"))
        a_class13=input("Which class do you have on this time?:")
        a_time14=int(input("What will be the class time/period:"))
        a_class14=input("Which class do you have on this time?:")
        a_time15=int(input("What will be the class time/period:"))
        a_class15=input("Which class do you have on this time?:")
    elif a2==6:
        a_time16=int(input("What will be the class time/period:"))
        a_class16=input("Which class do you have on this time?:")
        a_time17=int(input("What will be the class time/period:"))
        a_class17=input("Which class do you have on this time?:")
        a_time17=int(input("What will be the class time/period:"))
        a_class17=input("Which class do you have on this time?:")
        a_time18=int(input("What will be the class time/period:"))
        a_class18=input("Which class do you have on this time?:")
        a_time19=int(input("What will be the class time/period:"))
        a_class19=input("Which class do you have on this time?:")
        a_time20=int(input("What will be the class time/period:"))
        a_class20=input("Which class do you have on this time?:")
    elif a2==7:
        a_time21=int(input("What will be the class time/period:"))
        a_class21=input("Which class do you have on this time?:")
        a_time22=int(input("What will be the class time/period:"))
        a_class22=input("Which class do you have on this time?:")
        a_time23=int(input("What will be the class time/period:"))
        a_class23=input("Which class do you have on this time?:")
        a_time24=int(input("What will be the class time/period:"))
        a_class24=input("Which class do you have on this time?:")
        a_time25=int(input("What will be the class time/period:"))
        a_class25=input("Which class do you have on this time?:")
        a_time26=int(input("What will be the class time/period:"))
        a_class26=input("Which class do you have on this time?:")
        a_time27=int(input("What will be the class time/period:"))
        a_class27=input("Which class do you have on this time?:")
    elif a2==8:
        '''
        