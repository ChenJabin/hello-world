from tkinter import *
from tkinter import ttk, filedialog

# OptionMenu repalce menubutton

class mainApp(Tk):
    def __init__(self):
        super().__init__()
        menubar = menuBar(self)
        statbar = statBar(self)
        instframe = instFrame(self)
        naviframe = naviFrame(self)
        ctrlframe = ctrlFrame(self)
        mainframe = mainFrame(self)

        self.config(menu=menubar)
        statbar.pack(fill=X, side=BOTTOM)
        instframe.pack(fill=X, side=TOP)
        naviframe.pack(fill=Y, side=LEFT)
        ctrlframe.pack(fill=X, side=BOTTOM)
        mainframe.pack(fill=BOTH, expand=TRUE)

class menuBar(Menu):
    def __init__(self, master):
        super().__init__(master)
        # master.config(menu=self)
        fileMenu = Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label='Open', command=filedialog.askopenfilename)
        fileMenu.add_command(label='Open...', command=filedialog.askdirectory)
        fileMenu.add_command(label='Save', command=filedialog.asksaveasfilename)
        fileMenu.add_command(label='Exit', command=master.destroy)

        helpMenu = Menu(self, tearoff=0)
        self.add_cascade(label='Help', menu=helpMenu)

class statBar(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Style().configure('statBar.TFrame', background='#007ACC')
        self['style'] = 'statBar.TFrame'

class instFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Style().configure('instFrame.TFrame', background='#7F7F7F')
        self['style'] = 'instFrame.TFrame'

        instCtrlFrame = ttk.Frame(self, style='instFrame.TFrame', padding=(10,10,10,10))
        instListFrame = ttk.Frame(self, style='instFrame.TFrame', padding=(10,0,10,10))

        instCtrlFrame.pack(fill=X)
        instListFrame.pack(fill=X)

        ttk.Style().configure('TButton', width = 20)
        ttk.Button(instCtrlFrame, text='Select Platform').pack(side=LEFT)
        ttk.Button(instCtrlFrame, text='Show Full Overview').pack(side=LEFT, padx=10)
        ttk.Button(instCtrlFrame, text='Reload Address', command=instListFrame.pack).pack(side=RIGHT,)
        ttk.Button(instCtrlFrame, text='Hide Instrument', command=instListFrame.pack_forget).pack(side=RIGHT, padx=10)

        Label(instListFrame, text='t').grid()
class naviFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text='t').grid()
        ttk.Style().configure('naviFrame.TFrame', background='red')
        self['style'] = 'naviFrame.TFrame'

class ctrlFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text='t').grid()
        ttk.Style().configure('ctrlFrame.TFrame', background='blue')
        self['style'] = 'ctrlFrame.TFrame'

class mainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text='t').grid()
        ttk.Style().configure('mainFrame.TFrame', background='white')
        self['style'] = 'mainFrame.TFrame'



def GUI():
    app = mainApp()
    app.title('RadioKits')
    app.geometry('1080x720')
    app.minsize(width=960, height=540)
    app.iconbitmap(PhotoImage('ericsson.ico'))
    # app.update()
    app.mainloop()

if __name__ == '__main__':
    GUI()
