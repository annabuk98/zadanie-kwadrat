def setup():
    rectMode(RADIUS)
    size(500,500)
    noStroke()
    fill(random(255), random(255), random(255), random(255))
    global x
    x = 50
    global y
    y = 250
    background(200,10,125)
def draw():
    global x
    global y
    fill(random(255), random(255), random(255), random(255))
    rect(x,y,55,55)
    global x
    global y
    x+=5
    y+=5
    if x > (width/2)-20:
        noLoop()
    else:
        loop()

   
