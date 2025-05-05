import time

t = input ( "digite o tempo (em segundo): ")

if t.isdigit():
    t = int(t)
else: 
    print ("entrada invalida")
    quit ()

while t: # 0 -> false / 1,2 -> true
    minutes, seconds = divmod(t, 60)
    timer = "{:02d} : {:02d}".format(minutes,seconds)
    print (timer, end = "\r")
    #time.sleep(1)
    t = t-1
    