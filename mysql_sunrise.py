import pymysql
def add_0(name,data):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cao')
    cur = conn.cursor()
    cur.execute(f'insert into {name} values {data}')
    conn.commit()
    cur.close()
    conn.close()
def drop_0(name,reason):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cao')
    cur = conn.cursor()
    cur.execute(f'delete from {name} where {reason}')
    conn.commit()
    cur.close()
    conn.close()
def alter_0(inside):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cao')
    cur = conn.cursor()
    cur.execute(f'{inside}')
    conn.commit()
    cur.close()
    conn.close()
def finder_0(inside):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cao')
    cur = conn.cursor()
    cur.execute(f'{inside}')
    for users in cur.fetchall():
        print(users)
    cur.close()
    conn.close()
def look_0(inside):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='cao')
    cur = conn.cursor()
    cur.execute(f'select * from {inside}')
    list=[]
    for users in cur.fetchall():
        list.append(users)
    cur.close()
    conn.close()
    return (list)
