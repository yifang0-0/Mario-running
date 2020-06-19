import pymysql
from . import dataBaseGlobalData as GD
from .. import constants as c
from tkinter import *
from tkinter import messagebox

db = pymysql.connect('localhost','zhouyan','123456Qaz','mario')

def login(username, password):
    cursor = db.cursor()
    sql_SELECT1 = """SELECT * FROM userinfo WHERE USER_NAME = %s"""
    sql_SELECT2 = """SELECT * FROM userinfo WHERE USER_NAME = %s AND PASSWORD = %s"""

    #如果数据库中不存在该用户用户名，则默认为注册
    cursor.execute(sql_SELECT1,(username))
    result = cursor.fetchall()
    if len(result) == 0:
        return 'notfinduser'
    else:
        #如果存在，则根据用户名与密码进行查询
        cursor.execute(sql_SELECT2, (username, password))
        result = cursor.fetchall()
        #如果没有查询到，说明密码错误
        if len(result) == 0:
            return 'wrongpassword'
        else:
            #查询到后，获取用户信息
            id = getUserId(username)
            GD.shopinfo = list(getUserShopinfo(id))
            GD.userinfo = list(result[0])
            print(GD.userinfo)
            print(GD.shopinfo)
            return 'loginsuccess'

def register(username, password):
    cursor = db.cursor()
    sql_SELECT1 = """SELECT * FROM userinfo WHERE USER_NAME = %s"""
    cursor.execute(sql_SELECT1, (username))
    result = cursor.fetchall()
    if len(result) != 0:
        return 'alreadyexist'

    sql_REGISTER1 = """INSERT INTO userinfo(ID, USER_NAME, PASSWORD, STATUS)
    VALUES(null, %s, %s, 1)"""
    sql_REGISTER2 = """INSERT INTO shopinfo(ID) VALUES(%s)"""
    #插入userinfo表中
    cursor.execute(sql_REGISTER1, (username, password))
    db.commit()
    id = getUserId(username)
    #插入商店表中
    cursor.execute(sql_REGISTER2, (id))
    db.commit()
    return 'registersuccess'

def getUserId(username):
    cursor = db.cursor()
    sql_getId = """SELECT * FROM userinfo WHERE USER_NAME = %s"""
    cursor.execute(sql_getId, (username))
    result = cursor.fetchall()
    GD.userid = result[0][0]
    return GD.userid

def getUserShopinfo(id):
    sql_getshopinfo = """SELECT * FROM shopinfo WHERE ID = %s"""
    cursor = db.cursor()
    cursor.execute(sql_getshopinfo, id)
    result = cursor.fetchall()
    return result[0]

#根据数据库信息更新本地信息
def updateShopInfo(id):
    sql_getshopinfo = """SELECT * FROM shopinfo WHERE ID = %s"""
    cursor = db.cursor()
    cursor.execute(sql_getshopinfo, id)
    result = cursor.fetchall()
    GD.shopinfo = list(result[0])

def buyThings(price, goodid):
    coins = GD.shopinfo[c.COINID]
    lifes = GD.shopinfo[c.LIFEID]
    speed = GD.shopinfo[c.SPEEDID]
    jump = GD.shopinfo[c.JUMPID]
    if coins < price:
        Tk().wm_withdraw()
        messagebox.showerror('错误', '好好工作，努力赚钱')
        return False
    else:
        coins -= price
        update_coin(coins)
        if goodid == c.LIFEID:
            lifes += 1
            update_life(lifes)
            Tk().wm_withdraw()
            messagebox.showinfo('提示', '一股暖流入肚，你仿佛获得了新生！')
        if goodid == c.SPEEDID:
            speed += 1
            update_speed(speed)
            Tk().wm_withdraw()
            messagebox.showinfo('提示', '你感受到了风的流动，它在推动着你前行！')
        if goodid == c.JUMPID:
            jump += 1
            update_jump(jump)
            Tk().wm_withdraw()
            messagebox.showinfo('提示', '你觉得双腿充满了力量，重力无法束缚住你了！')
        updateShopInfo(GD.userid)
        return True

def update_coin(newcoins):
    sql_updateCoin = """UPDATE shopinfo SET COINS = %s WHERE ID = %s"""
    cursor = db.cursor()
    cursor.execute(sql_updateCoin, (newcoins, GD.userid))
    db.commit()

def update_life(newlifes):
    sql_updateCoin = """UPDATE shopinfo SET Lifes = %s WHERE ID = %s"""
    cursor = db.cursor()
    cursor.execute(sql_updateCoin, (newlifes, GD.userid))
    db.commit()

def update_speed(speed):
    sql_updateCoin = """UPDATE shopinfo SET Speed = %s WHERE ID = %s"""
    cursor = db.cursor()
    cursor.execute(sql_updateCoin, (speed, GD.userid))
    db.commit()

def update_jump(jump):
    sql_updateCoin = """UPDATE shopinfo SET Jump = %s WHERE ID = %s"""
    cursor = db.cursor()
    cursor.execute(sql_updateCoin, (jump, GD.userid))
    db.commit()

if __name__ == '__main__':
    print("ok")
    login("zhou11", "test123")
    db.close()
