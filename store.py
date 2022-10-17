def tell():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="aadil123")

    #CREATING DATABASE AND TABLE
    mycursor=mydb.cursor()
    mycursor.execute("create database if not exists store")
    mycursor.execute("use store")
    mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")
    def bill():
            mycursor.execute("use bill")
            mycursor.execute("show tables")
            ho=mycursor.fetchall()
            for row in ho:
                print(row)
            p=str(input('select customer:'))
            mycursor.execute("select * from "+str(p))
            for x in mycursor:
                print(x)
    def bill2(cus):
        mycursor.execute("create database if not exists bill")
        mycursor.execute("use bill")
        mycursor.execute("create table if not exists "+str(cus)+"(CustomerName varchar(20),PhoneNumber char(10),itemName varchar(30),Quantity int(100),Price int(4))")
        n_n=int(input('enter no of items:'))
        for i in range(n_n):
            cusname=str(input("Enter customer name:"))
            phno=int(input("Enter phone number:"))
            item=str(input("Enter item Name:"))
            price=int(input("Enter the price:"))
            n=int(input("Enter quantity:"))
            mycursor.execute("insert into "+str(cus)+" values('"+cusname+"','"+str(phno)+"','"+item+"','"+str(n)+"','"+str(price)+"')")
        mydb.commit()
    while True:
        print("""1:Signup
    2:Login""")

        ch=int(input("SIGNUP/LOGIN(1,2):"))

    #SIGNUP
        if ch==1:

            username=input("USERNAME:")
            pw=input("PASSWORD:")

            mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
            mydb.commit()

    #LOGIN
        elif ch==2:

            username=input("USERNAME:")

            mycursor.execute("select username from signup where username='"+username+"'")
            pot=mycursor.fetchone()

            if pot is not None:
                print("VALID USERNAME!!!!!!")

                pw=input("PASSWORD:")

                mycursor.execute("select password from signup where password='"+pw+"'")
                a=mycursor.fetchone()

                if a is not None:
                    print("""+++++++++++++++++++++++
    +++LOGIN SUCCESSFULL+++
    +++++++++++++++++++++++""")

                    print("""======================================================================
    ++++++++++++++++++++++++++    TURBO STORE     +++++++++++++++++++++++++
    ==========================================================================""")

                    mycursor.execute("create table if not exists item(itemName varchar(30) primary key,type varchar(20),Quantity int(3),dealer varchar(20),CODE varchar(30),Price int(4))")
                    mycursor.execute("create table if not exists Sell_rec(CustomerName varchar(20),PhoneNumber char(10) unique key, itemName varchar(30),Quantity int(100),Price int(4),foreign key (itemName) references item(itemName))")
                    mycursor.execute("create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber char(10) unique key , Address varchar(40))") 
                    mydb.commit()

                    while(True):
                        print("""1:Add items
    2:Delete items
    3:Search items
    4:Staff Details
    5:Sell Record
    6:Available items
    7:Total Income after the Latest Reset 
    8:Exit
    9:Billing
    10:Review bills
    11:Update list""")

                        a=int(input("Enter your choice:"))

        #ADD ITEMS
                        if a==1:
                            mycursor.execute("use store")

                            print("All information prompted are mandatory to be filled")
                        
                            item=str(input("Enter item Name:"))
                            type=str(input("type:"))
                            quantity=int(input("Enter quantity:"))        
                            dealer=str(input("Enter dealer name:"))
                            CODE=str(input("Enter CODE :"))
                            price=int(input("Enter the price:"))

                            mycursor.execute("select * from item where ITEMNAME='"+item+"'")
                            row=mycursor.fetchone()

                            if row is not None:
                                mycursor.execute("update item set quantity=quantity+'"+str(quantity)+"' where ITEMNAME='"+item+"'")
                                mydb.commit()

                                print("""++++++++++++++++++++++
    ++SUCCESSFULLY ADDED++
    ++++++++++++++++++++++""")
                            
                            
                            else:
                                mycursor.execute("insert into item(ITEMNAME,type,quantity,dealer,CODE,price) values('"+item+"','"+type+"','"+str(quantity)+"','"+dealer+"','"+CODE+"','"+str(price)+"')")
                                mydb.commit()

                                print("""++++++++++++++++++++++
    ++SUCCESSFULLY ADDED++
    ++++++++++++++++++++++""") 
                       

        #DELETE ITEMS
                        elif a==2:
                            mycursor.execute("use store")

                            print("AVAILABLE ITEMS...")

                            mycursor.execute("select * from item ")
                            for x in mycursor:
                                print(x)
                          
                            cusname=str(input("Enter customer name:"))
                            phno=int(input("Enter phone number:"))
                            item=str(input("Enter item Name:"))
                            price=int(input("Enter the price:"))
                            n=int(input("Enter quantity:"))

                            mycursor.execute("select quantity from item where ITEMNAME='"+item+"'")
                            lk=mycursor.fetchone()

                            if max(lk)<n:
                                print(n,"items are not available!!!!")

                            else:
                                mycursor.execute("select ITEMNAME from item where ITEMNAME='"+item+"'")
                                log=mycursor.fetchone()

                                if log is not None:
                                    mycursor.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+item+"','"+str(n)+"','"+str(price)+"')")
                                    mycursor.execute("update item set quantity=quantity-'"+str(n)+"' where itemName='"+item+"'")
                                    mydb.commit()

                                    print("""++++++++++++++++++++++
    ++ITEM HAS BEEN itemed++
    ++++++++++++++++++++++""")

                                else:
                                    print("ITEM IS NOT AVAILABLE!!!!!!!")

        #SEARCH ITEMS ON THE BASIS OF GIVEN OPTIONS
                                    
                        elif a==3:
                            mycursor.execute("use store")

                            print("""1:Search by name
    2:Search by type
    3:Search by dealer""")

                            l=int(input("Search by?:"))

            #BY ITEMNAME
                            if l==1:
                                o=input("Enter item to search:")

                                mycursor.execute("select ITEMNAME from item where ITEMNAME='"+o+"'")
                                tree=mycursor.fetchone()

                                if tree!=None:
                                    print("""++++++++++++++++++++
    ++ITEM IS IN STOCK++
    ++++++++++++++++++++""")

                                else:
                                    print("ITEM IS NOT IN STOCK!!!!!!!")

            #BY TYPE
                            elif l==2:
                                g=input("Enter type to search:")

                                mycursor.execute("select type from item where type='"+g+"'")
                                poll=mycursor.fetchall()

                                if poll is not None:
                                    print("""++++++++++++++++++++
    ++ITEM IS IN STOCK++
    ++++++++++++++++++++""")

                                    mycursor.execute("select * from item where type='"+g+"'")

                                    for y in mycursor:
                                        print(y)

                                else:
                                    print("ITEMS OF SUCH TYPE ARE NOT AVAILABLE!!!!!!!!!")


            #BY DEALER NAME
                            elif l==3:
                                au=input("Enter dealer to search:")

                                mycursor.execute("select dealer from item where dealer='"+au+"'")
                                home=mycursor.fetchall()

                                if home is not None:
                                    print("""++++++++++++++++++++
    ++ITEM IS IN STOCK++
    ++++++++++++++++++++""")

                                    mycursor.execute("select * from item where dealer='"+au+"'")

                                    for z in mycursor:
                                        print(z)

                                else:
                                    print("ITEMS OF THIS DEALER ARE NOT AVAILABLE!!!!!!!")
                            mydb.commit()

        #STAFF DETAILS
                        elif a==4:
                            mycursor.execute("use store")
                            print("1:New staff entry")
                            print("2:Remove staff")
                            print("3:Existing staff details")

                            ch=int(input("Enter your choice:"))

            #NEW STAFF ENTRY
                            if ch==1:
                                fname=str(input("Enter Fullname:"))
                                gender=str(input("Gender(M/F/O):"))
                                age=int(input("Age:"))
                                phno=int(input("Staff phone no.:"))
                                add=str(input("Address:"))

                                mycursor.execute("insert into Staff_details(name,gender,age,phonenumber,address) values('"+fname+"','"+gender+"','"+str(age)+"','"+str(phno)+"','"+add+"')")
                                print("""+++++++++++++++++++++++++++++
    +STAFF IS SUCCESSFULLY ADDED+
    +++++++++++++++++++++++++++++""")
                                mydb.commit()

            #REMOVE STAFF
                            elif ch==2:
                                nm=str(input("Enter staff name to remove:"))
                                mycursor.execute("select name from staff_details where name='"+nm+"'")
                                toy=mycursor.fetchone()

                                if toy is not None:
                                    mycursor.execute("delete from staff_details where name='"+nm+"'")
                                    print("""+++++++++++++++++++++++++++++++++
    ++STAFF IS SUCCESSFULLY REMOVED++
    +++++++++++++++++++++++++++++++++""")
                                    mydb.commit()

                                else:
                                    print("STAFF DOESNOT EXIST!!!!!!")

            #EXISTING STAFF DETAILS
                            elif ch==3:
                                mycursor.execute("select * from Staff_details")
                                run=mycursor.fetchall()
                                if run is not None:
                                    print("EXISTING STAFF DETAILS...")                        
                                    for t in run:
                                        print(t)

                                else:
                                    print("NO STAFF EXISTS!!!!!!!")
                                mydb.commit()

        #SELL HISTORY                                
                        elif a==5:
                            mycursor.execute("use store")
                            print("1:Sell history details")
                            print("2:Reset Sell history")

                            ty=int(input("Enter your choice:"))

                            if ty==1:
                                mycursor.execute("select * from sell_rec")
                                for u in mycursor:
                                    print(u)

                            if ty==2:
                                bb=input("Are you sure(Y/N):")

                                if bb=="Y":
                                    mycursor.execute("delete from sell_rec")
                                    mydb.commit()

                                elif bb=="N":
                                    pass

        #AVAILABLE ITEMS
                        elif a==6:
                            mycursor.execute("use store")
                            mycursor.execute("select * from item order by ITEMNAME")
                            for v in mycursor:
                                print(v)

        #TOTAL INCOME AFTER LATEST UPDATE
                        elif a==7:
                            mycursor.execute("use store")
                            
                            mycursor.execute("select sum(price) from sell_rec")
                            for x in mycursor:
                                print(x)
        #EXIT                    
                        elif a==8:
                             quit()
        #billing
                        elif a==9:
                            cus=str(input('enter customer name:'))
                            bill2(cus)
                        
         # Review bills
                        elif a==10:
                            bill()
        #update items
                        elif a==11:
                            mycursor.execute("use store")
                            i=str(input("Enter item Name:"))
                            t=str(input("type:"))
                            q=int(input("Enter quantity:"))        
                            dr=str(input("Enter dealer name:"))
                            C=str(input("Enter CODE :"))
                            p=int(input("Enter the price:"))
                            mycursor.execute("update item set Quantity='"+str(q)+"' where ITEMNAME='"+i+"'")
                            mydb.commit()
                            mycursor.execute("update item set type='"+str(t)+"' where ITEMNAME='"+i+"'")
                            mydb.commit()
                            mycursor.execute("update item set dealer='"+str(dr)+"' where ITEMNAME='"+i+"'")
                            mydb.commit()
                            mycursor.execute("update item set price='"+str(p)+"' where ITEMNAME='"+i+"'")
                            mydb.commit()
                            mycursor.execute("update item set CODE='"+str(C)+"' where ITEMNAME='"+i+"'")
                            mydb.commit()

                            print("""++++++++++++++++++++++
            ++LIST UPDATED++
            ++++++++++++++++++++++""")
                        else:
                                            print("""++++++++++++++++++++++
                            ++INCORRECT OPTION++
                            ++++++++++++++++++++++""")
     

                                
                            

    #LOGIN ELSE PART
                else:
                    print("""++++++++++++++++++++++
    ++INCORRECT PASSWORD++
    ++++++++++++++++++++++""")


            else:
                print("""++++++++++++++++++++
    ++INVALID USERNAME++
    ++++++++++++++++++++""")

        else:
            break
            quit()

tell()
