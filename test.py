import tkinter as tk

windows = tk.Tk()
label_list = []



for i in range(0, 5, 1):
    label_list.append(tk.Label(windows, text = "Text"))
    label_list[i].pack()



def delLabel():

    label_list[1].forget()
    print(label_list)


tk.Button(windows, text="DelLabel", command=delLabel).pack()

windows.mainloop()
