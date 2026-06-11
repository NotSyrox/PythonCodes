import time

timeUntilOver = int(input("How Many Seconds To Wait: ")) #seconds

while timeUntilOver >= 1:
    if timeUntilOver != 1:
        print(f"Time Remaining: {timeUntilOver} seconds")
        timeUntilOver -= 1
        time.sleep(1)
    elif timeUntilOver == 1:
        print("Time's Up!")
        break

    
        