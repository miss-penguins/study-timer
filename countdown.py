import time 

while True:
    my_time= int(input("Enter the time in seconds: "))

    for x in range(my_time, 0, -1):
        seconds= x%60
        minutes=int(x//60)%60
        hours= int(x//3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r") 
        time.sleep(1)



    print("\nTIME'S UP!!")

    time_again= input("Set another timer? (y/n): ")

    if time_again.lower() == "y":
        print("Starting again....")
        continue

    else:
        print("bYe bYe")
        break    
