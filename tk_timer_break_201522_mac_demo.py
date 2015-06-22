# -*- coding: utf-8 -*-
# for python 3.x use 'tkinter' rather than 'Tkinter'
#
BREAK_SECOND=10   		#take some secore break
BREAK_INTERVEL_MINUTES=20   #after how many minutes 


import Tkinter as tk
import time
from  datetime import datetime


MAX_ALPHA=1.0
ALPHA_STEP=MAX_ALPHA /(BREAK_SECOND*1000 /10) # 1000 is covert to msecond, 10 is .after(10) event
#!env python
class TakeBreakWindowApp():
    def __init__(self):
        self.start_time=datetime.now()

        self.tk = tk.Tk()
        self.top= FadeToplevel(self.tk)
        self.top = self.tk
                
        self.label0 = tk.Label(text="Please Take Break", font=("Helvetica", 14))
        self.label0.pack()
        self.label = tk.Label(text="", font=("Helvetica", 24))
        self.label.pack()
        self.update_clock()
        self.top.mainloop()

    def update_clock(self):
        now=datetime.now() - self.start_time
        run_seconds=BREAK_SECOND-now.seconds
        # time.strftime("%H:%M:%S")
        if (run_seconds)<0: run_seconds=0

        nowStr = "Relax for "+str(run_seconds) +"s"
        self.label.configure(text=nowStr)
        self.top.after(1000, self.update_clock)
        if (now.seconds >BREAK_SECOND): #Let windows exists more seconds after full alphaed
        	self.top.destroy()
        	self.top.quit()
        
    def fading_window(self):
        self.count += 1
        t=FadeToplevel(self.top)
        t.wm_title("Window %s" % self.count)
        #t.fade_in()
        
class FadeToplevel(tk.Toplevel):
    '''A toplevel widget with the ability to fade in'''
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.attributes("-alpha", 0.0)
        self.quitButton = tk.Button(self, text='休息一下，点我没用', 
        	width=1, font=("Helvetica", 16),
        	#command=self.quit)
			#command=self.destroy
			)
        self.quitButton.pack(side="top", fill='both', expand=False, padx=700, pady=300)
        #First two numbers represent dimensions of window. Third and fourth number say, where the window will appear.
        self.geometry("%dx%d%+d%+d" % (1920, 1080, 0, 0))
        self.fade_in()
        # self.mainloop()

    def fade_in(self):
        max_alpha=MAX_ALPHA
        duration=10  #time to wait
        #step=max_alpha/(duration*1000/100)  #0.1
        step=0.0005
        alpha = self.attributes("-alpha")
        alpha = min(alpha + ALPHA_STEP, max_alpha)
        self.attributes("-alpha", alpha)
        if alpha < max_alpha:
            self.after(10, self.fade_in)


if __name__ == '__main__':
	curTime=datetime.now()
	# while True:
	while True:
		print "break time:" + curTime.ctime()
		workingTime=datetime.now()
		app=TakeBreakWindowApp()
		# app=FadeToplevel(tk.Tk())
		time.sleep(BREAK_INTERVEL_MINUTES*60)