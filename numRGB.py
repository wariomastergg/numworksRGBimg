from PIL import Image
image =Image.open("") #put file path here
siz = [, ] #put xy image size here
s = ""
for i in range(siz[1]):
    for j in range(siz[0]):
        col = image.getpixel((j,i))
        s = s + str(col) + ", "
print(s[0:-2])
