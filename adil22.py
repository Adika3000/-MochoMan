import time

t = 0

while t<=60:
        
    mins, secs = divmod(t, 60)
    timer = ('{:02d}:{:02d}'.format(mins, secs))
    print(timer, end='\r')
    time.sleep(1)
    t = t + 1
