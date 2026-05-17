# -------- Countdown Timer --------
import time

# -------- User Input --------
total_seconds = int(input("Enter the time in seconds: "))

# -------- Countdown Logic --------
for x in range(total_seconds, 0, -1):

    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)

# -------- Timer Complete --------
print("TIME'S UP!")