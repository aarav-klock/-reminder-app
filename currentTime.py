import datetime
currdate = str(datetime.datetime.now())
print(currdate.split(" ")[1])


import time
curr_time = time.strftime("%H:%M:%S", time.localtime())
print(curr_time)