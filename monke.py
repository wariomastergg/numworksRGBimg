from PIL import Image
image =Image.open("/home/micah/Documents/python/computer sience ap/mario.jpg")
siz = [16, 16]
s = ""
for i in range(siz[1]):
    for j in range(siz[0]):
        col = image.getpixel((j,i))
        s = s + str(col) + ", "
print(s)