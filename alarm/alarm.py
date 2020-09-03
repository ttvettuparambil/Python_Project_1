
import winsound,time

a= int(input("Enter how many times I have beep  :"))
b= int(input("Enter when to wake up (in seconds) :"))

time.sleep(b)

for i in range(a):
    winsound.Beep(3000,100)
    winsound.Beep(2500,100)
    winsound.Beep(2000,100)    
    winsound.Beep(1000,100)    
    winsound.Beep(500,100)