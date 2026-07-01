import time
import winsound

def set_alarm(alarm_time):
    current_time = time.strftime("%H:%M:%S")
    print(f"Current time: {current_time}")
    print(f"Alarm set for: {alarm_time}")

    while True:
        if time.strftime("%H:%M:%S") == alarm_time:
            print("Time to wake up!")
            play_alarm_sound()
            break
        time.sleep(1)

def play_alarm_sound():
    # Play a beep sound (for Windows)
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)

if __name__ == "__main__":
    # Set the alarm time in 24-hour format (HH:MM:SS)
    alarm_time = "13:45:00"  # Example: 1:45 PM

    set_alarm(alarm_time)
