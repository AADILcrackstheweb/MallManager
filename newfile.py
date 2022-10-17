# Importing required libraries
import tkinter
from sys import version_info
if version_info.major == 2:
    from Tkinter import *
    import Tkinter.messagebox as tkmsg
elif version_info.major == 3:
    from tkinter import *
    import tkinter.messagebox as tkmsg
import mysql.connector
import datetime
import speekmodule
from winsound import *
import rad2
PlaySound('a26.wav',SND_FILENAME)

# Functions for adding data to sql

def exe(x):
    global mycursor
    mycursor.execute(x)
def ctable(a):
    global mycursor
    mycursor.execute('CREATE TABLE ' + str(a))
def reset():
    global mycursor
    mycursor.close()


def snack():
    PlaySound('a1.wav',SND_FILENAME)
    f=tkmsg.askyesno("NOTICE!","This will quit u outta main home page!")
    if f > 0:
        r.destroy()
        PlaySound('a34.wav',SND_FILENAME)
        import food
    else:
        pass

def book():
    PlaySound('a1.wav',SND_FILENAME)
    f=tkmsg.askyesno("NOTICE!","This will quit u outta main home page!")
    if f > 0:
        r.destroy()
        PlaySound('a41.wav',SND_FILENAME)
        import book
    else:
        pass

   
def store():
    PlaySound('a1.wav',SND_FILENAME)
    f=tkmsg.askyesno("NOTICE!","This will quit u outta main home page if u prefer to exit its window!")
    if f > 0:
        PlaySound('a33.wav',SND_FILENAME)
        import store
    else:
        pass
    
def speak():
    PlaySound('a1.wav',SND_FILENAME)
    f=tkmsg.askyesno("NOTICE!","This will quit u outta main home page if u prefer to exit its window!")
    PlaySound('a35.wav',SND_FILENAME)
    import interactivex
    

def movie():
    PlaySound('a1.wav',SND_FILENAME)
    f=tkmsg.askyesno("NOTICE!","This will quit u outta main home page if u prefer to exit its window!")
    PlaySound('a36.wav',SND_FILENAME)
    import movie
    
# Functions for Tkinter windows
def home():
    PlaySound('a4.wav',SND_FILENAME)
    global rawbn
    global brno
    brno=rawbn.get()

    try:

        global username
        global password
        global mycursor
        global mydb

        # connecting to sql

        mydb = mysql.connector.connect(host='localhost',
                                       user=str(username.get()),
                                       passwd=str(password.get()))
        mycursor = mydb.cursor()

    except mysql.connector.errors.ProgrammingError:
        PlaySound('a2.wav',SND_FILENAME)
        tkmsg.showinfo('Access Denied',
                       'Username or Password for SQL database is wrong')


    if brno == 0:
        PlaySound('a3.wav',SND_FILENAME)
        tkmsg.showinfo('Branch not Selected',
                       'Please select anyone of the listed branches')
    else:

        # Tkinter home window

        r.destroy()
        global homewin
        homewin = Tk()
        homewin.title("^_^Turbo Stores^_^")
        PlaySound('a1.wav',SND_FILENAME)
        tkmsg.showinfo('Notice','Pls initialize database before start!')
        PlaySound('a4.wav',SND_FILENAME)
        tkmsg.showinfo('Welcome','welcome to turbo stores.')

        initbutton = Button(homewin, text='Initialize database', command=initialize,bg='red',fg='white',width='5',height='3')
        viewbutton = Button(homewin, text='View Available productss', command=view,bg='orange',fg='black',width='5',height='3')
        servicebutton = Button(homewin, text='service a products', command=service,bg='yellow',fg='black',width='5',height='3')
        serviceviewbutton=Button(homewin,text='View active services',command=serviceview,bg='green',fg='white',width='5',height='3')
        servicereturnbutton=Button(homewin,text='Return serviced products',command=returnproducts,bg='blue',fg='black',width='5',height='3')
        feedbackbutton=Button(homewin,text='Enter feedback',command=feed,bg='indigo',fg='white',width='5',height='3')
        viewfeedbutton=Button(homewin,text='View feedback',command=viewfeed,bg='purple',fg='white',width='5',height='3')
        addproductsbtn=Button(homewin,text='Add products',command=addproducts,bg='pink',fg='black',width='5',height='3')
        remproductsbtn=Button(homewin,text='Remove products',command=remproducts,bg='crimson',fg='white',width='5',height='3')
        infobutton=Button(homewin,text='About us',command=info,bg='brown',fg='white',width='5',height='3')
        searchbutton=Button(homewin,text='search',command=search,bg='black',fg='white',width='5',height='3')
        minbutton=Button(homewin,text='leastrate',command=mini,bg='grey',fg='white',width='5',height='3')
        quitbutton=Button(homewin,text='Exit',command=exitfun,bg='violet',fg='white',width='5',height='3')

        initbutton.pack(fill=X)
        viewbutton.pack(fill=X)
        servicebutton.pack(fill=X)
        servicereturnbutton.pack(fill=X)
        serviceviewbutton.pack(fill=X)
        feedbackbutton.pack(fill=X)
        viewfeedbutton.pack(fill=X)
        addproductsbtn.pack(fill=X)
        remproductsbtn.pack(fill=X)
        infobutton.pack(fill=X)
        searchbutton.pack(fill=X)
        minbutton.pack(fill=X)
        quitbutton.pack(fill=X)
        homewin.mainloop()

        global rawdata
        global brcc
        global count
        exe('USE products_service')
        viewwin = Tk()
        exe('SELECT * FROM branch' + str(brno))
        rawdata = mycursor.fetchall()
        brcc=[]
        for i in rawdata:
           brcc.append(str(i[3]))
        exe("""select * from branch1 union select * from branch2
            union select * from branch3 union select * from branch4""" )
        count=(len(mycursor.fetchall()))

