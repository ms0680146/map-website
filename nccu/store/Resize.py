from PIL import Image
import glob
#'*.jpeg' | '*.jpg'  | '*.png'
filepng=glob.glob('*.jpg')
print(filepng)
for i in filepng:
	im = Image.open(i)
	im2 = im.resize((350,315))
	im2.save(i[:-3]+"png")
#print(im2.size)

