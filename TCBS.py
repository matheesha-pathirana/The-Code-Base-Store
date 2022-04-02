import tkinter as tk
import tkinter.font as tkFont
import webbrowser
import tkinter as tk
import tkinter.font as tkFont
import webbrowser
import os
import random
import string
import subprocess
import tkinter as tk
import tkinter.font as tkFont
import git


class App:
    def __init__(self, root):
        #setting title
        root.title("The Code Base Store App")
        #setting window size
        width=1515
        height=892
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
        GLabel_256["text"] = "The Code Base Store App"
        GLabel_256.place(x=50,y=10,width=686,height=76)

        GButton_519=tk.Button(root)
        GButton_519["bg"] = "#333333"
        ft = tkFont.Font(family='Segoe UI',size=18)
        GButton_519["font"] = ft
        GButton_519["fg"] = "#e9e9ed"
        GButton_519["justify"] = "center"
        GButton_519["text"] = "Settings"
        GButton_519.place(x=1360,y=20,width=110,height=40)
        GButton_519["command"] = self.GButton_519_command

        GButton_48=tk.Button(root)
        GButton_48["bg"] = "#333333"
        ft = tkFont.Font(family='Segoe UI',size=18)
        GButton_48["font"] = ft
        GButton_48["fg"] = "#e9e9ed"
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
        GButton_820["bg"] = "#333333"
        ft = tkFont.Font(family='Segoe UI',size=24)
        GButton_820["font"] = ft
        GButton_820["fg"] = "#e9e9ed"
        GButton_820["justify"] = "center"
        GButton_820["text"] = "Cryptical Software"
        GButton_820.place(x=20,y=190,width=338,height=98)
        GButton_820["command"] = self.GButton_820_command

        GButton_621=tk.Button(root)
        GButton_621["bg"] = "#333333"
        ft = tkFont.Font(family='Segoe UI',size=18)
        GButton_621["font"] = ft
        GButton_621["fg"] = "#e9e9ed"
        GButton_621["justify"] = "center"
        GButton_621["text"] = "Join Our Discord"
        GButton_621.place(x=20,y=810,width=253,height=52)
        GButton_621["command"] = self.GButton_621_command

        GButton_538=tk.Button(root)
        GButton_538["bg"] = "#333333"
        ft = tkFont.Font(family='Segoe UI',size=18)
        GButton_538["font"] = ft
        GButton_538["fg"] = "#e9e9ed"
        GButton_538["justify"] = "center"
        GButton_538["text"] = "Exit"
        GButton_538.place(x=1380,y=820,width=110,height=42)
        GButton_538["command"] = self.GButton_538_command

    def GButton_519_command(self):
        print("command")


    def GButton_48_command(self):
        print("command")


    def GButton_820_command(self):
        def tcbs_installer():
            if os.path.exists("D:/The Code Base App Data/Utility-Software/main.py"):
                import tkinter as tk
                import tkinter.font as tkFont

                class App:
                    def __init__(self, root):
                        # setting title
                        root.title("Cryptical Software")
                        # setting window size
                        width = 628
                        height = 297
                        screenwidth = root.winfo_screenwidth()
                        screenheight = root.winfo_screenheight()
                        alignstr = '%dx%d+%d+%d' % (
                        width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                        root.geometry(alignstr)
                        root.resizable(width=False, height=False)

                        GLabel_926 = tk.Label(root)
                        ft = tkFont.Font(family='Segoe UI', size=20)
                        GLabel_926["font"] = ft
                        GLabel_926["fg"] = "#333333"
                        GLabel_926["justify"] = "center"
                        GLabel_926["text"] = "Cryptical Software Already Installed To This Computer"
                        GLabel_926.place(x=0, y=30, width=617, height=30)

                        GButton_942 = tk.Button(root)
                        GButton_942["bg"] = "#333333"
                        ft = tkFont.Font(family='Segoe UI', size=28)
                        GButton_942["font"] = ft
                        GButton_942["fg"] = "#e9e9ed"
                        GButton_942["justify"] = "center"
                        GButton_942["text"] = "Ok, Close"
                        GButton_942.place(x=330, y=160, width=200, height=60)
                        GButton_942["command"] = self.GButton_942_command

                        GButton_237 = tk.Button(root)
                        GButton_237["bg"] = "#333333"
                        ft = tkFont.Font(family='Segoe UI', size=28)
                        GButton_237["font"] = ft
                        GButton_237["fg"] = "#e9e9ed"
                        GButton_237["justify"] = "center"
                        GButton_237["text"] = "Launch"
                        GButton_237.place(x=80, y=160, width=200, height=60)
                        GButton_237["command"] = self.GButton_237_command

                    def GButton_942_command(self):
                        exit()

                    def GButton_237_command(self):
                        exec(open("D:/The Code Base App Data/Utility-Software/main.py").read())
                        exit()


                if __name__ == "__main__":
                    root = tk.Tk()
                    app = App(root)
                    root.mainloop()
            else:
                main_dir = 'D:/The Code Base App Data'
                os.mkdir(main_dir)
                git.Git(main_dir).clone("https://github.com/matheesha-pathirana/Utility-Software.git")

                import tkinter as tk
                import tkinter.font as tkFont
                import subprocess
                class App:
                    def __init__(self, root):
                        # setting title
                        root.title("Installed Successfully!")
                        # setting window size
                        width = 500
                        height = 297
                        screenwidth = root.winfo_screenwidth()
                        screenheight = root.winfo_screenheight()
                        alignstr = '%dx%d+%d+%d' % (
                        width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                        root.geometry(alignstr)
                        root.resizable(width=False, height=False)

                        GLabel_472 = tk.Label(root)
                        ft = tkFont.Font(family='Segoe UI', size=18)
                        GLabel_472["font"] = ft
                        GLabel_472["fg"] = "#333333"
                        GLabel_472["justify"] = "center"
                        GLabel_472["text"] = "Cryptical Software Installed Successfully !"
                        GLabel_472.place(x=10, y=20, width=481, height=56)

                        GButton_139 = tk.Button(root)
                        GButton_139["bg"] = "#333333"
                        ft = tkFont.Font(family='Segoe UI', size=18)
                        GButton_139["font"] = ft
                        GButton_139["fg"] = "#e9e9ed"
                        GButton_139["justify"] = "center"
                        GButton_139["text"] = "Launch"
                        GButton_139.place(x=70, y=180, width=150, height=50)
                        GButton_139["command"] = self.GButton_139_command

                        GButton_980 = tk.Button(root)
                        GButton_980["bg"] = "#333333"
                        ft = tkFont.Font(family='Segoe UI', size=18)
                        GButton_980["font"] = ft
                        GButton_980["fg"] = "#e9e9ed"
                        GButton_980["justify"] = "center"
                        GButton_980["text"] = "Exit"
                        GButton_980.place(x=270, y=180, width=150, height=50)
                        GButton_980["command"] = self.GButton_980_command

                    def GButton_139_command(self):
                        exec(open(
                            "D:/The Code Base App Data/Utility-Software/main.py").read())
                        exit()

                    def GButton_980_command(self):
                        exit()

                if __name__ == "__main__":
                    root = tk.Tk()
                    app = App(root)
                    root.mainloop()

        tcbs_installer()
    def GButton_621_command(self):
        webbrowser.open('https://discord.gg/pkf2Hzxa9y')


    def GButton_538_command(self):
        exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
