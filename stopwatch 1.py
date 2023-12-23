import tkinter as tk

class Stopwatch(tk.Frame):
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.new_time = ''
        self.running = False
        self.total_hours = 0
        self.total_minutes = 0
        self.total_seconds = 0
        self.pack()
        self.features()

    def features(self):
        self.stopwatch_label = tk.Label(self, text='00:00:00', background="black", foreground="blue",
                                        font=('arial', 85, "bold"))
        self.stopwatch_label.pack()
        self.start_time_button = tk.Button(self, text="Start", height=5, width=7, font=('arial', 19, "bold"), background="green", command=self.start_time)
        self.start_time_button.pack(side=tk.LEFT)
        self.stop_time_button = tk.Button(self, text="Stop", height=5, width=7,
                                          font=('arial', 19, "bold"), background="red", command=self.pause_time)
        self.stop_time_button.pack(side=tk.LEFT)
        self.reset_time_button = tk.Button(self, text="Reset", height=5, width=7,
                                           font=('arial', 19, "bold"), background="orange", command=self.reset_time)
        self.reset_time_button.pack(side=tk.LEFT)
        self.quit_time_button = tk.Button(self, text="Quit", height=5, width=7,
                                          font=('arial', 19, "bold"), background="yellow", command=self.window.quit)
        self.quit_time_button.pack(side=tk.LEFT)
        self.window.title('Stopwatch')

    def start_time(self):
        if not self.running:
            self.new_time = self.stopwatch_label.after(1000, self.change)
            self.running = True

    def pause_time(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.new_time)
            self.running = False

    def reset_time(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.new_time)
            self.running = False
        self.total_hours, self.total_minutes, self.total_seconds = 0, 0, 0
        self.stopwatch_label.config(text="00:00:00")

    def change(self):
        self.total_seconds += 1
        if self.total_seconds == 60:
            self.total_minutes += 1
            self.total_seconds = 0
        if self.total_minutes == 60:
            self.total_hours += 1
            self.total_minutes = 0
        total_hours_string = f"{self.total_hours}" if self.total_hours > 9 else f'0{self.total_hours}'
        total_minutes_string = f"{self.total_minutes}" if self.total_minutes > 9 else f'0{self.total_minutes}'
        total_seconds_string = f"{self.total_seconds}" if self.total_seconds > 9 else f'0{self.total_seconds}'
        self.stopwatch_label.config(text=total_hours_string + ':' + total_minutes_string + ':' + total_seconds_string)
        self.new_time = self.stopwatch_label.after(1000, self.change)

root = tk.Tk()
obj = Stopwatch(window=root)
obj.mainloop()
