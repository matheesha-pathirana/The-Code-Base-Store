import tkinter as tk
import tkinter.font as tkFont
import git

class App:
    def __init__(self, root):
        #setting title
        root.title("The Code Base Store")
        #setting window size
        width=1511
        height=814
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_256=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI',size=28)
        GLabel_256["font"] = ft
        GLabel_256["fg"] = "#333333"
        GLabel_256["justify"] = "left"
        GLabel_256["text"] = "The Code Base Store"
        GLabel_256.place(x=50,y=10,width=686,height=76)

        GButton_519=tk.Button(root)
        GButton_519["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Segoe UI',size=18)
        GButton_519["font"] = ft
        GButton_519["fg"] = "#000000"
        GButton_519["justify"] = "center"
        GButton_519["text"] = "Settings"
        GButton_519.place(x=1360,y=20,width=110,height=40)
        GButton_519["command"] = self.GButton_519_command

        GButton_48=tk.Button(root)
        GButton_48["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Segoe UI',size=18)
        GButton_48["font"] = ft
        GButton_48["fg"] = "#000000"
        GButton_48["justify"] = "center"
        GButton_48["text"] = "Account"
        GButton_48.place(x=1230,y=20,width=110,height=40)
        GButton_48["command"] = self.GButton_48_command

        GLabel_897=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI',size=18)
        GLabel_897["font"] = ft
        GLabel_897["fg"] = "#333333"
        GLabel_897["justify"] = "center"
        GLabel_897["text"] = "Latest Softwares"
        GLabel_897.place(x=0,y=120,width=392,height=49)

        GButton_820=tk.Button(root)
        GButton_820["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Segoe UI',size=24)
        GButton_820["font"] = ft
        GButton_820["fg"] = "#000000"
        GButton_820["justify"] = "center"
        GButton_820["text"] = "Cryptical Software"
        GButton_820.place(x=20,y=190,width=338,height=98)
        GButton_820["command"] = self.GButton_820_command

    def GButton_519_command(self):
        print("command")


    def GButton_48_command(self):
        print("command")


    def GButton_820_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
