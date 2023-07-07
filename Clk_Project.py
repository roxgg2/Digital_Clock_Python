from tkinter import *
from datetime import *
import time
import winsound
import threading
from time import strftime
from tkinter.messagebox import *



def f1():
	cw.deiconify()
	mw.withdraw()
def f2():
	mw.deiconify()
	cw.withdraw()
def f3():
	ct.deiconify()
	mw.withdraw()
def f4():
	mw.deiconify()
	ct.withdraw()
def f5():
    alarm_frame.deiconify()
    mw.withdraw()
def f6():
    mw.deiconify()
    alarm_frame.withdraw()  
def f7():
    world_clock_frame.deiconify()
    mw.withdraw()
def f8():
    mw.deiconify()
    world_clock_frame.withdraw()
def f9():
    stopwatch_frame.deiconify()
    mw.withdraw()
def f10():
    mw.deiconify()
    stopwatch_frame.withdraw()

    
    
mw = Tk()
mw.title("Digital Clock")
mw.geometry("1000x500+100+100")
mw.configure(bg="black")
mw.iconbitmap("c.ico")
f = ("Arial",30,"bold","italic")
ft = ("Arial",20,"bold","italic")

lbl_Welcome = Label(mw,text = "Welcome To Digital Clock",font = f, anchor="center",bg="Light blue" )
lbl_Welcome.pack(pady=20)

btn_current = Button(mw,text = "Current time and date",font=ft,bg="yellow",command=f1)
btn_current.place(x=100,y=120)

btn_Count = Button(mw,text = "Countdown Timer",font=ft,bg="yellow",command=f3)
btn_Count.place(x=600,y=120)

btn_Alarm = Button(mw,text = "Alarm",font=ft,bg="yellow",command=f5)
btn_Alarm.place(x=150,y=240)




cw = Toplevel(mw)
cw.title("Current Time and Date")
cw.iconbitmap("d.ico")
cw.geometry("500x330+100+100")
cw.configure(bg="black")


lbl_Time = Label(cw,text="Current Time:-",font = ft,bg="yellow")
lbl_Time.place(x=10,y=20)
lbl_time = Label(cw, font=ft,anchor='center',bg="yellow")
lbl_time.place(x=250,y=20)

def t():
    string = strftime('%H:%M:%S %p')
    lbl_time.configure(text=string)
    lbl_time.after(1000, t)

lbl_Date = Label(cw,text="Current Date:-",font=ft,bg="yellow")
lbl_Date.place(x=10,y=100)

lbl_date = Label(cw, font=ft,anchor='center',bg="yellow")
lbl_date.place(x=250,y=100)
today = date.today()
lbl_date.configure(text=today)

btn_back = Button(cw,text="Back",font=ft,command=f2,bg="light green")
btn_back.place(x=200,y=230)

cw.withdraw()

def on_closing():
	if askokcancel("Quit","Are You Sure?"):
		mw.destroy()

cw.protocol("WM_DELETE_WINDOW", on_closing)
mw.protocol("WM_DELETE_WINDOW", on_closing)

t()


#Countdown


