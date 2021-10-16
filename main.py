import tkinter as tk


windows = tk.Tk()
windows.title("My_Label_Test")
windows.geometry("800x800")


column = 10
row = 9
rangeTempNumber = 1
arrayStar = 0
arrayEnd = 10

rangeNumber = 0
placeX = 20
placeY = 20

labelRangeStar = 20
labelRangeEnd = 200
labelRangeTemp = 20


demoLabelText = []

#製作99乘法表資料 並放入陣列中
for i in range(1, 10, 1):
    for j in range(1, 10, 1):

        demoLabelText.append(" " + str(i) + " x " + str(j) + " = " + str(i * j) + " ")

for i, j in zip(demoLabelText[0:9], range(200, 600, 20)):
    tk.Label(windows, text=i).place(x=20, y=j)

for i in demoLabelText:
    tk.Label(windows, text=i).pack()




# for i, j in zip(range(arrayStar, arrayEnd, rangeTempNumber), range(labelRangeStar, labelRangeEnd, labelRangeTemp)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=placeX, y=j)
#
# for i, j in zip(range(9, 19, 1),range(20, 200, 20)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=100, y=j)
#
# for i, j in zip(range(18, 28, 1),range(20, 200, 20)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=180, y=j)
#
# for i, j in zip(range(27, 37, 1), range(20, 200, 20)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=260, y=j)
#
# for i, j in zip(range(36, 46, 1), range(20, 200, 20)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=340, y=j)
#
# for i, j in zip(range(45, 55, 1), range(20, 200, 20)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=420, y=j)
#
# for i, j in zip(range(54, 64, 1), range(20, 200, 20)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=500, y=j)
#
# for i, j in zip(range(63, 73, 1), range(20, 200, 20)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=580, y=j)
#
# for i, j in zip(range(72, 81, 1), range(20, 200, 20)):
#     tk.Label(windows, text=demoLabelText[i]).place(x=660, y=j)


windows.mainloop()