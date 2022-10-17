import tkinter
window=tkinter.Tk()
window.title('ABOUT US!')
i=tkinter.PhotoImage(file="MYLOGO.png")
label=tkinter.Label(window,image=i)
label.pack()
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
l2=tkinter.Label(window,text=S,font=("Arial",15)).pack()
l3=tkinter.Label(window,text=P,font=("Arial",15)).pack()
l4=tkinter.Label(window,text=r,font=("Arial",15)).pack()
window.mainloop()
