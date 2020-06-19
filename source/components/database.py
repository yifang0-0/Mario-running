import pymysql
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
            shopinfo = getUserShopinfo(id)
            userinfo = result[0]
            print(userinfo)
            print(shopinfo)
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
    id = result[0][0]
    return id

def getUserShopinfo(id):
    sql_getshopinfo = """SELECT * FROM shopinfo WHERE ID = %s"""
    cursor = db.cursor()
    cursor.execute(sql_getshopinfo, id)
    result = cursor.fetchall()
    return result[0]

def setup_shop(price, goodid, username):
    pass

def main():
    print("ok")
    login("zhou11","test123")
    db.close()

if __name__ == '__main__':
    main()