def remproducts():
    PlaySound('a22.wav',SND_FILENAME)
    global remcc
    remw=Tk()
    remw.title("Remove")
    ccl=Label(remw,text="products-code")
    remcc=Entry(remw)
    okbtn=Button(remw,text="Remove products",command=remconfirm)

    ccl.grid(row=0,column=0)
    remcc.grid(row=0,column=1)
    okbtn.grid(row=1,column=1)

def remconfirm():
    global remcc
    global brcc
    global brno
    global mydb
    global count
    cc=remcc.get()
    if(cc not in brcc):
        PlaySound('a24.wav',SND_FILENAME)
        tkmsg.showinfo('productscode Invalid','Plese enter an existing productscode')
        return
    else:
        exe("DELETE FROM branch{} WHERE productscode={}".format(brno,cc))
        mydb.commit()
        PlaySound('a23.wav',SND_FILENAME)
        tkmsg.showinfo('Removed','The products is removed from branch{}'.format(brno))
        brcc.remove(cc)
        count-=1

def info():
        PlaySound('a25.wav',SND_FILENAME)
        import tkinter
        window=Tk()
        window.title('ABOUT US!')
        l1=tkinter.Label(window,text='Welcome to Turbotechies!',font=("Arial Bold",20)).pack()
        S='''

            THIS IS A SHOP MANAGEMENT PROJECT CREATED BY OUR TEAM CONSISTING OF AADIL ARSH.S.R , SHIBIL IRFAAN.I , SIDDHARTH
        RAMASAMY  FOR OUR GRADE 12 CP INVESTIGATORY PROJECT.
        IT IS AN INTERACTIVE OBJECT ORIENTED BUSINESS MANAGEMENT PROGRAM MADE USING TKINTER. IT ALLOWS THE SHOP OWNER
        TO CONTROL ,MANAGE AND SAVE TIME.WE HAVE ALSO ENABLE A  VOICE BEHIND CONTROL TO MAKE SURE WHAT BUTTON HAS BEEN
        CLICKED. PLS MAIL TO US OR GIVE FEEDBACK REGARDING OUR PROJECT AT OUR OFFICIAL WEBSITE! '''
        P='''

        EMAIL : turbotechies1@gmail.com
        WEBSITE : turbotechies.zohosites.in
        CONTACT INFO: 9443938329
        '''
        r='''
        THANK YOU!'''
        PlaySound('a26.wav',SND_FILENAME)
        l2=tkinter.Label(window,text=S,font=("Arial",15)).pack()
        l3=tkinter.Label(window,text=P,font=("Arial",15)).pack()
        l4=tkinter.Label(window,text=r,font=("Arial",15)).pack()
        window.mainloop()
            
def search():
   PlaySound('a27.wav',SND_FILENAME)
   global remcc
   remw=Tk()
   remw.title("Search")
   ccl=Label(remw,text="products")
   remcc=Entry(remw)
   okbtn=Button(remw,text="Search",command=sconfirm)

   ccl.grid(row=0,column=0)
   remcc.grid(row=0,column=1)
   okbtn.grid(row=1,column=1)

