import tkinter as tk


windows = tk.Tk()
windows.title("My_Label_Test")
windows.geometry("800x800")


placeX_Start = 20
placeX_End = 740
placeX_Range = 80
palceY_Start = 20
placeY_End = 200
placeY_Range = 20

labelText = []



# 製作99乘法表資料 並放入陣列中 格式為tk.Label
for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        labelText.append(tk.Label(windows, text=" " + str(i) + " x " + str(j) + " = " + str(i * j) + " "))
        labelText[i-1].pack()


def labelForget():
    for i in range(0, 10, 1):
        labelText[i].forget()


buttonTestForget = tk.Button(windows, text="buttonForget", command=labelForget).place(x=400, y=400)


windows.mainloop()
