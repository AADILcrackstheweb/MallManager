import pygame
from playsound import playsound
import pyaudio
import speech_recognition as sr
from pygame import mixer
import speekmodule
l=[]
t=0
i=0
n=0
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)     
        print("PLS SAY ITEMS ONE-BY-ONE!")
        audio = r.listen(source)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)
 
        if ('apple') in message:                          
            l.append('apple')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=250*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('bannana') in message:                          
            l.append('apple')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in number's:"))
            l.append(q)
            l.append('no.')
            c=15*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('mango') in message:                          
            l.append('mango')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=50*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('watermelon') in message:                          
            l.append('watermelon')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=25*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('orange') in message:                          
            l.append('orange')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=40*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('papaya') in message:                          
            l.append('papaya')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=90*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('jack fruit') in message:                          
            l.append('jack fruit')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=185*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('pineapple') in message:                          
            l.append('pineapple')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=90*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('sapota') in message:                          
            l.append('sapota')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=90*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('grapes') in message:                          
            l.append('grapes')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=80*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('beans') in message:                          
            l.append('beans')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=75*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('beetroot') in message:                          
            l.append('beetroot')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=18*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('brinjal') in message:                          
            l.append('brinjal')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=30*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('bitterguourd') in message:                          
            l.append('bittergourd')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=15*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('cabbage') in message:                          
            l.append('cabbage')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=20*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('capsicum') in message:                          
            l.append('capsicum')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=30*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('carrot') in message:                          
            l.append('carrot')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=15*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('cauliflower') in message:                          
            l.append('cauliflower')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=20*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('coconut') in message:                          
            l.append('coconut')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=30*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('garlic') in message:                          
            l.append('garlic')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=120*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('drumstick') in message:                          
            l.append('drumstick')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=10*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('bottlegourd') in message:                          
            l.append('bottlegourd')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=25*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('ginger') in message:                          
            l.append('apple')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=60*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('ladies finger') in message:                          
            l.append('ladies finger')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=15*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('onion') in message:                          
            l.append('onion')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=30*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('greenchilli') in message:                          
            l.append('greenchilli')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=12*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('sunflower oil') in message:                          
            l.append('sunflower oil')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=150*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('maggie noodles') in message:                          
            l.append('maggie noodles')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=30*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')
        if ('rock salt') in message:                          

            l.append('rock salt')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=50*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('pepper') in message:                          
            l.append('pepper')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=250*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')
        if ('urad dal') in message:                          

            l.append('urad dal')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=40*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('coconut oil') in message:                          
            l.append('coconut oil')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=300*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('groundnut oil') in message:                          
            l.append('groundnut oil')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=250*q #price of item
            t+=c
            l.append(c)

        if ('turmeric') in message:                          
            l.append('turmeric')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=70*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('tamarind') in message:                          
            l.append('tamarind')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=200*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('agar') in message:                          
            l.append('agar')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=35*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')            

        if ('jam') in message:                          
            l.append('jam')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=87*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')            

        if ('sauce') in message:                          
            l.append('sauce')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=40*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('biscuit') in message:                          
            l.append('biscuit')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=60*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('bread') in message:                          
            l.append('bread')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=36*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('chocolate') in message:                          
            l.append('chocolate')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=135*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')

        if ('egg') in message:                          
            l.append('egg')
            rand = ['please enter the quantity sir!']
            speekmodule.speek(rand,n,mixer)
            q=float(input("enter quantity in kg's:"))
            l.append(q)
            l.append('kgs')
            c=95*q #price of item
            t+=c
            l.append(c)
            l.append('rupees')
            
        if ('bil' or 'bill') in message:
            print(l)
            d=str(l)
            rand =['your bill is'+d]
            speekmodule.speek(rand,n,mixer)

        if ('total') in message:
            g=str(t)
            rand =[g+'rupees'+'to continue press enter'+'to exit say exit']
            speekmodule.speek(rand,n,mixer)
            print(t,' rupees')
          

        if ('exit') in message:                          
            rand = ['Thank you for shopping in turbo techies'+'powering off in 3, 2, 1, 0']
            speekmodule.speek(rand,n,mixer)
            break
            quit()
            
    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
            