def Start_Timer():
    try:
        times = int(float(hours.get())) * 3600 + int(float(minutes.get())) * 60 + int(float(seconds.get()))

        while times > -1:
            minute, second = (times // 60, times % 60)

            hour = 0
            if minute > 60:
                hour, minute = (minute // 60, minute % 60)

            seconds.set(second)
            minutes.set(minute)
            hours.set(hour)

            ct.update()
            time.sleep(1)
            times -= 1
        showinfo("Countdown Timer", "Time is up!")
    except Exception as e:
        showerror("ERROR","INVALID INPUT")
        
       
        

hours=StringVar()
minutes=StringVar()
seconds=StringVar()

ct = Toplevel(mw)
ct.title("Coutdown Timer")
ct.iconbitmap("d.ico")
ct.geometry("500x330+100+100")
ct.configure(bg="black")



lbl_hr = Label(ct,text="Hr",font=ft)
lbl_hr.place(x=130,y=20)
ent_hr= Entry(ct, width=3, font=ft,textvariable=hours)
ent_hr.place(x=80,y=20)
hours.set("00")


lbl_mt = Label(ct,text="Mt",font=ft)
lbl_mt.place(x=220,y=20)
ent_mt= Entry(ct, width=3, font=ft,textvariable=minutes)
ent_mt.place(x=170,y=20)
minutes.set("00")

lbl_sc = Label(ct,text="Sc",font=ft)
lbl_sc.place(x=310,y=20)
ent_sc= Entry(ct, width=3, font=ft,textvariable=seconds)
ent_sc.place(x=260,y=20)
seconds.set("00")

btn_st = Button(ct,text="start",font=ft,command=Start_Timer)
btn_st.place(x=80,y=100)

btn_b = Button(ct,text="back",font=ft,command=f4)
btn_b.place(x=280,y=100)
ct.withdraw()

ct.protocol("WM_DELETE_WINDOW", on_closing)


#Stopwatch

class Stopwatch:
    def __init__(self, parent):
        self.parent = parent
        self.is_running = False
        self.elapsed_time = 0

        self.time_label = Label(parent, font=("Times New Roman", 48), bg="black", fg="white", text="00:00:00")
        self.time_label.pack(pady=20)

        self.start_button = Button(parent, text="Start", command=self.start_stopwatch)
        self.start_button.pack()

        self.reset_button = Button(parent, text="Reset", command=self.reset_stopwatch)
        self.reset_button.pack()

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(text="Stop")
            self.update_stopwatch()

    def update_stopwatch(self):
        if self.is_running:
            self.elapsed_time += 1
            minutes, seconds = divmod(self.elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)
            time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.time_label.config(text=time_string)
            self.parent.after(1000, self.update_stopwatch)

    def reset_stopwatch(self):
        self.is_running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")
        self.start_button.config(text="Start")
stopwatch_frame = Toplevel(mw)
stopwatch_frame.geometry("300x300")
stopwatch_frame.iconbitmap("c.ico")
stopwatch_frame.title("Stopwatch")
stopwatch = Stopwatch(stopwatch_frame)
stopwatch_frame.configure(bg="black")
Bk = Button(stopwatch_frame,text="Back",command=f10)
Bk.pack(pady=3)

stopwatch_frame.withdraw()
stopwatch_frame.protocol("WM_DELETE_WINDOW", on_closing)
btn_stopwatch = Button(mw,text = "Stopwatch",font=ft,bg="yellow", command=f9)
btn_stopwatch.place(x=650,y=240)


#Alarm


#Importing all the necessary libraries to form the alarm clock

class Alarm:
    def __init__(self, parent):
        self.parent = parent

        self.alarm_label = Label(parent, font=("Arial", 24), bg="black", fg="white", text="Set the alarm time:")
        self.alarm_label.pack(pady=10)

        self.alarm_entry = Entry(parent, font=("Arial", 24))
        self.alarm_entry.pack(pady=10)

        self.set_alarm_button = Button(parent, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)

    def set_alarm(self):
        alarm_time = self.alarm_entry.get()
        if self.validate_alarm_time(alarm_time):
            self.alarm_label.config(text=f"Alarm set for: {alarm_time}")
            threading.Thread(target=self.check_alarm, args=(alarm_time,)).start()

    def validate_alarm_time(self, alarm_time):
        try:
            time.strptime(alarm_time, "%H:%M:%S")
            return True
        except ValueError:
            showerror("Invalid Time", "Please enter a valid time in HH:MM:SS format.")
            return False

    def check_alarm(self, alarm_time):
        while True:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                showinfo("Alarm", "Wake up!")
                break
alarm_frame = Toplevel(mw)
alarm_frame.geometry("350x350")
alarm_frame.iconbitmap("c.ico")
alarm_frame.title("Alarm")
alarm = Alarm(alarm_frame)
alarm_frame.configure(bg="black")
R = Button(alarm_frame,text="Back",command=f6)
R.place(x=158,y=170)

alarm_frame.withdraw()
alarm_frame.protocol("WM_DELETE_WINDOW", on_closing)

class WorldClock:
    
    def __init__(self, parent):
        self.parent = parent

        self.city_label = Label(parent, text="Select a city:")
        self.city_label.pack(pady=10)

        self.selected_city = StringVar()
        self.selected_city.set("GMT")

        self.city_radio1 = Radiobutton(parent, text="GMT", variable=self.selected_city, value="GMT")
        self.city_radio1.pack()

        self.city_radio2 = Radiobutton(parent, text="New York", variable=self.selected_city, value="New York")
        self.city_radio2.pack()

        self.city_radio3 = Radiobutton(parent, text="Tokyo", variable=self.selected_city, value="Tokyo")
        self.city_radio3.pack()

        self.city_label = Label(parent, text="Current time in selected city:")
        self.city_label.pack(pady=10)

        self.time_label = Label(parent, font=("Arial", 48), bg="black", fg="white")
        self.time_label.pack(pady=20)

        self.update_time()

    def update_time(self):
        selected_city = self.selected_city.get()
        if selected_city == "GMT":
            current_time = time.strftime("%H:%M:%S")
        elif selected_city == "New York":
            current_time = time.strftime("%H:%M:%S", time.gmtime(time.time() - 4 * 3600))
        elif selected_city == "Tokyo":
            current_time = time.strftime("%H:%M:%S", time.gmtime(time.time() + 9 * 3600))
        else:
            current_time = ""
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_time)
world_clock_frame = Toplevel(mw)
world_clock_frame.geometry("400x400")
world_clock_frame.iconbitmap("c.ico")
world_clock_frame.configure(bg="black")
world_clock_frame.title("World Clock")
world_clock = WorldClock(world_clock_frame)
Bak = Button(world_clock_frame,text="Back",font=("Arial", 35),command=f8)
Bak.pack(pady=30)

world_clock_frame.withdraw()
world_clock_frame.protocol("WM_DELETE_WINDOW", on_closing)

btn_WC = Button(mw,text = "World Clock",font=ft,bg="yellow",command=f7)
btn_WC.place(x=400,y=330)



mw.mainloop()