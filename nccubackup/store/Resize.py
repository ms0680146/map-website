from PIL import Image
import glob
filepng=glob.glob('*.png')
print(filepng)
for i in filepng:
	im = Image.open('i')
	im2 = im.resize((350,315))
im2.save("1.png")
print(im2.size)
