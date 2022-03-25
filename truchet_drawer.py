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
        # if self.theta % 360 == 0:
        #     # self.ctx.arc([(-25+50*a,-25+50*b),(25+50*a,25+50*b)], start=0, end=90, fill="black")
        #     self.ctx.arc(self.get_box(r,(50*a,50*b)), start=0, end=90, fill="black")
        #     self.ctx.arc([(25+50*a,25+50*b),(75+50*a,75+50*b)], start=180, end=270, fill="black")
        # elif self.theta % 360 == 180:
        #     self.ctx.arc([(-25+50*a,25+50*b),(25+50*a,75+50*b)], start=-90, end=0, fill="red")
        #     self.ctx.arc([(25+50*a,-25+50*b),(75+50*a,25+50*b)], start=90, end=180, fill="blue")
        # else:
        theta2 = (self.theta+45)*math.pi/180
        c = (50*a+25+2**0.5*r*math.cos(theta2),50*b+25+2**0.5*r*math.sin(theta2))
        #c = (50*a+25+math.cos(theta2)*r,50*b+25+math.sin(theta2)*r)
        self.ctx.arc(self.get_box(r,c),start = 180+self.theta, end=self.theta+270, fill="green")
        #self.ctx.rectangle(self.get_box(r,c), outline="blue")

class TruchetDrawer():
    def __init__(self):
        self.img = Image.new("RGB", (500, 300), (255,255,255))  # create new Image
        self.ctx = ImageDraw.Draw(self.img)  # create drawing context

    def fill_in_tiles(self):
        for i in range(10):
            for j in range(6):
                #orientation = bool(random.getrandbits(1))
                orientation = random.randint(0, 1)*90
                #orientation=0
                TileDrawer(i,j,orientation,self.ctx).draw()
                TileDrawer(i,j,orientation+180,self.ctx).draw()

    def make_image(self,filename):
        self.fill_in_tiles()
        self.img.save('truchet/' + filename + '.png')





TruchetDrawer().make_image('test4')


