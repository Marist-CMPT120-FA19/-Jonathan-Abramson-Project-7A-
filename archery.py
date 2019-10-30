from graphics import *
import math

def rad(point, dist):
    x=point.getX()-dist.getCenter().getX()
    y=point.getY()-dist.getCenter().getY()
    rad=math.sqrt(x*x+y*y)
    
    return rad <=dist.getRadius()
 
    
 
def main():
    score=0
    win=GraphWin("Bullseye")
    tan = Circle(Point(100,100), 70)
    tan.setOutline("tan")
    tan.setFill("tan")
    tan.draw(win)
    
    black = Circle(Point(100,100), 60)
    black.setOutline("black")
    black.setFill("black")
    black.draw(win)
    
    white = Circle(Point(100,100), 50)
    white.setOutline("white")
    white.setFill("white")
    white.draw(win)
    
    blue = Circle(Point(100,100), 40)
    blue.setOutline("blue")
    blue.setFill("blue")
    blue.draw(win)
    
    yellow = Circle(Point(100,100), 30)
    yellow.setOutline("yellow")
    yellow.setFill("yellow")
    yellow.draw(win)
    
    green = Circle(Point(100,100), 20)
    green.setOutline("green")
    green.setFill("green")
    green.draw(win)
    
    red = Circle(Point( 100,100), 10)
    red.setOutline("red")
    red.setFill("red")
    red.draw(win)

    message= Text(Point(100,10), "You have 5 clicks to shoot 5 arrows at the target.")
    message.draw(win)
           
    for i in range (5):
        p=win.getMouse()
                         
        if(rad(p, red)):
                score+=12       
        elif(rad(p, green)):
                score+=10                
        elif(rad(p, yellow)):
                score+=8                
        elif(rad(p, blue)):
                score+=6                
        elif(rad(p, white)):
                score+=4  
        elif(rad(p, tan)):
                score+=2                     
        else:
                score+=0
          
    message.setText("Your total score is: "+ str(score))
    win.getMouse()
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()
main()