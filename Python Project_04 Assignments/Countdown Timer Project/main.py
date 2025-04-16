# =============================== ⏳ Countdown Master | By Muzna Amir Zubairi ===============================
import time
print("TimerX | Built by Muzna Amir Zubairi")

def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timmer = "{:02d} : {:02d}".format(minutes, seconds)
        print(timmer)
        time.sleep(1)
        t -= 1
    print("✅ Time’s Up! Well Done!")

t = input("Set Your Countdown Seconds : ")
countdown(int(t))
