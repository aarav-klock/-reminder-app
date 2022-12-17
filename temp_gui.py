from tkinter import *
from tkinter import ttk
import random
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time


t = Tk()
t.title('Reminder App')
t.geometry("500x300")


#Image
notifier_img = ImageTk.PhotoImage(Image.open("notify_label.png"))
label = Label(t, image = notifier_img)
label.pack()


#Greeting
def greeting():
    curr_time = str(time.strftime("%H:%M", time.localtime()))
    if curr_time <= "12:00":
        return("Good Morning!")
    elif curr_time >= "12:00" and curr_time <= "16:00":
        return("Good Afternoon!")
    else:
        return("Good Evening!")
greeting = Label(t,text = greeting(), font=("Helvetica",14,"bold")).place(x=12,y=70)

reminder_title = Label(t, text = "What do you want to be reminded for?", font=("poppins",12)). place(x=12,y=100)



#Notifier
def get_details():

    get_title = title.get()
    #get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" and get_time == "":
        messagebox.showerror("Alert","All fields are required!")
    elif get_title == "":
        messagebox.showerror("Alert", "Title is empty, please enter all the details!")
    elif get_time == "":
        messagebox.showerror("Alert", "Time is empty, please enter all the details!")
    else:

        motivational_quotes=["Never put off until tomorrow what you can do today.","We are what we repeatedly do. Excellence then, is not an act, but a habit.","Be humble. Be hungry. And always be the hardest worker in the room.","Work hard and be kind and amazing things will happen.","Hard work beats talent when talent doesn’t work hard.","There are no secrets to success. It is the result of preparation, hard work, and learning from failure.","Perseverance is the hard work you do after you get tired of doing the hard work you already did.","Nothing will work unless you do.","Work hard in silence, let your success be your noise.","You don’t have to see the whole staircase, just take the first step.","You can have it all. You just can’t have it all at once.","If you get tired, learn to rest, not to quit.","Believe you can and you’re halfway there.","It always seems impossible until it’s done.","Progress is impossible without change, and those who cannot change their minds cannot change anything.","What we fear of doing most is usually what we most need to do.","Every accomplishment starts with the decision to try."]
        motivation_index= random.randint(0,len(motivational_quotes)-1)
        output_motivation = motivational_quotes[motivation_index]

        def isTimeCorrect(get_time):
            try:
                time.strptime(get_time, '%H:%M')
                return True
            except ValueError:
                messagebox.showerror("Alert", "Time is invalid, please enter valid time in HH:MM format.")
    


        while (isTimeCorrect(get_time)):
            curr_time = str(time.strftime("%H:%M", time.localtime()))
            if curr_time==get_time:
                #print("Yes")
                if __name__=="__main__":
                    notification.notify(title=get_title,
                                message= output_motivation,
                                app_name="Notifier",
                                app_icon="ico.ico",
                                toast=True,
                                timeout=10)
                    time.sleep(7)
                break




def meeting_win():
    new = Toplevel(t)
    new.geometry("500x300")
    new.title("Meeting Schedule")
        
    global notifier_img1
    notifier_img1 = ImageTk.PhotoImage(Image.open("notify_label.png"))
    label = Label(new, image = notifier_img1)
    label.pack()



    # Label - Title
    t_label = Label(new, text="Title to Notify:",font=("poppins", 10))
    t_label.place(x=12, y=145)

    # ENTRY - Title
    global title
    title = Entry(new, width="25",font=("poppins", 13))
    title.place(x=123, y=145)

    # Label - Time
    time_label = Label(new, text="Set Time:", font=("poppins", 10))
    time_label.place(x=12, y=175)

    # ENTRY - Time
    global time1
    time1 = Entry(new, width="5", font=("poppins", 13))
    time1.place(x=123, y=175)

    # Label - min
    time_min_label = Label(new, text="HH:MM", font=("poppins", 10))
    time_min_label.place(x=175, y=180)

    # Button
    but = Button(new, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised",
                command=get_details)
    but.place(x=170, y=230)

meeting_button = ttk.Button(t, text ="Meeting Schedule", command = meeting_win).pack(side=LEFT, padx= 10, pady= 60)

def workout_win():
    new = Toplevel(t)
    new.geometry("500x300")
    new.title("Workout Schedule")

    Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30)

workout_button = ttk.Button(t, text ="Workout Schedule", command = workout_win).pack(side=LEFT ,pady = 60)

def birthday_win():
    new = Toplevel(t)
    new.geometry("500x300")
    new.title("Birthday/Anniversary Reminder")

    Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30)

birthday_button = ttk.Button(t, text ="Birthday/Anniversary Reminder", command = birthday_win).pack(side=LEFT,padx=20,pady=60)


#Dropdown
'''
def show():
	label.config( text = clicked.get() )
options = [
    "Custom Task",
	"Meeting Schedule",
	"CLass Schedule",
	"Birthday/Anniversary Reminder",
	"Water drinking Reminder",
	"Medicine Reminder",
	"Assignments Deadline Reminder",
	"Workout Schedule"
]
clicked = StringVar()
clicked.set( "Custom Task" )
drop = OptionMenu( t , clicked , *options ).pack()
#drop.place()
button = Button( t , text = "Proceed" , command = show ).pack()
#button.place()

label = Label( t , text = " " )
label.pack()
'''


t.resizable(0,0)
t.mainloop()
