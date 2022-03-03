#Kaylee Petek
#CS61002 Algorithms and Programming I
#Lab 07
#November 7, 2021

#A pgrogram to move a ball left, right, up, and down

#import tkinter
from tkinter import *

#create a class to move a ball on a screen
class moveBall:
    def __init__ (self):
        self.root = Tk () #constructs root window
        self.root.title("Moving Ball") #Create a title
        self.root.resizable (False, False) #size cannot be changed

        self.width=300 #create a width variable
        self.height=300 #create a height variable
        self.canvas = Canvas (self.root, width=self.width, height=self.height) #create the canvas
        self.canvas.pack() #display the canvas

        frame = Frame(self.root) #create the frame
        frame.pack() #display the frame

        self.canvas.create_rectangle(10,10,290,290) #create a border

        x1=self.width/2 #create coordinate variable for x1
        y1=self.height/2 #create coordinate variable for y1
        x2=x1+10 #create coordinate variable for x2
        y2=y1+10 #create coordinate variable for y2
        self.ball = self.canvas.create_oval(x1,y1,x2,y2, fill="red") #create a ball
                 
        btLeft = Button (frame, text = ("Left"), command = self.moveBallLeft) #create a left button that moves the ball left
        btRight = Button (frame, text = ("Right"), command = self.moveBallRight) #create a right button to move the ball right
        btUp = Button (frame, text = ("Up"), command = self.moveBallUp) #create an up button to move the ball up
        btDown = Button (frame, text = ("Down"), command = self.moveBallDown) #create a down button to move the ball down

        btLeft.pack(side=LEFT) #display the left button on the left side
        btRight.pack(side=RIGHT) #display the right button on the right side
        btUp.pack() #display the up button above the down button
        btDown.pack() #display the down button below the up button

        self.root.mainloop() #enters a game loop
        
    #create a function to move the ball left
    def moveBallLeft (self):
        left, top, right, bottom = self.canvas.coords(self.ball) #obtain coordinates of the ball
        if left <= 10: #if the ball reaches an x coordinate of 10 or less
            x = 0 #do not move further on the x, x becomes 0
        else: # if the x coordinate is greater than 10
            x=-10 #move to the left 10 spaces
        y=0 #no change in y
        self.canvas.move(self.ball, x, y) #move the ball

        
    #create a function to move the ball right    
    def moveBallRight (self):
        left, top, right, bottom = self.canvas.coords(self.ball) #obtain coordinates of the ball
        if right>=290: #if the ball reaches an x coordinate of 290 or more
            x = 0 #do not move the ball further (it reached the boundary)
        else: #else the x coordinate is less than 290
            x= 10 #change the x coordinate by 10 to the right
        y=0 #no change in y
        self.canvas.move (self.ball, x, y) #move the ball

        
    #create a function to move the ball up    
    def moveBallUp (self):
        left, top, right, bottom = self.canvas.coords(self.ball) #obtain the coordinates
        if top<=10: #if the ball reaches a y coordinate of 10 or less
            y = 0 #do not move the ball (it reached the boundary)
        else: #else the ball has a y coordinate of more than 10
            y=-10 #change the y coordiante by 10 up
        x=0 #no change in x
        self.canvas.move(self.ball, x, y) #move the ball up
        
    #create a function to move the ball down
    def moveBallDown(self):
        left, top, right, bottom = self.canvas.coords(self.ball) #obtain the coordinates of the ball
        if bottom>=290: #if the ball reaches a y coordinate of 290 or more
            y = 0 #do not change y (it reached the boundary)
        else: #else the ball has a y coordinate of less than 290
            y=10 #change the y coordinate by 10 down
        x=0 #no change in x
        self.canvas.move (self.ball, x, y) #move the ball down
        


#call the class
moveBall()

