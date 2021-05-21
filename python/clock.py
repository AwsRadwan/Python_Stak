def clockhandangles(Sec):
    minute=int(Sec/60)
    hour=int(minute/60)
    sec=Sec-(hour*3600 + minute*60)
    arr=[hour,minute,sec]
    print(arr)
    
clockhandangles(3000)