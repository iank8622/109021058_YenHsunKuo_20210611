from tkinter import *

def setLabText(text):
    print(text)

screen = Tk()
screen.geometry("400x400+200+200")
screen.title("Calculation")

for row in range(4):
    screen.rowconfigure(row, weight = 1) # 第row行設定 權重
for column in range(4):
    screen.columnconfigure(column, weight = 1) # 第column行設定 權重

#lab = Label(screen, text = "", height = 3, bg = "#ffc472")
#lab.grid(row = 4 , column = 0, sticky = NSEW)

btn7 = Button(screen, text = 7, command = lambda:setLabText(7)) # lambda: 可在函式內代入參數
btn7.grid(row = 0 , column = 0, sticky = NSEW)
btn8 = Button(screen, text = 8, command = lambda:setLabText(8))
btn8.grid(row = 0 , column = 1, sticky = NSEW)
btn9 = Button(screen, text = 9, command = lambda:setLabText(9))
btn9.grid(row = 0 , column = 2, sticky = NSEW)
btn_div = Button(screen, text = '/', command = lambda:setLabText('/'))
btn_div.grid(row = 0 , column = 3, sticky = NSEW)

btn4 = Button(screen, text = 4, command = lambda:setLabText(4))
btn4.grid(row = 1 , column = 0, sticky = NSEW)
btn5 = Button(screen, text = 5, command = lambda:setLabText(5))
btn5.grid(row = 1 , column = 1, sticky = NSEW)
btn6 = Button(screen, text = 6, command = lambda:setLabText(6))
btn6.grid(row = 1 , column = 2, sticky = NSEW)
btn_mul = Button(screen, text = 'x', command = lambda:setLabText('x'))
btn_mul.grid(row = 1 , column = 3, sticky = NSEW)

btn1 = Button(screen, text = 1, command = lambda:setLabText(1)) # lambda: 可在函式內代入參數
btn1.grid(row = 2 , column = 0, sticky = NSEW)
btn2 = Button(screen, text = 2, command = lambda:setLabText(2))
btn2.grid(row = 2 , column = 1, sticky = NSEW)
btn3 = Button(screen, text = 3, command = lambda:setLabText(3))
btn3.grid(row = 2 , column = 2, sticky = NSEW)
btn_sub = Button(screen, text = '-', command = lambda:setLabText('-'))
btn_sub.grid(row = 2 , column = 3, sticky = NSEW)

btn0 = Button(screen, text = 0, command = lambda:setLabText(0))
btn0.grid(row = 3 , column = 0, sticky = NSEW)
btn_dec = Button(screen, text = '.', command = lambda:setLabText('.'))
btn_dec.grid(row = 3 , column = 1, sticky = NSEW)
btn_amount = Button(screen, text = '=', command = lambda:setLabText('='))
btn_amount.grid(row = 3 , column = 2, sticky = NSEW)
btn_add = Button(screen, text = '+', command = lambda:setLabText('+'))
btn_add.grid(row = 3 , column = 3, sticky = NSEW)

screen.mainloop()

