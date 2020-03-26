import win32api
import time


f = open("C:\MouseLogger.txt",'w')
LKstat = win32api.GetAsyncKeyState(0x01)  
RKstat = win32api.GetAsyncKeyState(0x02)
ENstat = win32api.GetAsyncKeyState(0x0D)

while True:
    
    LK = win32api.GetKeyState(0x01)  
    RK = win32api.GetKeyState(0x02)
    EK = win32api.GetKeyState(0x0D)
    
    if LK != LKstat:
        LKstat = LK
        if LK < 0:
            f.write('Left Key Pressed' + time.strftime(' %H:%M:%S\n'))
        else:
            f.write('Left Key Released'+ time.strftime(' %H:%M:%S\n'))

    if RK != RKstat:  
        RKstat = RK
        if RK < 0:
            f.write('Right Key Pressed'+ time.strftime(' %H:%M:%S\n'))
        else:
            f.write('Right Key Released'+ time.strftime(' %H:%M:%S\n'))
    
    if EK != ENstat:
        f.close()
        print("Enter Key Pressed")
        exit(0)
