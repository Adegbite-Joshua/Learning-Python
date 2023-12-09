from tkinter import *

window = Tk() # Instantiate an instance of a window
window.geometry('500x500')
window.title('PROADE CODE')

icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background='black')

photo = PhotoImage(file='logo.png')

label = Label(window,
              text='Hello World', 
              font=('Arial', 40, 'bold'), 
              fg='green', 
              bg='red', 
              relief=RAISED,
              bd=10,
              padx=10,
              pady=20,
            #   image=photo,
            #   compound='bottom',
              )
# label.place(x=0, y=0)
# label.pack()
# label.config(background='red')

count  = 0
def click():
    global count 
    count += 1
    print(count)

button = Button(window, 
                text='Click',
                command=click,
                font=('Comic Sans', 30),
                fg='green',
                activeforeground='green',
                activebackground='gold',
                state=ACTIVE,
                # image=photo,
                # compound='top'
                )
# button.pack()



window.mainloop() # Place window on a computer screen, listen for event
