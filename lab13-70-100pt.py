#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")
enemy1 = drawpad.create_rectangle(290,180,330,200, fill="blue")
enemy2 = drawpad.create_rectangle(490,380,530,400, fill="blue")
enemy3 = drawpad.create_rectangle(390,280,430,300, fill="blue")
# Create your "enemies" here, before the class
direction = 1
direction2 = 2
direction3 = 2

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    

       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "orange")
       	    self.down.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "blue")
       	    self.right.grid(row=1,column=0)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "red")
       	    self.left.grid(row=1,column=1)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global enemy1
	    global direction
            global direction2
            global direction3
	    global enemy2
	    global enemy3
	    # Uncomment this when you're ready to test out your animation!
            x1, y1, x2, y2 = drawpad.coords(enemy1)
            if x2 > drawpad.winfo_width(): 
                    direction = - 5
            elif x1 < 0:
                    direction = 5
            drawpad.move(enemy1,direction,0)
            x1, y1, x2, y2 = drawpad.coords(enemy2)
            if x2 > drawpad.winfo_width(): 
                    direction2 = - 5
            elif x1 < 0:
                    direction2 = 5
            drawpad.move(enemy2,direction2,0)
            x1, y1, x2, y2 = drawpad.coords(enemy3)
            if x2 > drawpad.winfo_width(): 
                    direction3 = - 5
            elif x1 < 0:
                    direction3 = 5
            drawpad.move(enemy3,direction3,0)
	    drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
		
        def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	   
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
app = MyApp(root)
root.mainloop()