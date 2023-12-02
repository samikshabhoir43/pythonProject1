import tkinter
import random
import time

root = tkinter.Tk()
root.geometry("1500x700+0+0")
# root.resizable(0,0)
root.title("Restaurant Management System")

Tops = tkinter.Frame(root, bg="white", width = 1600, height=50, relief=tkinter.SUNKEN)
Tops.pack(side=tkinter.TOP)

f1 = tkinter.Frame(root, width = 900, height=700, relief=tkinter.SUNKEN)
f1.pack(side=tkinter.LEFT)
#
f2 = tkinter.Frame(root, width = 100, height=300, relief=tkinter.SUNKEN)
f2.pack(side=tkinter.RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = tkinter.Label(Tops, font=('aria' , 30, 'bold'), text="Restaurant Management System ", fg="steel blue", bd=10, anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = tkinter.Label(Tops, font=('aria' , 20,), text=localtime, fg="steel blue", anchor=tkinter.W)
lblinfo.grid(row=1,column=0)
#
#---------------Calculator------------------
text_Input=tkinter.StringVar()
operator =""

txtdisplay = tkinter.Entry(f2, font=('ariel' , 20, 'bold'), textvariable=text_Input, bd=5, insertwidth=7, bg="white", justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    # rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Cheese_burger.set("")


btn7=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="7", bg="powder blue", command=lambda: btnclick(7))
btn7.grid(row=2,column=0)

btn8=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="8", bg="powder blue", command=lambda: btnclick(8))
btn8.grid(row=2,column=1)

btn9=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="9", bg="powder blue", command=lambda: btnclick(9))
btn9.grid(row=2,column=2)

Addition=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 10 , 'bold'), text="+", bg="powder blue", command=lambda: btnclick("+"))
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="4", bg="powder blue", command=lambda: btnclick(4))
btn4.grid(row=3,column=0)

btn5=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="5", bg="powder blue", command=lambda: btnclick(5))
btn5.grid(row=3,column=1)

btn6=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="6", bg="powder blue", command=lambda: btnclick(6))
btn6.grid(row=3,column=2)

Substraction=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 10 , 'bold'), text="-", bg="powder blue", command=lambda: btnclick("-"))
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="1", bg="powder blue", command=lambda: btnclick(1))
btn1.grid(row=4,column=0)

btn2=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="2", bg="powder blue", command=lambda: btnclick(2))
btn2.grid(row=4,column=1)

btn3=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="3", bg="powder blue", command=lambda: btnclick(3))
btn3.grid(row=4,column=2)

multiply=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 10 , 'bold'), text="*", bg="powder blue", command=lambda: btnclick("*"))
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="0", bg="powder blue", command=lambda: btnclick(0))
btn0.grid(row=5,column=0)

btnc=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text="c", bg="powder blue", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=tkinter.Button(f2, padx=16, pady=16, bd=4, width = 16, fg="black", font=('ariel', 20 , 'bold'), text="=", bg="powder blue", command=eqals)
btnequal.grid(columnspan=4)

Decimal=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 20 , 'bold'), text=".", bg="powder blue", command=lambda: btnclick("."))
Decimal.grid(row=5,column=2)

Division=tkinter.Button(f2, padx=16, pady=16, bd=4, fg="black", font=('ariel', 10 , 'bold'), text="/", bg="powder blue", command=lambda: btnclick("/"))
Division.grid(row=5,column=3)
status = tkinter.Label(f2, font=('aria', 15, 'bold'), width = 16, text="-By samiksha", bd=2, relief=tkinter.SUNKEN)
status.grid(row=7,columnspan=3)

#---------------------------------------------------------------------------------------
rand = tkinter.StringVar()
Fries = tkinter.StringVar()
Largefries = tkinter.StringVar()
Burger = tkinter.StringVar()
Filet = tkinter.StringVar()
Subtotal = tkinter.StringVar()
Total = tkinter.StringVar()
Service_Charge = tkinter.StringVar()
Drinks = tkinter.StringVar()
Tax = tkinter.StringVar()
cost = tkinter.StringVar()
Cheese_burger = tkinter.StringVar()


lblreference = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Order No.", fg="steel blue", bd=10, anchor='w')
lblreference.grid(row=0,column=0)
txtreference = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtreference.grid(row=0,column=1)

lblfries = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Fries Meal", fg="steel blue", bd=10, anchor='w')
lblfries.grid(row=1,column=0)
txtfries = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Lunch Meal", fg="steel blue", bd=10, anchor='w')
lblLargefries.grid(row=2,column=0)
txtLargefries = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Largefries, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Burger Meal", fg="steel blue", bd=10, anchor='w')
lblburger.grid(row=3,column=0)
txtburger = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Burger, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtburger.grid(row=3,column=1)

lblFilet = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Pizza Meal", fg="steel blue", bd=10, anchor='w')
lblFilet.grid(row=4,column=0)
txtFilet = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtFilet.grid(row=4,column=1)

lblCheese_burger = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Cheese burger", fg="steel blue", bd=10, anchor='w')
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Cheese_burger, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Drinks", fg="steel blue", bd=10, anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtDrinks.grid(row=0,column=3)

lblcost = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="cost", fg="steel blue", bd=10, anchor='w')
lblcost.grid(row=1,column=2)
txtcost = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=cost, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Service Charge", fg="steel blue", bd=10, anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Tax", fg="steel blue", bd=10, anchor='w')
lblTax.grid(row=3,column=2)
txtTax = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Subtotal", fg="steel blue", bd=10, anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Subtotal, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = tkinter.Label(f1, font=('aria' , 16, 'bold'), text="Total", fg="steel blue", bd=10, anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = tkinter.Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="powder blue", justify='right')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = tkinter.Label(f1, text="---------------------", fg="white")
lblTotal.grid(row=6,columnspan=3)
#
btnTotal=tkinter.Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel' , 16, 'bold'), width=10, text="TOTAL", bg="powder blue", command=Ref)
btnTotal.grid(row=7, column=1)
#
btnreset=tkinter.Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel' , 16, 'bold'), width=10, text="RESET", bg="powder blue", command=reset)
btnreset.grid(row=7, column=2)

btnexit=tkinter.Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel' , 16, 'bold'), width=10, text="EXIT", bg="powder blue", command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = tkinter.Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=tkinter.W)
    lblinfo.grid(row=0, column=2)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=tkinter.W)
    lblinfo.grid(row=0, column=3)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=1, column=0)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=1, column=3)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=2, column=0)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=2, column=3)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=3, column=0)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=3, column=3)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=4, column=0)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=4, column=3)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=5, column=0)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=5, column=3)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=6, column=0)
    lblinfo = tkinter.Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=tkinter.W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()

btnprice=tkinter.Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel' , 16, 'bold'), width=10, text="PRICE", bg="powder blue", command=price)
btnprice.grid(row=7, column=0)

root.mainloop()