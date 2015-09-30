# Import statements
from tkinter import *
    
# Class definition
class EntryDisplay:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.minsize(500,300)
        self.top_frame = Frame(self.main_window)
        self.second_frame = Frame(self.main_window)
        self.third_frame = Frame(self.main_window)
        self.fourth_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)

        self.ready = False

# Altitude Input
        self.altitude_prompt = Label(self.top_frame, text='Altitude (km):') #prompt init
        self.altitude_entry = Entry(self.top_frame,width=10)                #entry window init
        self.altitude_entry.insert(0, "500")                                #default value
        self.altitude_prompt.pack(side='left')                              #pack prompt
        self.altitude_entry.pack(side='left')                               #pack entry window

# Equations of Motion (acceleration) Inputs
        self.fx_prompt = Label(self.second_frame, text='F(x):')
        self.fx_entry = Entry(self.second_frame,width=10)
        self.fx_entry.insert(0, "0")
        self.fx_prompt.pack(side='left')
        self.fx_entry.pack(side='left')

        self.fy_prompt = Label(self.third_frame, text='F(y):')
        self.fy_entry = Entry(self.third_frame,width=10)
        self.fy_entry.insert(0, "0")
        self.fy_prompt.pack(side='left')
        self.fy_entry.pack(side='left')

        self.fz_prompt = Label(self.fourth_frame, text='F(z):')
        self.fz_entry = Entry(self.fourth_frame,width=10)
        self.fz_entry.insert(0, "0")
        self.fz_prompt.pack(side='left')
        self.fz_entry.pack(side='left')

# Velocity Equations Inputs
        self.xd_prompt = Label(self.second_frame, text='xd(0):')
        self.xd_entry = Entry(self.second_frame,width=10)
        self.xd_entry.insert(0, "0")
        self.xd_prompt.pack(side='left')
        self.xd_entry.pack(side='left')

        self.yd_prompt = Label(self.third_frame, text='yd(0):')
        self.yd_entry = Entry(self.third_frame,width=10)
        self.yd_entry.insert(0, "0")
        self.yd_prompt.pack(side='left')
        self.yd_entry.pack(side='left')

        self.zd_prompt = Label(self.fourth_frame, text='zd(0):')
        self.zd_entry = Entry(self.fourth_frame,width=10)
        self.zd_entry.insert(0, "0")
        self.zd_prompt.pack(side='left')
        self.zd_entry.pack(side='left')

# Position Equations Inputs
        self.x_prompt = Label(self.second_frame, text='x(0):')
        self.x_entry = Entry(self.second_frame,width=10)
        self.x_entry.insert(0, "0")
        self.x_prompt.pack(side='left')
        self.x_entry.pack(side='left')

        self.y_prompt = Label(self.third_frame, text='y(0):')
        self.y_entry = Entry(self.third_frame,width=10)
        self.y_entry.insert(0, "0")
        self.y_prompt.pack(side='left')
        self.y_entry.pack(side='left')

        self.z_prompt = Label(self.fourth_frame, text='z(0):')
        self.z_entry = Entry(self.fourth_frame,width=10)
        self.z_entry.insert(0, "0")
        self.z_prompt.pack(side='left')
        self.z_entry.pack(side='left')

# Buttons
        self.calc_button = Button(self.bottom_frame, text='Run', command=self.readyToCalculate)
        self.quit_button = Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

# Pack frames
        self.calc_button.pack()
        self.quit_button.pack()
        self.top_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()
        self.bottom_frame.pack()

# Mainloop
        self.main_window.mainloop()

    def readyToCalculate(self):
        self.altitude = self.altitude_entry.get()
        self.fx = self.fx_entry.get()
        self.fy = self.fy_entry.get()
        self.fz = self.fz_entry.get()
        self.xd = self.xd_entry.get()
        self.yd = self.yd_entry.get()
        self.zd = self.zd_entry.get()
        self.x  = self.x_entry.get()
        self.y  = self.y_entry.get()
        self.z  = self.z_entry.get()
        
        self.ready = True
        self.main_window.destroy()

    def getValues(self):
        return (self.altitude, self.fx, self.fy, self.fz,
                self.xd, self.yd, self.zd, self.x, self.y, self.z)

 

