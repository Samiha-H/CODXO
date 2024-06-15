import tkinter as tk
import time
import datetime
import math

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        self.alarm_time = None

        self.create_clock_face()
        self.update_clock()

        self.alarm_entry = tk.Entry(root)
        self.alarm_entry.pack()
        self.alarm_entry.insert(0, 'HH:MM:SS')

        self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack()

    def create_clock_face(self):
        self.canvas.create_oval(50, 50, 350, 350, outline="black", width=4)
        self.center_x = 200
        self.center_y = 200
        for i in range(12):
            angle = math.radians(i * 30)
            x = self.center_x + 140 * math.sin(angle)
            y = self.center_y - 140 * math.cos(angle)
            self.canvas.create_text(x, y, text=str(i + 1), font=("Arial", 20))

    def update_clock(self):
        self.canvas.delete("hands")  # Clear previous hands

        now = datetime.datetime.now()
        self.draw_hand(now.hour % 12 * 30 + now.minute * 0.5, 80, "blue", 4)  # Hour hand
        self.draw_hand(now.minute * 6, 120, "blue", 2)                      # Minute hand
        self.draw_hand(now.second * 6, 140, "red", 1)                       # Second hand

        self.root.after(1000, self.update_clock)
        
        if self.alarm_time and now.strftime("%H:%M:%S") == self.alarm_time:
            self.alarm_triggered()

    def draw_hand(self, angle, length, color, width):
        angle = math.radians(angle)
        x = self.center_x + length * math.sin(angle)
        y = self.center_y - length * math.cos(angle)
        self.canvas.create_line(self.center_x, self.center_y, x, y, fill=color, width=width, tags="hands")

    def set_alarm(self):
        self.alarm_time = self.alarm_entry.get()
        print(f"Alarm is set for {self.alarm_time}")

    def alarm_triggered(self):
        self.canvas.create_text(200, 200, text="WAKE UP!", fill="red", font=("Arial", 40))
        self.play_sound()

    def play_sound(self):
        try:
            import winsound
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        except ImportError:
            import os
            os.system('say "Wake up!"')

if __name__ == "__main__":
    root = tk.Tk()
    clock = AlarmClock(root)
    root.mainloop()
