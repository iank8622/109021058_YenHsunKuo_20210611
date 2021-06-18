from tkinter import *
import hashlib # 雜湊值 類似亂碼 加密用


account = dict()
s256 = hashlib.sha256()
s1 = hashlib.sha1()
m5 = hashlib.md5()

hashCode = {"03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4": "1234",
            "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8": "password",
            "bef57ec7f53a6d40beb640a780a639c83bc29ac8a9816f1fc6c5c6dcd93c4721": "abcdef",
            "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5": "qwerty",
            "5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456": "h3041723"}

def login():
    idData = entryID.get()
    pwData = entryPW.get()
    if len(idData) > 0 and len(pwData):
        # Q1
        idHash = hashlib.sha256(idData.encode("utf-8")).hexdigest()
        pwHash = hashlib.sha256(pwData.encode("utf-8")).hexdigest()
        if idHash == "207a0fd942624d8c7d26cb85594480f37840acfbf399f6cdc3724774ba9f1931" and pwHash == "5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":
            root.deiconify() # 顯示其視窗
            loginScreen.destroy() # 銷毀
            registScreen.destroy()
            labPrompt.config(text = "請輸入帳號與密碼。")
        else:
            # 註冊登入
            if account[idHash] == pwHash:
                root.deiconify() # 顯示其視窗
                loginScreen.destroy() # 銷毀
                registScreen.destroy()
                labPrompt.config(text = "請輸入帳號與密碼。")     
            else:
                entryID.delete(0, "end") # 將框中第0個字元至尾清空
                entryPW.delete(0, "end")
    else:
        entryID.delete(0, "end")
        entryPW.delete(0, "end")
        labPrompt.config(text = "帳號或密碼錯誤！")     

def registConfirm():
    idData = entryRegistID.get()
    pwData = entryRegistPW.get()
    if len(idData) > 0 and len(pwData):
        idHash = hashlib.sha256(idData.encode("utf-8")).hexdigest()
        pwHash = hashlib.sha256(pwData.encode("utf-8")).hexdigest()
        if idHash not in account:
            account[idHash] = pwHash
            entryRegistID.delete(0, "end")
            entryRegistPW.delete(0, "end")
            labRegistPrompt.config(text = "註冊成功！")     
        else:
            entryRegistID.delete(0, "end")
            entryRegistPW.delete(0, "end")
            labRegistPrompt.config(text = "此帳戶已經存在！")     
    else:
        entryID.delete(0, "end")
        entryPW.delete(0, "end")
        labRegistPrompt.config(text = "帳號或密碼不可為空！")     


def switchRegest():
    registScreen.deiconify()
    loginScreen.withdraw()
    labRegistPrompt.config(text = "請輸入欲註冊之帳號與密碼。")

def switchLogin():
    loginScreen.deiconify()
    registScreen.withdraw()

def exitProgram():
    loginScreen.destroy() # 銷毀
    registScreen.destroy()
    root.destroy()

def hashParsing():
    h = entryHash.get()
    
    hHash = hashlib.sha256(h.encode("utf-8")).hexdigest() #encode重新編碼 16進制摘要
    print(hHash)
    
    if h in hashCode:
        labHash.config(text = hashCode[h])
    else:
        labHash.config(text = "無此資料。")




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




root = Tk()
root.geometry("400x300+200+100")
root.title("OX Game")
loginScreen = Toplevel(root) # 登入視窗
loginScreen.title("Login")
registScreen = Toplevel(root) # 註冊視窗
registScreen.title("Regist")


# GUI
'''loginScreen_登入頁面'''
labID = Label(loginScreen, text = "ID", anchor = E, justify = RIGHT, font = ("Times", 30)) # anchor = 元件對齊方位, justify = 文字對齊方向
labPW = Label(loginScreen, text = "Password", anchor = E, justify = RIGHT, font = ("Times", 30))
labPrompt = Label(loginScreen, text = "請輸入帳號與密碼。", anchor = CENTER, justify = CENTER, font = ("Times", 15))
labHash = Label(loginScreen, text = "請輸入HashCode。", anchor = CENTER, justify = CENTER, font = ("Times", 15))

entryID = Entry(loginScreen) # 輸入框
entryPW = Entry(loginScreen, show = "*") # show = 顯示字元
entryHash = Entry(loginScreen)

btnLogin = Button(loginScreen, text = "Login", command = login, font = ("Times", 18), width = 12)
btnRegist = Button(loginScreen, text = "Regist", command = switchRegest, font = ("Times", 18), width = 12)
btnExit = Button(loginScreen, text = "Exit", command = exitProgram, font = ("Times", 18), width = 12)
btnHash = Button(loginScreen, text = "Unhash", command = hashParsing, font = ("Times", 18), width = 12)

'''loginScreen_grid'''
labID.grid(row = 0, column = 0, sticky = NSEW)
entryID.grid(row = 0, column = 1, sticky = NSEW)

labPW.grid(row = 1, column = 0, sticky = NSEW)
entryPW.grid(row = 1, column = 1, sticky = NSEW)

btnLogin.grid(row = 2, column = 0, sticky = NSEW)
btnRegist.grid(row = 2, column = 1, sticky = NSEW)
btnExit.grid(row = 2, column = 2, sticky = NSEW)

labPrompt.grid(row = 3, column = 1, sticky = NSEW)

entryHash.grid(row = 4, column = 0, sticky = NSEW)
btnHash.grid(row = 4, column = 1, sticky = NSEW)
labHash.grid(row = 4, column = 2, sticky = NSEW)

'''registScreen_註冊頁面'''
labRegistID = Label(registScreen, text = "Regist ID", anchor = E, justify = RIGHT, font = ("Times", 20))
labRegistPW = Label(registScreen, text = "Regist Password", anchor = E, justify = RIGHT, font = ("Times", 20))
labRegistPrompt = Label(registScreen, text = "請輸入欲註冊之帳號與密碼。", anchor = CENTER, justify = CENTER, font = ("Times", 15))

entryRegistID = Entry(registScreen)
entryRegistPW = Entry(registScreen, show = "*")


btnRegistBack = Button(registScreen, text = "Back", command = switchLogin, font = ("Times", 18), width = 12)
btnRegistConfirm = Button(registScreen, text = "Confirm", command = registConfirm, font = ("Times", 18), width = 12)
btnRegistExit = Button(registScreen, text = "Exit", command = exitProgram, font = ("Times", 18), width = 12)

'''registScreen_grid'''
labRegistID.grid(row = 0, column = 0 ,sticky = NSEW)
entryRegistID.grid(row = 0, column = 1 ,sticky = NSEW)

labRegistPW.grid(row = 1, column = 0 ,sticky = NSEW)
entryRegistPW.grid(row = 1, column = 1 ,sticky = NSEW)

btnRegistBack.grid(row = 2, column = 0, sticky = NSEW)
btnRegistConfirm.grid(row = 2, column = 1, sticky = NSEW)
btnRegistExit.grid(row = 2, column = 2, sticky = NSEW)

labRegistPrompt.grid(row = 3, column = 1,sticky = NSEW)

'''root_遊戲頁面'''
for row in range(3):
    root.rowconfigure(row, weight = 1) # 第row行設定 權重
for column in range(3):
    root.columnconfigure(column, weight = 1) # 第column行設定 權重

'''root_grid'''
btnList = []
flag = True
for row in range(3):
    for column in range(3):
        btn = Button(root, text = "", command = lambda:setBtnText(), font = ("Times", 20)) # lambda: 可在函式內代入參數
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



root.withdraw() # 抽出視窗 使其不會出現
registScreen.withdraw()
root.mainloop() # 主程式