def sconfirm():
    global remcc
    global brno
    global mydb
    global count
    exe('USE products_service')
    viewwin = Tk()
    exe('SELECT * FROM branch' + str(brno))
    rawdata = mycursor.fetchall()
    brcc=[]
    for i in rawdata:
       brcc.append(str(i[0]))
    cc=remcc.get()
    if(cc not in brcc):
        PlaySound('a29.wav',SND_FILENAME)
        tkmsg.showinfo('Product Invalid','Plese enter an existing product')
        return
    else:
        PlaySound('a28.wav',SND_FILENAME)
        exe('USE products_service')
        exe("select * FROM branch{} WHERE products='{}'".format(brno,cc))    
        rawdat = mycursor.fetchall()
        viewwin = Tk()
        viewwin.title("search products")
        viewlab1 = Label(viewwin, text='Search Products')
        txt=Text(viewwin,height=20,width=60)
        txt.insert(INSERT,"('products','product no','Price per day','products-Code') \n")
        for i in rawdat:
            txt.insert(INSERT,str(i)+"\n")
        txt.config(state="disabled")

    viewlab1.pack()
    txt.pack()
    #viewlab2.pack()
    viewwin.mainloop()

def mini():
   PlaySound('a30.wav',SND_FILENAME)
   global remcc
   remw=Tk()
   remw.title("Search")
   ccl=Label(remw,text="Enter price:")
   remcc=Entry(remw)
   okbtn=Button(remw,text="Search",command=mconfirm)

   ccl.grid(row=0,column=0)
   remcc.grid(row=0,column=1)
   okbtn.grid(row=1,column=1)

def mconfirm():
    PlaySound('a31.wav',SND_FILENAME)
    global remcc
    global brno
    global mydb
    global count
    exe('USE products_service')
    viewwin = Tk()
    exe('SELECT * FROM branch' + str(brno))
    rawdata = mycursor.fetchall()
    brcc=[]
    for i in rawdata:
       brcc.append(int(i[2]))
    cc=remcc.get()
    exe('USE products_service')
    exe("select * FROM branch{} WHERE priceperday<={}".format(brno,cc))    
    rawdat = mycursor.fetchall()
    viewwin = Tk()
    viewwin.title("Min prices")
    viewlab1 = Label(viewwin, text='All Products of your range:')
    txt=Text(viewwin,height=20,width=60)
    txt.insert(INSERT,"('products','product no','Price per day','products-Code') \n")
    for i in rawdat:
        txt.insert(INSERT,str(i)+"\n")
    txt.config(state="disabled")

    viewlab1.pack()
    txt.pack()
    #viewlab2.pack()
    viewwin.mainloop()    

def addproducts():
    PlaySound('a21.wav',SND_FILENAME)
    global caservice
    global plte
    global ppde
    global cce
    adw=Tk()
    adw.title("Add products")
    productslab=Label(adw,text="products name")
    caservice=Entry(adw)
    pltl=Label(adw,text="Product No")
    plte=Entry(adw)
    ppdl=Label(adw,text="Price per day")
    ppde=Entry(adw)
    ccl=Label(adw,text="products-code")
    cce=Entry(adw)
    okbtn=Button(adw,text="Add products",command=addconfirm)

    productslab.grid(row=0,column=0)
    caservice.grid(row=0,column=1)
    pltl.grid(row=1,column=0)
    plte.grid(row=1,column=1)
    ppdl.grid(row=2,column=0)
    ppde.grid(row=2,column=1)
    ccl.grid(row=3,column=0)
    cce.grid(row=3,column=1)
    okbtn.grid(row=4,column=1)
    adw.mainloop()

def addconfirm():
    global caservice
    global plte
    global ppde
    global cce
    global brno
    global mydb
    global brcc
    global count
    exe("USE products_service")
    exe('SELECT * FROM branch' + str(brno))
    count=(len(mycursor.fetchall()))
    if (int(cce.get())<=count):
        PlaySound('a24.wav',SND_FILENAME)
        tkmsg.showinfo('Invalid products-code','The productscode has already been taken.\n please try a larger number')
        return
    else:
        try:
            exe("USE products_service")
            exe("""INSERT INTO branch{} VALUES
                ('{}','{}','{}','{}')""".format(brno,caservice.get().upper(),
                    plte.get().upper(),ppde.get(),cce.get()))
            mydb.commit()
            PlaySound('a18.wav',SND_FILENAME)
            tkmsg.showinfo('Done','products added to branch {}'.format(brno))
            brcc.append(cce.get())
            count+=1
        except mysql.connector.errors.DataError:
            PlaySound('a16.wav',SND_FILENAME)
            tkmsg.showinfo('Data Invalid','Please recheck data')

def feed():
    PlaySound('a17.wav',SND_FILENAME)
    global namee
    global feede
    global feedwin
    feedwin=Tk()
    feedwin.title("Feedback")
    feedwin.title("Feedback")
    namel=Label(feedwin,text="Name")
    namee=Entry(feedwin)
    feedl=Label(feedwin,text="Feedback:")
    feede=Text(feedwin)
    okbtn=Button(feedwin,text="OK",command=enterfeed)

    namel.grid(row=1,column=1)
    namee.grid(row=1,column=2)
    feedl.grid(row=2,column=1)
    feede.grid(row=3,column=2)
    okbtn.grid(row=5,column=2)

    feedwin.mainloop()

