import tkinter as tk
from time import strftime
import tkinter.font as tkfont
# making object of root tk.Tk
root=tk.Tk()
root.title("Digital clock")

clock_font = tkfont.Font(
    family="cliberi",   # change to DS-Digital / Orbitron if installed
    size=90,
    weight="bold"
)

# function for time to root
def time():
    string=strftime("%H : %M:%S %p \n %D")
    label.config(text=string)
    label.after(1000,time)
# making object for label
label=tk.Label(root,font=(clock_font),background='black',foreground='blue')
label.pack(anchor="center")
# call function 
time()
# open loop of root
root.mainloop()