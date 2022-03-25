from PIL import Image, ImageDraw
import random, math


class TileDrawer():
    def __init__(self,a_coord,b_coord,theta,ctx):
        self.a = a_coord
        self.b = b_coord
        self.theta = theta
        self.ctx = ctx

    def get_box(self,r,center):
        (x,y)=center
        return [(x-r,y-r),(x+r,y+r)]

    def draw(self):
        a = self.a
        b = self.b
        r = 25
        theta2 = (self.theta+45)*math.pi/180
        theta3 = (self.theta+225)*math.pi/180
        c = (50*a+25+2**0.5*r*math.cos(theta2),50*b+25+2**0.5*r*math.sin(theta2))
        c2 = (50*a+25+2**0.5*r*math.cos(theta3),50*b+25+2**0.5*r*math.sin(theta3))
        self.ctx.arc(self.get_box(r,c),start = 180+self.theta, end=self.theta+270, fill="green")
        self.ctx.arc(self.get_box(r,c2),start = self.theta, end=self.theta+90, fill="green")

class TruchetDrawer():
    def __init__(self):
        self.img = Image.new("RGB", (500, 300), (255,255,255))  # create new Image
        self.ctx = ImageDraw.Draw(self.img)  # create drawing context

    def fill_in_tiles(self):
        for i in range(10):
            for j in range(6):
                orientation = random.randint(0, 1)*90
                TileDrawer(i,j,orientation,self.ctx).draw()

    def make_image(self,filename):
        self.fill_in_tiles()
        self.img.save('truchet/' + filename + '.png')





TruchetDrawer().make_image('test5')


