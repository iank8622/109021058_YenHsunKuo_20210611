from tkinter import *



def setBtnText(num):
    global flag

    if flag:
        btnList[num].config(text = "O", state = DISABLED)
    else:
        btnList[num].config(text = "X", state = DISABLED)

    flag = not flag

    reFlag = False
    if btnList[0].cget("text") != "" and btnList[0].cget("text") == btnList[1].cget("text") == btnList[2].cget("text"):
        print(btnList[0].cget("text") + " win!!!")
        reFlag = not reFlag
    elif btnList[3].cget("text") != "" and btnList[3].cget("text") == btnList[4].cget("text") == btnList[5].cget("text"):
        print(btnList[3].cget("text") + " win!!!")
        reFlag = not reFlag
    elif btnList[6].cget("text") != "" and btnList[6].cget("text") == btnList[7].cget("text") == btnList[8].cget("text"):
        print(btnList[6].cget("text") + " win!!!")
        reFlag = not reFlag
    elif btnList[0].cget("text") != "" and btnList[0].cget("text") == btnList[3].cget("text") == btnList[6].cget("text"):
        print(btnList[0].cget("text") + " win!!!")
        reFlag = not reFlag
    elif btnList[1].cget("text") != "" and btnList[1].cget("text") == btnList[4].cget("text") == btnList[7].cget("text"):
        print(btnList[1].cget("text") + " win!!!")
        reFlag = not reFlag
    elif btnList[2].cget("text") != "" and btnList[2].cget("text") == btnList[5].cget("text") == btnList[8].cget("text"):
        print(btnList[2].cget("text") + " win!!!")
        reFlag = not reFlag
    elif btnList[0].cget("text") != "" and btnList[0].cget("text") == btnList[4].cget("text") == btnList[8].cget("text"):
        print(btnList[0].cget("text") + " win!!!")
        reFlag = not reFlag
    elif btnList[2].cget("text") != "" and btnList[2].cget("text") == btnList[4].cget("text") == btnList[6].cget("text"):
        print(btnList[2].cget("text") + " win!!!")
        reFlag = not reFlag
    elif btnList[0].cget("text") != "" and btnList[1].cget("text") != "" and btnList[2].cget("text") != "" and btnList[3].cget("text") != "" and btnList[4].cget("text") != "" and btnList[5].cget("text") != "" and btnList[6].cget("text") != "" and btnList[7].cget("text") != "" and btnList[8].cget("text") != "":
        print("Draw!!!")
        reFlag = not reFlag


    if reFlag:
        for btn in btnList:
            btn.config(text = "", state = NORMAL)
        reFlag = not reFlag



screen = Tk()
screen.geometry("400x400+200+200")
screen.title = "Button Test"

for row in range(3):
    screen.rowconfigure(row, weight = 1) # 第row行設定 權重
for column in range(3):
    screen.columnconfigure(column, weight = 1) # 第column行設定 權重


btnList = []
flag = True
for row in range(3):
    for column in range(3):
        btn = Button(screen, text = "", command = lambda:setBtnText()) # lambda: 可在函式內代入參數
        btn.grid(row = row , column = column, sticky = NSEW) # 以網格概念放置 需先設定rowconfigure 和 columnconfigure 後使用sticky 以NS EW放大
        btnList.append(btn)

btnList[0].config(command = lambda:setBtnText(0))
btnList[1].config(command = lambda:setBtnText(1))
btnList[2].config(command = lambda:setBtnText(2))
btnList[3].config(command = lambda:setBtnText(3))
btnList[4].config(command = lambda:setBtnText(4))
btnList[5].config(command = lambda:setBtnText(5))
btnList[6].config(command = lambda:setBtnText(6))
btnList[7].config(command = lambda:setBtnText(7))
btnList[8].config(command = lambda:setBtnText(8))

screen.mainloop()