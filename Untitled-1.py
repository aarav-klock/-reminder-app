print("What do you want to be reminded for?")
print("1. Workout" ,"2. Classes time table", "3. Day time table", "4. Meeting Schedule",sep="\n")
x=int(input("Choose a number:"))
if x==1:
    print("Do you want a workout reminder on sunday?:", "1. Yes (Monday-Sunday)","2. No  (Monday-Saturday)",sep="\n")
    a1=int(input("Choose one option:"))
    if a1==1:
        a_mon=input("What is your workout schedule for Monday?:")
        a_tues=input("What is your workout schedule for Tuesday?:")
        a_wed=input("What is your workout schedule for Wednesday?:")
        a_thurs=input("What is your workout schedule for Thursday?:")
        a_fri=input("What is your workout schedule for Friday?:")
        a_sat=input("What is your workout schedule for Saturday?:")
        a_sun=input("What is your workout schedule for Sunday?:")
    elif a1==2:
        a_mon6=input("What is your workout schedule for Monday?:")
        a_tue6=input("What is your workout schedule for Tuesay?:")
        a_wed6=input("What is your workout schedule for Wednesday?:")
        a_thu6=input("What is your workout schedule for Thursday?:")
        a_fri6=input("What is your workout schedule for Friday?:")
        a_sat6=input("What is your workout schedule for Saturday?:")
    else:
        print("Sorry, invalid input (Kindly choose either option 1 or 2)")
elif x==2:
    a2=int(input("How much classes do you want to add in a day?:"))
    xx=1
    while xx<=a2:
        print("On what time is your", xx, "st class?")
        a_time=input("Enter a valid time in numerics:")
        print("Which class do you have in", xx, "st period?")
        a_class=input("Enter the name of the period:")
        xx+=1        
elif x==4:
    print("At what date do you have your meeting?")
    b=(input("Enter date in the form of  DD/MM/YYYY: "))
    a_meeting=(b.split("/"))
    day=a_meeting[0]
    month=a_meeting[1]
    year=a_meeting[2]
    if int(month)==1:
        print("January",day,",",year)

        



































































'''elif x==3:
    print("Which of the following time table do you need?")
    print("1. Specefic schedule for a perticular day.", "2. Regular day schedule")
    a_day=int(input("Choose any one option:"))
    if a_day==1:
        a_perticular=input("For which date do you want to add your schedule?: ")
        a_schedule=input("Enter time and work")'''