import tkinter as tk

class PopOut(tk.Toplevel):
    def __init__(self, master, **kwargs):
        tk.Toplevel.__init__(self, master, **kwargs)
        
        #Getting screen resolution
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()  
        #Getting window size and putting it in the center
        size = tuple(int(_) for _ in self.geometry().split('+')[0].split('x'))
        x = screen_width/2 - size[0]/2
        y = screen_height/2 - size[1]/2
        self.geometry("+%d+%d" % (x, y))
        
        #set focus to this window
        self.focus_set()

class Warning(PopOut, object):
    def __init__(self, master, msg):
        super(Warning, self).__init__(master)
        #set focus to this window
        self.focus_set()
        #disable the main window
        master.attributes('-disabled', True)
        #capture close event
        self.protocol("WM_DELETE_WINDOW", self.close)
        #Content and message
        label = tk.Label(self, text=msg)
        label.pack(side="top", fill="x", padx=5, pady=5)
        B1 = tk.Button(self, text="Okay", command = self.close)
        B1.pack(pady=5)
        
    def close(self, event=None):
        #re-enable the main window
        self.master.attributes('-disabled', False)
        #destroy this window
        self.destroy()