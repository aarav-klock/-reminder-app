import time
import random
from plyer import notification

def main():

    #Greeting
    curr_time = str(time.strftime("%H:%M", time.localtime()))
    if curr_time <= "12:00":
        print("Good Morning!")
    elif curr_time >= "12:00" and curr_time <= "4:00":
        print("Good Afternoon!")
    else:
        print("Good Evening!")


    #User-Input
    print("What do you want to be reminded for?")
    print("1. Class Schedule" ,"2. Meeting Schedule", "3. Workout", "4. Custom task",sep="\n")
    Remainder_for=int(input("Choose a number: "))


    if Remainder_for==1:
        data_extracted = class_schedule()
        notifier(data_extracted)
    elif Remainder_for==2:
        #date()
        data_extracted = meeting_schedule()
        notifier(data_extracted)
    elif Remainder_for==3:
        data_extracted = workout()
        notifier(data_extracted)
    elif Remainder_for==4:
        a = custom()
        notifier(a)

def custom():
    input_task=input("Enter your task: ")
    input_time = input("Enter Time: ")
    custom_sched = {}
    custom_sched[input_task]=input_time
    return custom_sched

def workout():  
    '''print("Do you want a workout reminder on sunday?:", "1. Yes (Monday-Sunday)","2. No  (Monday-Saturday)",sep="\n")
    YOUR_CHOICE=int(input("Choose one option:"))
    if YOUR_CHOICE==1:
        for_mon=input("What is your workout schedule for Monday?:")
        for_tues=input("What is your workout schedule for Tuesday?:")
        for_wed=input("What is your workout schedule for Wednesday?:")
        for_thurs=input("What is your workout schedule for Thursday?:")
        for_fri=input("What is your workout schedule for Friday?:")
        for_sat=input("What is your workout schedule for Saturday?:")
        for_sun=input("What is your workout schedule for Sunday?:")
    elif YOUR_CHOICE==2:
        For_Mon=input("What is your workout schedule for Monday?:")
        For_Tue=input("What is your workout schedule for Tuesay?:")
        For_Wed=input("What is your workout schedule for Wednesday?:")
        For_Thurs=input("What is your workout schedule for Thursday?:")
        For_Fri=input("What is your workout schedule for Friday?:")
        For_Sat=input("What is your workout schedule for Saturday?:")
    else:
        print("Sorry, invalid input (Kindly choose either option 1 or 2)")'''

    workout_sched = input("Enter your workout schedule for today: ")
    workout_time = input("Enter your reminder time in this format HH:MM: ")
    workout_dict = {}
    workout_dict[workout_sched] = workout_time
    return workout_dict

def class_schedule():
     no_of_classes=int(input("How much classes do you want to add in a day? "))
     count=0
     time_table_dict={}
     while count<no_of_classes:
        sub_name = input("Enter subject name: ")
        input_time = input("Enter your reminder time in this format HH:MM: ")
        time_table_dict[sub_name] = input_time
        count+=1
     return time_table_dict

def date():
    def months_in_Q1(day):
        if int(day)>30:
            print("Invalid date")
            date()
        else:
            pass
    def months_in_Q2(day):
        if int(day)>31:
            print("Invalid date")
            date()
        else:
            pass

    print("At what date do you have your meeting?")
    for_date=(input("Enter date in the form of  DD/MM/YYYY: "))
    meeting=(for_date.split("/"))
    day=meeting[0]
    month=meeting[1]
    year=meeting[2]
    if int(month)==1:
        months_in_Q2(day)
        print("January",day,",",year)
        
    elif int(month)==2:
        if int(day)>=29:
            print("Invalid date")
            date()
        print("Febuary",day,",",year)
        
    elif int(month)==3:
        months_in_Q2(day)
        print("March",day,",",year)
        
    elif int(month)==4:
        months_in_Q1(day)
        print("April",day,",",year)
        
    elif int(month)==5:
        months_in_Q2(day)
        print("May",day,",",year)
        
    elif int(month)==6:
        months_in_Q1(day)
        print("June",day,",",year)
        
    elif int(month)==7:
        months_in_Q2(day)
        print("July",day,",",year)
        
    elif int(month)==8:
        months_in_Q2(day)
        print("August",day,",",year)
        
    elif int(month)==9:
        months_in_Q1(day)
        print("September",day,",",year)
        
    elif int(month)==10:
        months_in_Q2(day)
        print("October",day,",",year)

    elif int(month)==11:
        months_in_Q1(day)
        print("November",day,",",year)

    elif int(month)==12:
        months_in_Q2(day)
        print("December",day,",",year)
    else:
        print("Invalid Month")
        date()

def meeting_schedule():

    '''time_for_meet=input("What time do you want to want to add meeting for?(Enter in this format HH:MM): ")
    time_for_meet= time_for_meet.split(":")
    am=time_for_meet[0]
    pm=time_for_meet[1]
    for_am_pm=int(input("Choose one of the following(1. AM      2. PM): "))
    if for_am_pm==1:
        pass
    elif for_am_pm==2:
        a_24hrs=int(am)+12
    else:
        print("Enter a valid time in 12hrs system")



    if int(am)>=13:
        print("Invalid date")
    
    if int(pm)>=60:
        print("Enter a valid time in 12hrs system")'''


    meeting_title = input("Enter meeting title: ")
    meeting_time = input("Enter your reminder time in this format HH:MM: ")
    meeting_dict = {}
    meeting_dict[meeting_title]=meeting_time
    return meeting_dict

def notifier(data_extracted):
    
    motivational_quotes=["Never put off until tomorrow what you can do the day after tomorrow.","We are what we repeatedly do. Excellence then, is not an act, but a habit.","Be humble. Be hungry. And always be the hardest worker in the room.","Work hard and be kind and amazing things will happen.","Hard work beats talent when talent doesn’t work hard.","There are no secrets to success. It is the result of preparation, hard work, and learning from failure.","Perseverance is the hard work you do after you get tired of doing the hard work you already did.","Nothing will work unless you do.","Work hard in silence, let your success be your noise.","You don’t have to see the whole staircase, just take the first step.","You can have it all. You just can’t have it all at once.","If you get tired, learn to rest, not to quit.","Believe you can and you’re halfway there.","It always seems impossible until it’s done.","Progress is impossible without change, and those who cannot change their minds cannot change anything.","What we fear of doing most is usually what we most need to do.","Every accomplishment starts with the decision to try."]
    motivation_index= random.randint(0,len(motivational_quotes)-1)
    output_motivation = motivational_quotes[motivation_index]


    for i in range(len(data_extracted)):
        input_time = list(data_extracted.values())[i]
        input_title = list(data_extracted.keys())[i]

    

        def isTimeCorrect(input_time):
            try:
                time.strptime(input_time, '%H:%M')
                return True
            except ValueError:
                return print('time is wrong')
    


        while (isTimeCorrect(input_time)):
            curr_time = str(time.strftime("%H:%M", time.localtime()))
            if curr_time==input_time:
                #print("Yes")
                if __name__=="__main__":

                        notification.notify(
                            title = input_title,
                            message= output_motivation ,
                        
                            # displaying time
                            timeout=2
                )
                        # waiting time
                        time.sleep(7)
                break

main()