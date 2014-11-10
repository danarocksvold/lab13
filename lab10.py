##########################################
# #
# Draw a house! #
# #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600)
drawpad.grid(row=0, column=1)


#roof outline

line1 = drawpad.create_line(50,150,710,150)
line2 = drawpad.create_line(50,150,90,50)
line3 = drawpad.create_line(90,50,670,50)
line4 = drawpad.create_line(670,50,710,150)
#house outline

house1 = drawpad.create_rectangle(80,150,670,510, fill = 'red')

#windows
window1 = drawpad.create_rectangle(120,180,300,280, fill = 'gray')
window2 = drawpad.create_rectangle(460,180,650,280, fill = 'gray')
window3 = drawpad.create_rectangle(120,360,300,460, fill = 'gray')
window4 = drawpad.create_rectangle(460,360,650,460, fill = 'gray')
window1line = drawpad.create_line(120,230,300,230)
window2line = drawpad.create_line(460,230,650,230)
window3line = drawpad.create_line(120,410,300,410)
window4line = drawpad.create_line(460,410,650,410)
window5line = drawpad.create_line(220,180,220,280)
window6line = drawpad.create_line(220,360,220,460)
window7line = drawpad.create_line(560,180,560,280)
window8line = drawpad.create_line(560,360,560,460)
#door

door = drawpad.create_rectangle(320,360,440,510)

#90pt
doorhandle = drawpad.create_oval(390,420,420,450, fill = 'gray')

chimney = drawpad.create_rectangle(520,10,610,80, fill = 'gray')

#100pt
grass = drawpad.create_rectangle(0,510,800,600, fill = 'green')

root.mainloop()