from PIL import Image, ImageDraw, ImageFont
from words import *

X_SIZE = 200
Y_SIZE = 100

print("making images")

# get a font
fnt = ImageFont.truetype("Arial.ttf", 28)

def draw_bingo_image():
	out = Image.new("RGB", (X_SIZE, Y_SIZE), (255,255,255))
	draw = ImageDraw.Draw(out)

	word = bingo_title

	fnt = ImageFont.truetype("Arial.ttf", 60)

	left, top, right, bottom = draw.multiline_textbbox((0,0), word, fnt)
	width = right - left
	height = bottom - top

	x = (out.width - width) / 2
	y = (out.height - height) / 2

	draw.multiline_text((x,y), word, font=fnt, fill=(0,0,0), align='center')
	out.save(f"images/title.gif", "gif")


def draw_image(foods_list,lang):

	# for i in range(len(foods_list)):
	for i in range(25):

		# create an image
		out = Image.new("RGB", (X_SIZE, Y_SIZE), (255, 255, 255))

		# get a drawing context
		draw = ImageDraw.Draw(out)

		word = foods_list[i].replace(" ","\n",1)

		left, top, right, bottom = draw.multiline_textbbox((0,0), word, fnt)
		width = right - left
		height = bottom - top
		
		# print(width, height)
	 
		# print(bounding_box)
		x = (out.width - width) / 2
		y = (out.height - height) / 2

		# draw multiline text
		draw.multiline_text((x, y), word, font=fnt, fill=(0, 0, 0), align='center')

		# out.show()
		if i == 0:
			out.save(f"images/999{lang}.gif", "gif")
		else:
			out.save(f"images/{i-1}{lang}.gif", "gif")


draw_image(words[0], 'sf')
draw_image(words[1], 'ef')
draw_image(words[2], 'sb')
draw_image(words[3], 'eb')

draw_bingo_image()

print("done")