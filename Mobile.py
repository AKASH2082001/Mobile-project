import sqlite3

from prettytable import PrettyTable

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
    print("6. view the most expensive mobile phone")
    print("7. view the less expensive mobile phone")
    print("8. view the average cost of mobile phone")
    print("9. display total count of mobile phone in stock")
    print("10. display total amount of mobile phone in stock")
    print("11. display sum of mobile phone prices")
    print("12. display total amount of mobile phone inn stock based on each brand")
    print("13. display the mobile phone based on price range")
    print("14. exit")

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

        table = PrettyTable(["Id","serialno","mobilebrand","mobilename","getmanufactureyear","manufacturemonth","price"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)

    elif choice == 3:
        result = connection.execute("select * from smartphones")
        table = PrettyTable(["Id","serialno","mobilebrand","mobilename","getmanufactureyear","manufacturemonth","price"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)

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

        table = PrettyTable(["Id","serialno","mobilebrand","mobilename","getmanufactureyear","manufacturemonth","price"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)

    elif choice == 5:
        getserialno = input("enter the serialno: ")

        connection.execute("delete from smartphones where serialno=" +getserialno)
        connection.commit()

        print("Data deleted successfully")

        result = connection.execute("select * from smartphones")

        print("data updated")

        table = PrettyTable(["Id","serialno","mobilebrand","mobilename","getmanufactureyear","manufacturemonth","price"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)

    elif choice == 6:
        result= connection.execute("select max(price) as price from smartphones")

        for i in result:
            print("max value=>",i[0])

    elif choice == 7:
        result = connection.execute("select min(price) as price from smartphones")

        for i in result:
            print("min value=>", i[0])

    elif choice == 8:
        result = connection.execute("select avg(price) as price from smartphones")

        for i in result:
            print("average value=>", i[0])

    elif choice == 9:
        result = connection.execute("select count(*) as price from smartphones")

        for i in result:
            print("total count=>", i[0])

    elif choice == 10:
        result = connection.execute("select * from smartphones where price=(select max(price) from smartphones)")

        table = PrettyTable(["Id","serialno","mobilebrand","mobilename","getmanufactureyear","manufacturemonth","price"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)

    elif choice == 11:
        result = connection.execute("select sum(price) as price from smartphones")

        for i in result:
            print("sum of cost=>", i[0])

    elif choice == 12:
        result = connection.execute("select mobilebrand,sum(price) as price from smartphones group by mobilebrand")
        table = PrettyTable(["mobilebrand","price"])

        for i in result:
            table.add_row([i[0],i[1]])
        print(table)

    elif choice == 13:
        loweramount = input("enter the lower amount")
        higheramount = input("enter the higher amount")
        result = connection.execute("select * from smartphones where price between "+loweramount+" AND "+higheramount+"")

        table = PrettyTable(["Id","serialno","mobilebrand","mobilename","getmanufactureyear","manufacturemonth","price"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6]])
        print(table)


    elif choice == 14:
        break

    else:
        print("invalid choice")