def enterfeed():
    PlaySound('a17.wav',SND_FILENAME)
    global namee
    global feede
    global mydb
    global mycursor
    feeddat=feede.get("1.0",END)
    namedat=namee.get()

    exe("USE products_service")
    exe("SELECT * FROM feedback")
    fl=mycursor.fetchall()
    if(fl==[]):
        count=1
    else:
        i=len(fl)-1
        count=(fl[i][0])+1

    today=datetime.date.today()
    d=today.strftime("%Y-%m-%d")
    try:
        exe("""INSERT INTO feedback VALUES
            ('{}','{}','{}','{}')""".format(count,namedat,d,feeddat))
        mydb.commit()
        PlaySound('a18.wav',SND_FILENAME)
        tkmsg.showinfo('Done','Thank you for your valuable feedback!')
        global feedwin
        feedwin.destroy()
    except mysql.connector.errors.DataError:
        PlaySound('a19.wav',SND_FILENAME)
        tkmsg.showinfo('Data Invalid','The feedback must be less than 300 charecters')

def viewfeed():
    PlaySound('a20.wav',SND_FILENAME)
    exe("USE products_service")
    exe("SELECT sno,name,date_written FROM feedback")
    dat=mycursor.fetchall()
    vfw=Tk()
    vfw.title("Feedbacks available")
    upframe=Frame(vfw)
    upframe.pack()
    dwframe=Frame(vfw)
    dwframe.pack(side=BOTTOM)

    txt=Text(upframe,height=20,width=50)
    txt.insert(INSERT,"('S-no','Name','Date Written')\n")
    for i in dat:
        txt.insert(INSERT,str(i)+"\n")
    txt.config(state="disabled")
    txt.pack()
    global snoent
    lab1=Label(dwframe,text="S-no to be viewed:")
    snoent=Entry(dwframe)
    okbtn=Button(dwframe,text="View",command=vf)
    lab1.grid(row=0,column=0)
    snoent.grid(row=0,column=1)
    okbtn.grid(row=1,column=1)

    vfw.mainloop()
    reset()

def vf():
    global snoent
    sno=snoent.get()
    global mycursor
    exe("USE products_service")
    exe("SELECT feedback FROM feedback WHERE sno={}".format(sno))
    f=mycursor.fetchall()
    vf=Tk()
    vf.title("View Feedback")
    txt=Text(vf,height=20,width=50)
    txt.insert(INSERT,str(f[0][0]))
    closebtn=Button(vf,text="close",command=vf.destroy)
    txt.pack()
    closebtn.pack()

def returnproducts():
    PlaySound('a37.wav',SND_FILENAME)
    global caservice
    returnwin=Tk()
    returnwin.title("Return serviceal")
    productslab=Label(returnwin,text='products-code')
    caservice=Entry(returnwin)
    quitbutton=Button(returnwin,text="Exit",command=returnwin.destroy)
    okaybutton=Button(returnwin,text='OK',command=returnconfirm)
    productslab.grid(row=1,column=1)
    caservice.grid(row=1,column=2)
    quitbutton.grid(row=2,column=1)
    okaybutton.grid(row=2,column=2)
    returnwin.mainloop()

def returnconfirm():
    global caservice
    global mydb
    global brno
    cc=caservice.get()
    exe('USE products_service')
    exe('SELECT * FROM active_serviceal')
    servicedata=mycursor.fetchall()
    print(servicedata)
    if(servicedata==[]):
        PlaySound('a11.wav',SND_FILENAME)
        tkmsg.showinfo('Error','No active services')
        return
    flag=0
    for i in servicedata:
        if(i[2]==str(cc)):
            flag+=1

            today=datetime.date.today()
            drt=today.strftime("%Y-%m-%d")
            drtc=datetime.datetime.strptime(drt,"%Y-%m-%d")
            brn=i[4]
            name=i[0]
            pno=i[1]
            drn=i[3]
            drnc=datetime.datetime.strptime(str(drn),"%Y-%m-%d") #str(datetime.date(2019,8,20)) for example purpose
            dt=drtc-drnc
            d=dt.days


            exe("SELECT * FROM temp WHERE productscode={}".format(cc))
            data=mycursor.fetchall()[0]
            products=data[0]
            no=data[1]
            ppd=data[2]
            pp=int(ppd)

            global l
            l=[name,pno,cc,drn,brn,drt,brno,pp,products,no,ppd]


            retcon= Tk()
            retcon.title('Return information')
            upframe=Frame(retcon)
            upframe.pack()
            dwframe=Frame(retcon)
            dwframe.pack(side=BOTTOM)
            namel=Label(upframe,text=("Name: "+str(name)))
            pnol=Label(upframe,text=("Phone-no: "+str(pno)))
            productsl=Label(upframe,text=("products: "+str(products)))
            nol=Label(upframe,text=("Lisence-no: "+str(no)))
            brnl=Label(upframe,text=("Branch serviced: Branch"+str(brn)))
            brtl=Label(upframe,text=("Branch returned: Branch"+str(brno)))
            drnl=Label(upframe,text=("Date serviced: "+str(drn)))
            drtl=Label(upframe,text=("Date returnrd: "+str(drt)))
            dtl=Label(upframe,text=("Price to be paid: "+str(pp)+"Rs"))
            okbutton=Button(dwframe,text='Confirm',command=rtc)
            cancelbutton=Button(dwframe,text='Cancel',command=retcon.destroy)

            namel.pack()
            pnol.pack()
            productsl.pack()
            nol.pack()
            brnl.pack()
            brtl.pack()
            drnl.pack()
            drtl.pack()
            dtl.pack()

            cancelbutton.grid(row=1,column=1)
            okbutton.grid(row=1,column=2)

            retcon.mainloop()

    if(flag==0):
        PlaySound('a16.wav',SND_FILENAME)
        tkmsg.showinfo('Wrong data','Please verify products-Code')

