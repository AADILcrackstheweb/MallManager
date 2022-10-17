import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="aadil123")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists movie")
mycursor.execute("use movie")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20),email varchar(40))")
while True:
    print("""1:Signup
2:Login""")

    ch=int(input("SIGNUP/LOGIN(1,2):"))

#SIGNUP
    if ch==1:

        username=input("USERNAME:")
        pw=input("PASSWORD:")
        e=input("E-mail:")

        mycursor.execute("insert into signup values('"+username+"','"+pw+"','"+e+"')")
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
++++++++++++++++++++++++""")

                print("""==========================================================================
++++++++++++++++++++++++++TURBO TECHIES THEATRE+++++++++++++++++++++++++
==========================================================================""")
                print('.',end="")
                print('|',end="")
                print('/',end="")
                print('{',end="")
                print('-',end="")
                print('}',end="")
                print('\\',end="")
                print('|',end="")
                print('.',end="")
                print('.')
                print('|',end="")
                print('/',end="")
                print('{',end="")
                print('-',end="")
                print('}',end="")
                print('\\',end="")
                print('|',end="")
                print('.',end="")
                print('.')
                print('|',end="")
                print('/',end="")
                print('{',end="")
                print('-',end="")
                print('}',end="")
                print('\\',end="")
                print('|',end="")
                print('.')
                print('MOVIES AVAILABLE')
                mycursor.execute("use movie")
                mycursor.execute("create table if not exists movi(sno varchar(20),movie varchar(30),category varchar(30),cost varchar(30))")
                l=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','e1','e2','e3','e4','e5','e6','e7','e8','e9','e10','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','g1','g2','g3','g4','g5','g6','g7','g8','g9','g10','h1','h2','h3','h4','h5','h6','h7','h8','h9','h10']
                la=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','e1','e2','e3','e4','e5','e6','e7','e8','e9','e10','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','g1','g2','g3','g4','g5','g6','g7','g8','g9','g10','h1','h2','h3','h4','h5','h6','h7','h8','h9','h10']
                lb=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','e1','e2','e3','e4','e5','e6','e7','e8','e9','e10','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','g1','g2','g3','g4','g5','g6','g7','g8','g9','g10','h1','h2','h3','h4','h5','h6','h7','h8','h9','h10']
                u=0
                seatd=[]
                while u<1:
                    mycursor.execute("select * from movi order by movie")
                    for v in mycursor:
                        print(v)
                    print("""1:Add movie
2:Remove movie
3:Book tickets
4:Update movie
5:Exit""")
                    a=int(input('Enter choice:'))
                    #add movie
                    if a==1:
                        mycursor.execute("use movie")

                        print("All information prompted are mandatory to be filled")
                        s=str(input("Enter the S.no:"))
                        item=str(input("Enter Movie Name:"))
                        category=str(input("Category:"))
                        cost=int(input("Enter the price:"))
                        mycursor.execute("select * from movi where movie='"+item+"'")
                        row=mycursor.fetchone()

                        if row is not None:
                            mycursor.execute("update movi set cost=cost+'"+str(cost)+"' and category='"+category+"' where movie='"+item+"'")
                            mydb.commit()
                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")


                        else:
                            mycursor.execute("insert into movi(sno,movie,category,cost) values('"+s+"','"+item+"','"+category+"','"+str(cost)+"')")
                            mydb.commit()
                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")

                #remove movie
                    elif a==2:
                        mycursor.execute("use movie")
                        s=str(input("Enter s.no of movie:"))
                        mycursor.execute("delete from movi where sno='"+s+"'")
                        print("""+++++++++++++++++++++++++++++++++
