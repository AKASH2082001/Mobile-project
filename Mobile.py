import sqlite3

connection = sqlite3.connect("mobile.db")

table_list = connection.execute("select name from sqlite_master where type='table' and name='smartphones'").fetchall()

if table_list != []:
    print("table already exsist")

else:
    connection.execute(''' create table smartphones(
                       Id integer primary key autoincrement,
                       serialno integer,
                       mobilebrand text,
                       mobilename text,
                       manufactureyear integer,
                       manufacturemonth text,
                       price integer
                       
    )''')

print("Table created")

while True:
    print("select an option from the given menu")
    print("1. add mobile phone")
    print("2. search an mobile phone using serialnumber")
    print("3. view all mobile phone")
    print("4. update an mobile phone using serialnumber")
    print("5. delete an mobile phone using serialnumber")
    print("6. exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        getserialno = input("enter the serial number:")
        getmobilebrand = input("enter the mobile brand name:")
        getmobilename = input("enter the mobile model name:")
        getmanufactureyear = input("enter the manufacture year:")
        getmanufacturemonth = input("enter the manufacture month:")
        getprice = input("enter the mobile price:")
        connection.execute("insert into smartphones(serialno,mobilebrand,mobilename,manufactureyear,manufacturemonth,price) values("+getserialno+",'"+getmobilebrand+"','"+getmobilename+"',"+getmanufactureyear+",'"+getmanufacturemonth+"',"+getprice+")")

        connection.commit()

        print("data inserted successfully")

    elif choice == 2:
        getserialno = input("enter the serialnumber to be search:")

        result = connection.execute("select * from smartphones where serialno= "+getserialno)

        for i in result:
            print("Id =>", i[0])
            print("serialno =>", i[1])
            print("mobilebrand =>", i[2])
            print("mobilename =>", i[3])
            print("manufactureyear =>", i[4])
            print("manufacturemonth =>", i[5])
            print("price =>", i[6])

    elif choice == 3:
        result = connection.execute("select * from smartphones")

        for i in result:
            print("Id =>", i[0])
            print("serialno =>", i[1])
            print("mobilebrand =>", i[2])
            print("mobilename =>", i[3])
            print("manufactureyear =>", i[4])
            print("manufacturemonth =>", i[5])
            print("price =>", i[6])

    elif choice == 4:
        getserialno = input("enter the serial number:")
        getmobilebrand = input("enter the mobile brand name:")
        getmobilename = input("enter the mobile model name:")
        getmanufactureyear = input("enter the manufacture year:")
        getmanufacturemonth = input("enter the manufacture month:")
        getprice = input("enter the mobile price:")

        result = connection.execute("update smartphones set mobilebrand='"+getmobilebrand+"',mobilename='"+getmobilename+"',manufactureyear="+getmanufactureyear+",manufacturemonth='"+getmanufacturemonth+"',price="+getprice+" where serialno="+getserialno+"")
        connection.commit()

        print("mobile data updated successfully")

        result = connection.execute("select * from smartphones where serialno="+getserialno+"")

        print("data updated")

        for i in result:
            print("Id =>", i[0])
            print("serialno =>", i[1])
            print("mobilebrand =>", i[2])
            print("mobilename =>", i[3])
            print("manufactureyear =>", i[4])
            print("manufacturemonth =>", i[5])
            print("price =>", i[6])

    elif choice == 5:
        getserialno = input("enter the serialno: ")

        connection.execute("delete from smartphones where serialno=" +getserialno)
        connection.commit()

        print("Data deleted successfully")

        result = connection.execute("select * from smartphones")

        print("data updated")

        for i in result:
            print("Id =>", i[0])
            print("serialno =>", i[1])
            print("mobilebrand =>", i[2])
            print("mobilename =>", i[3])
            print("manufactureyear =>", i[4])
            print("manufacturemonth =>", i[5])
            print("price =>", i[6])

    elif choice == 6:
        break

    else:
        print("invalid choice")