def rtc():
    global l
    global mydb
    exe("DELETE FROM active_serviceal WHERE productscode={}".format(l[2]))
    exe("""INSERT INTO customer_record VALUES
        ('{}','{}','{}','{}','{}','{}','{}','{}'
         )""".format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7]))
    exe("""INSERT INTO branch{} VALUES
        ('{}','{}','{}','{}')""".format(l[6],l[8],l[9],l[10],l[2]))
    mydb.commit()
    PlaySound('a12.wav',SND_FILENAME)
    tkmsg.showinfo('Success','products returned successfully')

def exitfun():
    PlaySound('a32.wav',SND_FILENAME)
    global mycursor
    global homewin
    exe('drop database products_service')
    homewin.destroy()
    mycursor.close()

def view():
    PlaySound('a8.wav',SND_FILENAME)
    # Tkinter productss available window
    exe('USE products_service')
    viewwin = Tk()
    viewwin.title("Available productss")
    viewlab1 = Label(viewwin, text='AVAILABLE productsS')
    #viewlab2 = Label(viewwin, text=data)
    txt=Text(viewwin,height=20,width=60)
    txt.insert(INSERT,"('products','product number','Price per day','products-Code') \n")
    global rawdata
    for i in rawdata:
        txt.insert(INSERT,str(i)+"\n")
    txt.config(state="disabled")

    viewlab1.pack()
    txt.pack()
    #viewlab2.pack()
    viewwin.mainloop()

def serviceview():
    PlaySound('a13.wav',SND_FILENAME)
    exe('USE products_service')
    service2=Tk()
    service2.title('View services')
    exe('SELECT * FROM active_serviceal')
    servicedata=mycursor.fetchall()
    fields=\
        """
('Name','Phone-no','products-Code','Date serviced','Branch serviced')

"""
    data=fields
    for i in servicedata:
        if i != len(servicedata) - 1:
            data += str(i) + '\n'

    viewlab1 = Label(service2, text='Active services')
    if (data==fields):
        PlaySound('a14.wav',SND_FILENAME) 
        viewlab2 = Label(service2, text="No active services")
    else:
         PlaySound('a15.wav',SND_FILENAME)
         viewlab2 = Label(service2, text=data)

    viewlab1.pack()
    viewlab2.pack()
    service2.mainloop()

def service():
    PlaySound('a9.wav',SND_FILENAME)
    global rname
    global rpno
    global rproductscode
    global servicewin

    # Tkinter serviced productss window

    exe('USE products_service')
    servicewin = Tk()
    servicewin.title("service products")

    titlelab=Label(servicewin,text="PLEASE ENTER THE REQUIRED DATA")

    namelab=Label(servicewin,text="Name ")
    pnolab=Label(servicewin,text="Phone-Number ")
    productscodelab=Label(servicewin,text="products-Code ")

    rname=Entry(servicewin)
    rpno=Entry(servicewin)
    rproductscode=Entry(servicewin)

    enterbutton=Button(servicewin,text="confirm",command=serviceconfirm)
    exitbutton=Button(servicewin,text="close",command=servicewin.destroy)

    titlelab.grid(row=1,column=1)

    namelab.grid(row=2,column=1)
    rname.grid(row=2,column=2)

    pnolab.grid(row=3,column=1)
    rpno.grid(row=3,column=2)

    productscodelab.grid(row=4,column=1)
    rproductscode.grid(row=4,column=2)

    enterbutton.grid(row=5,column=2)
    exitbutton.grid(row=5,column=1)

    servicewin.mainloop()