++MOVIE IS SUCCESSFULLY REMOVED++
+++++++++++++++++++++++++++++++++""")
                        mydb.commit()

                #book tickets
                    elif a==3:
                        n=input('Enter customer name:')
                        t1="10:00a.m-12:30p.m"
                        t2='02:00p.m-04:30p.m'
                        t3='06:30p.m-09:00p.m'
                        print("""
                t1:10:00a.m-12:30p.m
                t2:02:00p.m-04:30p.m
                t3:06:30p.m-09:00p.m
                """)
                        tb=input('Enter timing:')
                        mycursor.execute("use movie")
                        item=str(input('Enter movie name:'))
                        mycursor.execute("select * from movi where movie='"+item+"'")
                        g=mycursor.fetchone()
                        if g is not None:
                            print("""
                            |================================|
                            |   a1 a2 a3       a4 a5 a6 a7       a8 a9 a10 |
                            |================================|
                            |   b1 b2 b3       b4 b5 b6 b7      b8 b9 b10 |
                            |================================|
                            |   c1 c2 c3       c4 c5 c6 c7       c8 c9 c10 |
                            |================================|
                            |   d1 d2 d3       d4 d5 d6 d7      d8 d9 d10 |
                            |================================|
                            |   e1 e2 e3        e4 e5 e6 e7      e8  e9 e10 |
                            |================================|
                            |   f1   f2  f3        f4   f5  f6  f7       f8   f9  f10 |
                            |================================|
                            |  g1 g2 g3       g4  g5 g6 g7     g8   g9 g10|
                            |================================|
                            |  h1 h2 h3        h4 h5 h6 h7      h8   h9  h10|
                            |================================|""")
                            i=int(input('No of seats:'))
                            if tb=='t1':
                                tx=t1
                                print('Seats available:',l)
                                for r in range(i):
                                    t=input('Enter seat no:')
                                    seatd.append(t)
                                    l.remove(t)
                            elif tb=='t2':
                                tx=t2
                                print('Seats available:',la)
                                for r in range(i):
                                    t=input('Enter seat no:')
                                    seatd.append(t)
                                    la.remove(t)
                            elif tb=='t3':
                                tx=t3
                                print('Seats available:',lb)
                                for r in range(i):
                                    t=input('Enter seat no:')
                                    seatd.append(t)
                                    lb.remove(t)
                            else:
                                 print('incorrect time choice!')
                                 break
                            mycursor.execute("select cost from movi where movie='"+item+"'")
                            l2=mycursor.fetchone()
                            for z in l2:
                                c=int(z)
                            c1=c*i
                            j=int(input("Enter 1 if u want snacks or else 2 if you don't want:"))
                            p,b,f=200,150,80
                            if j==1:
                                we="yes"
                                print("""
                snacks available:
                1:popcorn
                2:burger
                3:french fries""")
                                y=int(input("Input choice:"))
                                if y==1:
                                    y2=int(input("Enter quantity:"))
                                    c2=p*y2
                                    c1+=c2
                                elif y==2:
                                    y2=int(input("Enter quantity:"))
                                    c2=b*y2
                                    c1+=c2
                                elif y==3:
                                    y2=int(input("Enter quantity:"))
                                    c2=f*y2
                                    c1+=c2
                                
                                j2=1
                                while (j2==1):
                                    j2=int(input("Enter 1 if u want to add more snacks or else 2 if you don't want:"))
                                    if j2==1:
                                        pass
                                    else:
                                        break
                                    print("""
                    snacks available:
                    1:popcorn
                    2:burger
                    3:french fries""")
                                    y=int(input("Input choice:"))
                                    if y==1:
                                        y2=int(input("Enter quantity:"))
                                        c2=p*y2
                                        c1+=c2
                                    elif y==2:
                                        y2=int(input("Enter quantity:"))
                                        c2=b*y2
                                        c1+=c2
                                    elif y==3:
                                         y2=int(input("Enter quantity:"))
                                         c2=f*y2
                                         c1+=c2
                                else:
                                     print("ok fine")
                            else:
                                print("ok fine")
                                we="no"
                               
                            o=input("Enter c for cash and cc for credit card:")
                            if o=='c':
                                print('pls pay rs.',c1)
                                print('your ticket:')
                                print('=======================')
                                print('Name:',n)
                                print('Movie:',item)
                                print('Timing:',tx)
                                print('Snacks:',we)
                                print('Cost:Rs.',c1)
                                print('Payment Option : Cash')
                                print('Seats:',seatd)
                                print('=======================')
                            if o=='cc':
                                print('pls pay rs.',c1)
                                cc=input("Credit card no:")
                                ccv=input("CCV no:")
                                cpin=input("Pin:")
                                print('your ticket:')
                                print('=======================')
                                print('Name:',n)
                                print('Movie:',item)
                                print('Timing:',tx)
                                print('Snacks:',we)
                                print('Cost:Rs.',c1)
                                print('Seats:',seatd)
                                print('Payment Option : Credit Card')
                                print('CreditCard no:',cc)
                                print('=======================') 
                              
                        else:
                            print('Movie not available!')
                #update
                    elif a==4:
                        mycursor.execute("use movie")
                        s2=str(input("Enter s.no of movie:"))
                        mycursor.execute("select * from movi where sno='"+s2+"'")
                        for a4 in mycursor:
                            print(a4)
                        i2=str(input("Enter Movie Name:"))
                        c2=str(input("Category:"))
                        c3=int(input("Enter the price:"))
                        mycursor.execute("update movi set movie='"+i2+"' where sno='"+s2+"'")
                        mydb.commit()
                        mycursor.execute("update movi set category='"+c2+"' where sno='"+s2+"'")
                        mydb.commit()
                        mycursor.execute("update movi set cost='"+str(c3)+"' where sno='"+s2+"'")
                        mydb.commit()
                        print("""++++++++++++++++++++++
++SUCCESSFULLY UPDATED++
++++++++++++++++++++++""")
                        mydb.commit()

                #exit
                    elif a==5:
                        quit()
                #incorrect choice
                    else:
                        print("Incorrect choice!Try again!")

#LOGIN ELSE PART
            else:
                print("""++++++++++++++++++++++
++INCORRECT PASSWORD++
++++++++++++++++++++++""")


        else:
            print("""++++++++++++++++++++
++INVALID USERNAME++
+++++++++++++++++++++""")

    else:
        break
        quit()
