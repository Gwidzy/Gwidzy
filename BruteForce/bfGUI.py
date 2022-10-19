from Tkinter import *

# bfm = bruteForceMain = main window object
bfm = Tk(className='Login')
bfm.configure(bg='white')

# can = canvas = for layout/graphics/text/widgets
#can = Canvas(bfm, width=40, height=30, bg='white', bd=3)
#l1 = Label(bfm, text='Enter Username:').grid(row=0)
#l2 = Label(bfm, text='Enter Password:').grid(row=1)
#e1 = Entry(bfm)
#e2 = Entry(bfm)
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
#can.pack()

menu = Menu(bfm)

bfm.configure(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Option', menu=filemenu)
filemenu.add_command(label='About')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=bfm.quit)


# widgets are added below:
bfm.title('Totally safe')

print("Running...")
mainloop()
# can = canvas = for layout/graphics/text/widgets
#can = Canvas(bfm, width=40, height=30, bg='white', bd=3)
#can.pack()

#l1 = Label(bfm, text='Enter Username:').grid(row=0)
#l2 = Label(bfm, text='Enter Password:').grid(row=1)
#e1 = Entry(bfm)
#e2 = Entry(bfm)
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

#mainloop()

# mainloop()

#butt = Button(bfm, text='Submit', width=30, height=10, command=bfm.destroy)
#butt.pack()



print("Success!")

