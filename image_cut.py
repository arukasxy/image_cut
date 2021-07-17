from PIL import Image

name=input("输入图片路径，例如./data/cut/thor.jpg\n")
img = Image.open(name)
width=img.size[0]
a4_length=width*1.414
length=img.size[1]
numbers=length/a4_length
i_num=int(length//a4_length)
for i in range(i_num):
    cropped = img.crop((0,a4_length*i, width,a4_length*i+a4_length)) # (left, upper, right, lower)
    file_name="./image"+str(i)+".jpg"
    print(file_name)
    cropped.save(file_name)
if(numbers!=length//a4_length):
	cropped = img.crop((0,(i_num)*a4_length, width,length)) # (left, upper, right, lower)
	file_name="./image"+str(length//a4_length)+".jpg"
	cropped.save(file_name)
