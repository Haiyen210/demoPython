# import thư viện
import mysql.connector
# kết nối tới mysql
def connect_mysql():
    connect=mysql.connector.connect(
        host="localhost",
        database="test",
        user="root",
        password=""
        )
    return connect
#thêm
def insert():
    con=connect_mysql()
    cursor=con.cursor()
    insert_pro = "insert into product(name,price,status) values(%s,%s,%s)"
    name=input("Tên SP:")
    price=input("Giá SP: ")
    status=input("Nhập trạng thái: ")
    cursor.execute(insert_pro,(name,price,status))
    con.commit()
    con.close()
    cursor.close()

#sửa
def update(name,price,status,id):
    con=connect_mysql()
    cursor=con.cursor()
    sql="update product set name=%s, price=%s, status=%s where id=%s",(name,price,status,id)
    id=input("Nhập Id: ")
    name=input("Tên SP:")
    price=input("Giá SP: ")
    status=input("Nhập trạng thái: ")
    cursor.execute(sql)
    con.commit()
    con.close()
    cursor.close()

#show
def showall():
    con=connect_mysql()
    cursor=con.cursor()
    sql="select * from product"
    cursor.execute(sql)
    records=cursor.fetchall()
    print("---------------DANH SÁCH SẢN PHẨM---------------\n")
    print("ID","\t","Name","\t","Price","\t","Status")
    print("-------------------------------")
    for r in records:
        print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],"\n")
    print("------------------------------------------------")
    con.close()
    cursor.close()

#xóa
def delete():
    con=connect_mysql()
    cursor=con.cursor()
    sql="delete from product where id=%s"

    id = input("Mã cần xóa: ")
    count = cursor.execute(sql,(id))
    con.commit()
    con.close()
    cursor.close()
    if(count>0):
        print("Xóa thành công")
    else:
        print("Mã không tồn tại")

#hàm nhập
def input_pro():
    print("--------------DANH SÁCH NHÂN VIÊN-------------")
    while(True):
        insert()
        choose=input("Bạn có muốn nhập tiếp ko? ")
        if(choose=="N"):
            break
    print("----------------------------------------")

while(True):
    print("1. Nhập SP")
    print("2. Hiển thị tất cả SP")
    print("3. Sửa SP")
    print("4. Xóa SP")
    print("5. Thoát")
    choose=input("Chọn một chức năng:")
    con=connect_mysql()
    if(choose=="1"): 
        input_pro()
    elif(choose=="2"):
        showall()
    elif(choose=="3"):
        update()
    elif(choose=="4"):
        delete()
    elif(choose=="5"):
        break
    else:
        print("Mời bạn chọn lại")
print("Kết thúc")