def serviceconfirm():
    global rname
    global rpno
    global rproductscode
    global servicewin
    global brcc
    global mycursor
    global brno

    if(rproductscode.get() not in brcc):
        PlaySound('a10.wav',SND_FILENAME)
        tkmsg.showinfo('Wrong products-code','Please enter a valid productscode')
        return
    try:

        exe("SELECT * FROM branch{} WHERE productscode='{}'".format(brno,rproductscode.get()))
        templ=mycursor.fetchall()
        t=templ[0]
        exe("INSERT INTO temp VALUES('{}','{}','{}','{}')".format(t[0],t[1],t[2],t[3]))
        exe("DELETE FROM branch{} WHERE productscode='{}'".format(brno,rproductscode.get()))
        today=datetime.date.today()
        exe("""INSERT INTO active_serviceal VALUES
            ('{}','{}','{}','{}','{}')""".format(rname.get(),rpno.get(),rproductscode.get()
            ,today.strftime("%Y-%m-%d"),brno))

        mydb.commit()
    except mysql.connector.errors.DataError:
        tkmsg.showinfo('Error','Please recheck data')
        PlaySound('a11.wav',SND_FILENAME)
        return
    PlaySound('a12.wav',SND_FILENAME)
    tkmsg.showinfo('Success','The requested products has been serviced successfully')


