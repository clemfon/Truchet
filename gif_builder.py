from PIL import Image, ImageDraw

gif_list = []
for i in range(10):
    gif_list.append(Image.open("drawing1/hello_drawing" + str(i) + ".png"))

gif_list[0].save('drawing1/hello_drawing.gif', save_all=True, append_images=gif_list[1:], optimize=False, duration=40, loop=0)