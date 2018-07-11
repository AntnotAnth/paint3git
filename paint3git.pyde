def setup():
    size (500, 450)
    global Red, Green, Blue 
    background(255, 255, 255)
    fill(255, 0, 0) #red
    rect (5, 1, 50, 50, 8)
    fill( 0, 255, 0) #green
    rect( 5, 60, 50, 50, 8)
    fill(0, 0, 255) #blue
    rect(5, 120, 50, 50, 8)
    stroke(0, 0, 0)
    line(50, 450, 50, 110)

def draw():
    Red > 1
    Blue > 120
    Green > 60

    if mousePressed:
       stroke(0, 0, 255)
       line(pmouseX, pmouseY, mouseX, mouseY)
    

     
def mouseClicked():
    stroke (255, 40, 30)
    #if mouseClicked(Red):
        #stroke( 255, 0, 0) 