def initialize():
    PlaySound('a5.wav',SND_FILENAME)
    global mycursor
    exe('drop database if exists products_service')
    # Tkinter function for initializing databases

    try:
        exe('CREATE DATABASE products_service')
        exe('USE products_service')

        # CREATING TABLE AND INSERTING DATA FOR BRANCH 1

        ctable("""branch1(products varchar(40),prodno  varchar(10),
                          priceperday varchar(10),
                          productscode varchar(3) PRIMARY KEY)""")
        exe("""INSERT INTO branch1 VALUES
            ('WINDOWS INSTALLATION','W6363',800,1)""")
        exe("""INSERT INTO branch1 VALUES
            ('MAC INSTALLATION','A1234',800,2)""")
        exe("""INSERT INTO branch1 VALUES
            ('LINUX INSTALLATION','T5342',700,3)""")
        exe("""INSERT INTO branch1 VALUES
            ('ANTI-VIRUS INSTALLATION','W6090',800,4)""")
        exe("""INSERT INTO branch1 VALUES
            ('SOFTWARE INSTALLATION','N2435',200,5)""")
        exe("""INSERT INTO branch1 VALUES
            ('LAPTOP RENTAL','S9087',1200,6)""")
        exe("""INSERT INTO branch1 VALUES
            ('PC RENTAL','P3922',1500,7)""")
        exe("""INSERT INTO branch1 VALUES
            ('PROJECTOR RENTAL','K9354',600,8)""")
        exe("""INSERT INTO branch1 VALUES
            ('PRINTER RENTAL','B6879',500,9)""")
        exe("""INSERT INTO branch1 VALUES
            ('WIFI RENTAL','Z5342',100,10)""")
        exe("""INSERT INTO branch1 VALUES
            ('3D-printer RENTAL','F5432',1000,11)""")


        # APPLYING CHANGES

        mydb.commit()

        # CREATING AND INSERTING DATA FOR BRANCH 2

        ctable("""branch2(products varchar(40),prodno  varchar(10),
                        priceperday varchar(10),
                        productscode varchar(3) PRIMARY KEY)""")
        exe("""INSERT INTO branch2 VALUES
            ('PYTHON COURSE','D2090',150,12)""")
        exe("""INSERT INTO branch2 VALUES
            ('SCRATCH COURSE','W4090',250,13)""")
        exe("""INSERT INTO branch2 VALUES
            ('ARDUINO COURSE','D5989',200,14)""")
        exe("""INSERT INTO branch2 VALUES
            ('RASPBERRY PI COURSE','A4098',400,15)""")
        exe("""INSERT INTO branch2 VALUES
            ('ADOBE COURSE','T5873',200,16)""")
        exe("""INSERT INTO branch2 VALUES
            ('PHOTOSHOP COURSE','E4832',100,17)""")
        exe("""INSERT INTO branch2 VALUES
            ('AFTER EFFECTS COURSE','E3982',200,18)""")
        exe("""INSERT INTO branch2 VALUES
            ('JAVA COURSE','F3948',100,19)""")
        exe("""INSERT INTO branch2 VALUES
            ('WEBSITE AND LOGO MAKING COURSE','W5080',350,20)""")
        exe("""INSERT INTO branch2 VALUES
            ('RAINMETER COURSE','D2039',100,21)""")
        exe("""INSERT INTO branch2 VALUES
            ('AI COURSE','R3094',450,22)""")

        # APPLYING CHANGES

        mydb.commit()

        # CREATING AND INSERTING DATA FOR BRANCH 3

        ctable("""branch3(products varchar(40),prodno  varchar(10),
                        priceperday varchar(10),
                        productscode varchar(3) PRIMARY KEY)""")

        exe("""INSERT INTO branch3 VALUES
            ('PC SERVICE','R4978',1200,23)""")
        exe("""INSERT INTO branch3 VALUES
            ('LAPTOP SERVICE','R3984',1100,24)""")
        exe("""INSERT INTO branch3 VALUES
            ('PRINTER SERVICE','W0987',800,25)""")
        exe("""INSERT INTO branch3 VALUES
            ('MICROPHONE SERVICE','W0987',400,26)""")
        exe("""INSERT INTO branch3 VALUES
            ('WEBCAM SERVICE','S3098',200,27)""")
        exe("""INSERT INTO branch3 VALUES
            ('3D-PRINTER SERVICE','TN48GH3980',1000,28)""")
        exe("""INSERT INTO branch3 VALUES
            ('DUSTING AND CLEANING SERVICE','O2349',200,29)""")
        exe("""INSERT INTO branch3 VALUES
            ('PROJECTOR SERVICE','R3087',500,30)""")
        exe("""INSERT INTO branch3 VALUES
            ('SPEAKER SERVICE','TN49ES0978',200,31)""")
        exe("""INSERT INTO branch3 VALUES
            ('SCANNER SERVICE','I2987',350,32)""")
        exe("""INSERT INTO branch3 VALUES
            ('HARDWARE SERVICE','F3088',450,33)""")
        exe("""INSERT INTO branch3 VALUES
            ('TELEVISION SERVICE','D0987',100,34)""")
        exe("""INSERT INTO branch3 VALUES
            ('PC UPS SERVICE','D0878',200,35)""")
        mydb.commit()

        # CREATING AND INSERTING DATA FOR BRANCH 4

        ctable("""branch4(products varchar(40),prodno  varchar(10),
                        priceperday varchar(10),
                        productscode varchar(3) PRIMARY KEY)""")
        exe("""INSERT INTO branch4 VALUES
            ('PC-LG','P4347',56000,36)""")
        exe("""INSERT INTO branch4 VALUES
            ('PC-DELL','P4348',60000,37)""")
        exe("""INSERT INTO branch4 VALUES
            ('PC-LOGITECH','P4349',57500,38)""")
        exe("""INSERT INTO branch4 VALUES
            ('PC-ZEBRONICS','P4350',52000,39)""")
        exe("""INSERT INTO branch4 VALUES
            ('LAPTOP-HP','M5543',43000,40)""")
        exe("""INSERT INTO branch4 VALUES
            ('LAPTOP-DELL','M5544',55000,41)""")
        exe("""INSERT INTO branch4 VALUES
            ('LAPTOP-ACER','M5545',32000,42)""")
        exe("""INSERT INTO branch4 VALUES
            ('PRINTER-EPSON','G5432',24000,43)""")
        exe("""INSERT INTO branch4 VALUES
            ('PRINTER-CANON','G5433',22000,44)""")
        exe("""INSERT INTO branch4 VALUES
            ('MICROPHONE-INTEX','W6090',600,45)""")
        exe("""INSERT INTO branch4 VALUES
            ('WEBCAM-INTEX','N2435',1800,46)""")
        exe("""INSERT INTO branch4 VALUES
            ('3D-PRINTER-GRAPHIX','T6689',140000,47)""")
        exe("""INSERT INTO branch4 VALUES
            ('PROJECTOR-EPSON','P3872',11000,48)""")
        exe("""INSERT INTO branch4 VALUES
            ('PROJECTOR-SONY','P3873',12500,49)""")
        exe("""INSERT INTO branch4 VALUES
            ('SPEAKER-LOGITCH','K7654',2000,50)""")
        exe("""INSERT INTO branch4 VALUES
            ('SCANNER-ZEBRONICS','B6987',23000,51)""")
        exe("""INSERT INTO branch4 VALUES
            ('MONITOR-LG','Z5756',10000,52)""")
        exe("""INSERT INTO branch4 VALUES
            ('MONITOR-DELL','Z5757',11000,53)""")
        exe("""INSERT INTO branch4 VALUES
            ('MONITOR-ACER','Z5758',350,54)""")
        exe("""INSERT INTO branch4 VALUES
            ('MOUSE-ZEBRONICS','F5454',300,55)""")
        exe("""INSERT INTO branch4 VALUES
            ('MOUSE-DELL','F5455',400,56)""")
        exe("""INSERT INTO branch4 VALUES
            ('MOUSE-LOGITECH','F5456',80000,57)""")
        exe("""INSERT INTO branch4 VALUES
            ('KEYBOARD-ZEBRONICS','R9943',900,58)""")
        exe("""INSERT INTO branch4 VALUES
            ('KEYBOARD-DELL','R9944',1000,59)""")
        exe("""INSERT INTO branch4 VALUES
            ('KEYBOARD-LOGITECH','R9945',800,60)""")
        exe("""INSERT INTO branch4 VALUES
            ('UPS-NUMERIC','Y6654',9000,61)""")
        exe("""INSERT INTO branch4 VALUES
            ('HEADPHONE-SONY','Y6655',5000,62)""")
        exe("""INSERT INTO branch4 VALUES
            ('HEADPHONE-INTEX','Y6656',4000,63)""")
        exe("""INSERT INTO branch4 VALUES
            ('HEADPHONE-BELL','Y6657',3400,64)""")
        exe("""INSERT INTO branch4 VALUES
            ('PENDRIVE-SONY-32GB','Y6658',2500,65)""")
        exe("""INSERT INTO branch4 VALUES
            ('PENDRIVE-SANDISK-84GB','Y6659',3000,66)""")
        exe("""INSERT INTO branch4 VALUES
            ('PENDRIVE-TRANSCEND-16GB','Y6660',1500,67)""")
        mydb.commit()

        ctable("""active_serviceal(name varchar(30) NOT NULL UNIQUE ,
                                phone_no varchar(10) NOT NULL UNIQUE,
                                productscode varchar(3) NOT NULL UNIQUE,
                                date_serviced date NOT NULL ,
                                branch_serviced varchar(10) NOT NULL)""")

        ctable("""temp(products varchar(40),prodno  varchar(10),
                        priceperday varchar(10),
                        productscode varchar(3) PRIMARY KEY)""")

        # CREATING CUSTOMER DATA TABLE

        ctable("""customer_record(name varchar(30), phone_no varchar(10),
                                productscode varchar(3), date_serviced date,
                                branch_serviced varchar(10), date_returned date,
                                branch_returned varchar(10),
                                price_paid varchar(20))""")

        # CREATING A TABLE FOR STORING CUSTOMER FEEDBACK
        ctable("""feedback(sno int,name varchar(30) NOT NULL,date_written date,
                           feedback varchar(300) NOT NULL)""")

        PlaySound('a7.wav',SND_FILENAME)
        tkmsg.showinfo('Initialization Successfull',
                       'The required database and tables have been initialized successfully')

        global rawdata
        global brcc
        exe('USE products_service')
        exe('SELECT * FROM branch' + str(brno))
        rawdata = mycursor.fetchall()
        brcc=[]
        for i in rawdata:
           brcc.append(str(i[3]))
    except mysql.connector.errors.DatabaseError:
        PlaySound('a6.wav',SND_FILENAME)
        tkmsg.showinfo('initialization',
                       'The database has already been initialized')


