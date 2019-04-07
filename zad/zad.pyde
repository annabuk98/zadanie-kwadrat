def setup():
    rectMode(RADIUS)
    size(500,500)
    noStroke()
    fill(random(255), random(255), random(255), random(255))
    global rectSize
    rectSize = 55
    global x
    x = rectSize
    global y
    y = height/2
    background(200,10,125)
def draw():
    global rectSize
    global x
    global y
    fill(random(255), random(255), random(255), random(255))
    rect(x,y,rectSize,rectSize)
    global x
    global y
    x+=5
    y+=5
    if x > (width/2)-rectSize/2:
        noLoop()
    else:
        loop()

   
