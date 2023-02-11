import time
from plyer import notification

def isTimeCorrect(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return print('time is wrong')

input_time = input('Type your reminder time in this format HH:MM\n')




while (isTimeCorrect(input_time)):
    curr_time = str(time.strftime("%H:%M", time.localtime()))
    if curr_time==input_time:
        #print("Yes")
        if __name__=="__main__":

                notification.notify(
                    title = "HEADING HERE",
                    message=" DESCRIPTION HERE" ,
                
                    # displaying time
                    timeout=2
        )
                # waiting time
                time.sleep(7)
        break
