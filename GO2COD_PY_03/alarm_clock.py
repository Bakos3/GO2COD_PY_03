import time
from datetime import datetime
from playsound import playsound

while True:
    try:
        alarm_time = input("Enter the alarm time in 24-hour format (HH:MM:SS): ")
        datetime.strptime(alarm_time, "%H:%M:%S")  # Validate time format
        break
    except ValueError:
        print("Invalid time format! Please try again.")

task = input(f"Enter task to do at {alarm_time}: ")
print(f"You will be alarmed at {alarm_time} for: {task}.")

print("Waiting for the alarm time...")
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print(f"Time to {task}!")
        
        try:
            playsound("C:\\Users\\Kiyane\\Documents\\Go2Cod\\GO2COD_PY\\GO2COD_PY_03\\mixkit-morning-clock-alarm-1003.wav")  # Adjust path if needed
        except Exception as e:
            print(f"Error playing sound: {e}")
        
        break
    
    time.sleep(1)
