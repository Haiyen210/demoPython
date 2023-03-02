# import thư viện
import mysql.connector
import datetime
# kết nối tới mysql và làm việc với
def connect_mysql():
    con=mysql.connector.connect(
        host="localhost",
        database="demo",
        user="root",
        password="123456aA@"
        )
    return con
def insert(EmployeeId, FullName, Birthday, Phone,con):
    con = connect_mysql()
    cursor = con.cursor()
    cursor.execute("insert into tbl_Employee values(%s,%s,%s,%s)",(EmployeeId,FullName,Birthday,Phone))
    con.commit()
    cursor.close()

def update_category(con):
    con=connect_mysql()
    cursor=con.cursor()
    update_mysql="update tbl_Employee set FullName=%s,Birthday=%s,Phone=%s where EmployeeId=%s"
    EmployeeId = input("Mã NV:")
    FullName = input("Tên NV:")
    Birthday = datetime.datetime.strptime(input("Ngày sinh dd/mm/yyyy:"), "%d/%m/%Y")
    Phone = input("Điện thoại:")
    cursor.execute(update_mysql,(FullName, Birthday,Phone,EmployeeId))
    con.commit()
    cursor.close()

def delete_employee(id,con):
    con = connect_mysql()
    cursor = con.cursor()
    cursor.execute("delete from tbl_Employee where EmployeeId=%s",(id,))
    con.commit()
    cursor.close()
    
def search_employee(name,con):
    con = connect_mysql()
    cursor = con.cursor()
    count = cursor.execute("select * from tbl_Employee where FullName=%s",(name,))
    myresult = cursor.fetchall()
    if(myresult):
        print("---------------Danh sách nhân viên--------------")
        for r in myresult:
            print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],)
    else:
        print("Khoogn timg thấy")
    con.commit()
    cursor.close()

def show_all(con):
     con = connect_mysql()
     cursor = con.cursor()
     cursor.execute("select * from tbl_Employee")
     records = cursor.fetchall()
     print("---------------Danh sách nhân viên--------------")
     for r in records:
         print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],)
     cursor.close()

def input_employee(con):
    print("-------------------Danh sách nhân viên-----------------")
    while(True):
        EmployeeId = input("Mã NV:")
        FullName = input("Tên NV:")
        Birthday = datetime.datetime.strptime(input("Ngày sinh dd/mm/yyyy:"), "%d/%m/%Y")
        Phone = input("Điện thoại:")
        insert(EmployeeId,FullName,Birthday,Phone,con)
        choose = input("Bạn có muốn nhập tiếp không?y/n:")
        if(choose == "n"):
            break
    print("---------------------------------------")
con = connect_mysql()
while(True):
    print("1. Nhập nhân viên")
    print("2. Hiển thị tất cả nhân viên")
    print("3. Sửa thông tin")
    print("4. Xóa nhân viên")
    print("5. Tìm kiếm nhân viên")
    print("6. Thoát")
    choose = input("Chọn 1 chức năng:")
    if(choose == "1"):
        input_employee(con)
    elif(choose == "2"):
        show_all(con)
    elif(choose == "3"):
        update_category(con)
    elif(choose == "4"):
        id = input("Nhập mã cần xóa:")
        delete_employee(id,con)
    elif(choose == "5"):
        name = input("Nhập tên nhân viên muốn tìm:")
        search_employee(name,con)
    elif(choose == "6"):
        break
    else:
        print("Bạn chọn sai rồi")
print("Kết thúc chương trình")