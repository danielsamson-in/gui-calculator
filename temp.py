from tkinter import * 
expression = ""  
def press(num):  
    global expression  
    expression = expression + str(num)  
    equation.set(expression)  
def equalpress():  
    try:  
        global expression  
        total = str(eval(expression))  
        equation.set(total)  
        expression = ""  
    except:  
        equation.set(" error ")  
        expression = ""  
def clear():  
    global expression  
    expression = ""  
    equation.set("") 

def multizero0():
    global expression
    expression = expression +str('00') 
    equation.set(expression) 
    
    
#Main
 
gui = Tk()  
gui.configure(background="white")  
gui.title("Calculator")  
gui.geometry("500x350")  
equation = StringVar()  
expression_field = Entry(gui,font=("Courier New",17,'bold'), textvariable=equation)  
expression_field.grid(columnspan=50, ipadx=70)  
equation.set("0") 

 
button0=Button(gui, text=' 0 ', fg='black', bg='light yellow',command=lambda: press(0),  height=2, width=8,font=("Courier New",16,'bold'))  
button0.grid(row=2, column=0)  

button1=Button(gui, text=' 1 ', fg='black', bg='light yellow', command=lambda: press(1),  height=2, width=8,font=("Courier New",16,'bold'))  
button1.grid(row=2, column=1) 
 
button2= Button(gui, text=' 2 ', fg='black', bg='light yellow', command=lambda: press(2),  height=2, width=8,font=("Courier New",16,'bold'))  
button2.grid(row=2, column=2) 

button3=Button(gui, text=' 3 ', fg='black', bg='light yellow',command=lambda: press(3),  height=2, width=8,font=("Courier New",16,'bold'))  
button3.grid(row=2, column=3)

 
button4=Button(gui, text=' 4 ', fg='black', bg='light yellow', command=lambda: press(4),  height=2, width=8,font=("Courier New",16,'bold'))  
button4.grid(row=3, column=0) 
 
button5=Button(gui, text=' 5 ', fg='black', bg='light yellow', command=lambda: press(5),  height=2, width=8,font=("Courier New",16,'bold'))  
button5.grid(row=3, column=1)  

button6=Button(gui, text=' 6 ', fg='black', bg='light yellow', command=lambda: press(6),  height=2, width=8,font=("Courier New",16,'bold'))  
button6.grid(row=3, column=2) 

button7=Button(gui, text=' 7 ', fg='black', bg='light yellow',command=lambda: press(7),  height=2, width=8,font=("Courier New",16,'bold'))  
button7.grid(row=3, column=3) 

button8=Button(gui, text=' 8 ', fg='black', bg='light yellow',command=lambda: press(8),  height=2, width=8,font=("Courier New",16,'bold'))  
button8.grid(row=4, column=0)  

button9=Button(gui, text=' 9 ', fg='black', bg='light yellow', command=lambda: press(9),  height=2, width=8,font=("Courier New",16,'bold'))  
button9.grid(row=4, column=1)  

decimal=Button(gui, text='.', fg='black', bg='light yellow',command=lambda: press("."),  height=2, width=8,font=("Courier New",16,'bold'))  
decimal.grid(row=4, column=2)


plus = Button(gui, text=' + ', fg='black', bg='dark orange', command=lambda: press("+"),  height=2, width=8,font=("Courier New",16,'bold'))  
plus.grid(row=4, column=3) 

minus = Button(gui, text=' - ', fg='black', bg='dark orange', command=lambda: press("-"),  height=2, width=8,font=("Courier New",16,'bold'))  
minus.grid(row=5, column=0)
 
multiply = Button(gui, text='X', fg='black', bg='dark orange', command=lambda:  press("*"), height=2, width=8,font=("Courier New",16,'bold'))  
multiply.grid(row=5, column=1) 

divide = Button(gui, text=' / ', fg='black', bg='dark orange',command=lambda:press("/"),  height=2, width=8,font=("Courier New",16,'bold'))  
divide.grid(row=5, column=2) 

equal = Button(gui, text=' = ', fg='black', bg='dark orange',command=equalpress,  height=2, width=8,font=("Courier New",16,'bold'))  
equal.grid(row=5, column=3) 

clear = Button(gui, text='Clear', fg='black', bg='red',command=clear, height=2,  width=8,font=("Courier New",16,'bold'))  
clear.grid(row=6, column=1) 

button00=Button(gui, text=' 00 ', fg='white', bg='black',command=multizero0,  height=2, width=8,font=("Courier New",16,'bold'))  
button00.grid(row=6, column=0) 
                        


 
reset = Button(gui, text='Reset', fg='black', bg='cyan',command=lambda: press(" "),  height=2, width=8,font=("Courier New",16,'bold'))  
reset.grid(row=6, column=2)
 
temp2 = Button(gui, text='', fg='black', bg='cyan',command=lambda: press(" "), height=2,  width=8,font=("Courier New",16,'bold'))  
temp2.grid(row=6, column=3) 

gui.mainloop() 