brno = 0
r = Tk()
r.title("Login")

upframe = Frame(r)
upframe.pack()

dwframe = Frame(r)
dwframe.pack(side=BOTTOM)

username = StringVar()
password = StringVar()

unlabel = Label(upframe, text='Username')
unentry = Entry(upframe, textvariable=username)
unlabel.grid(row=0, column=0)
unentry.grid(row=0, column=1)

passlabel = Label(upframe, text='Password')
passentry = Entry(upframe, textvariable=password)
passlabel.grid(row=1, column=0)
passentry.grid(row=1, column=1)

rlab = Label(dwframe, text='''

Select Branch number''')

rawbn=IntVar()
rch1 = Radiobutton(dwframe, text='Branch-1', variable=rawbn,value=1)
rch2 = Radiobutton(dwframe, text='Branch-2', variable=rawbn,value=2)
rch3 = Radiobutton(dwframe, text='Branch-3', variable=rawbn,value=3)
rch4 = Radiobutton(dwframe, text='Branch-4', variable=rawbn,value=4)
beg = Button(dwframe, text='Connect to SQL', command=home)
rlab.pack()
rch1.pack()
rch2.pack()
rch3.pack()
rch4.pack()
beg.pack()
departmentstoresbutton=Button(dwframe,text='DEPARTMENT STORES',command=store,bg='red',fg='white',width='5',height='3')
snacksbutton=Button(dwframe,text='SNACKS COUNTER',command=snack,bg='green',fg='white',width='5',height='3')
speechbutton=Button(dwframe,text='JUST SPEAK(*<*)',command=speak,bg='blue',fg='white',width='5',height='3')
moviebutton=Button(dwframe,text='MOVIE BOOKING',command=movie,bg='violet',fg='white',width='5',height='3')
bookshopbutton=Button(dwframe,text='BOOK SHOP',command=book,bg='yellow',fg='black',width='5',height='3')
departmentstoresbutton.pack(fill=X)
snacksbutton.pack(fill=X)
speechbutton.pack(fill=X)
moviebutton.pack(fill=X)
bookshopbutton.pack(fill=X)
r.mainloop()


