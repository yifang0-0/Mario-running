from tkinter import *
import tkinter.messagebox
import database as db

def loginIn():
    username=entry1.get()
    password=entry2.get()
    print(username)
    print(password)
    if(lengthControl(username, password)):
        info = db.login(username, password)
        if info == 'notfinduser':
            wantToRegister(username, password)
        if info == 'wrongpassword':
            tkinter.messagebox.showerror('错误','密码错误!')
        if info == 'loginsuccess':
            tkinter.messagebox.showinfo('成功', '恭喜你成功登录!')

def wantToRegister(username, password):
    result = tkinter.messagebox.askokcancel(title='是否注册', message='您尚未注册，是否要注册？')
    if result :
        print("yes")
        register()

def register():
    username = entry1.get()
    password = entry2.get()
    print(username)
    print(password)
    if(lengthControl(username, password)):
        info = db.register(username,password)
        if info == 'alreadyexist':
            tkinter.messagebox.showerror('错误','已经存在该用户!')
        if info == 'registersuccess':
            tkinter.messagebox.showinfo('成功', '恭喜你成功注册!')

def lengthControl(username, password):
    if len(username) < 6:
        tkinter.messagebox.showwarning('警告', '用户名过短，请输入6-15个字符')
        return False
    if len(password) < 6:
        tkinter.messagebox.showwarning('警告', '密码过短，请输入6-15个字符')
        return False
    if len(username) > 16:
        tkinter.messagebox.showwarning('警告', '用户名过长，请输入6-15个字符')
        return False
    if len(username) > 16:
        tkinter.messagebox.showwarning('警告', '密码过长，请输入6-15个字符')
        return False
    return True

# def setup_window():
loginwindow = Tk()
loginwindow.title('login in')

width = 300
height = 150

screenwidth = loginwindow.winfo_screenwidth()
screenheight = loginwindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
loginwindow.geometry(alignstr)

Label(loginwindow, text="用户名：",font = ',10').grid(row=2, column=1)
Label(loginwindow, text="密码：",font = ',10').grid(row=3, column=1)
entry1=Entry(loginwindow)
entry2=Entry(loginwindow,show='*')
entry1.grid(row=2, column=2)
entry2.grid(row=3, column=2)

Button(loginwindow, text='登录',command=loginIn,width=8, height=2).grid(row=4, column=1,sticky=W, padx=5, pady=5)
Button(loginwindow, text='注册', command=register,width=8, height=2).grid(row=4, column=2, sticky=W, padx=5, pady=5)
Button(loginwindow, text='退出',command=loginwindow.quit,width=8, height=2).grid(row=4, column=3)
loginwindow.resizable(width=False, height=True)

loginwindow.mainloop()

if __name__ == '__main__':
 main()