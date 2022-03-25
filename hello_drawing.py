from PIL import Image, ImageDraw
def image_with_line(x1,y1,x2,y2,filename):
    img = Image.new("RGB", (500, 300), (255,255,255))  # create new Image
    ctx = ImageDraw.Draw(img)  # create drawing context
    ctx.line((x1,y1,x2,y2), fill="black")
    del ctx  # destroy drawing context

    img.save('drawing1/' + filename + '.png')

for i in range(10):
    image_with_line(7*i,2,130-10*i,180,'hello_drawing' + str(i))