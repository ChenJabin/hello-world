from tkinter import *
from tkinter import ttk
# OptionMenu repalce menubutton

class mainApp(Tk):
    def __init__(self):
        super().__init__()
        instFrame(self).pack(fill=X, expand=TRUE)
        measFrame(self).pack(fill=BOTH, expand=TRUE)
        # menu
        # tatusbar.pack(side="bottom", fill="x")
        # toolbar.pack(side="top", fill="x")
        # navbar.pack(side="left", fill="y")
        # main.pack(side="right", fill="both", expand=True)

class instFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        instCtrlFrame = ttk.Frame(self)
        instListFrame = ttk.Frame(self)

class measFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)



def GUI():
    app = mainApp()
    app.title('RadioKits')
    app.geometry('1080x720')
    app.minsize(width=960, height=540)
    app.iconbitmap(PhotoImage('ericsson.ico'))
    app.mainloop()

if __name__ == '__main__':
    GUI()
