from PIL import Image
image =Image.open("/home/micah/Documents/python/image data/mario.jpg") #put file path here
siz = [8, 8] #put xy image size here
s = []
def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

hex_to_rgb("#ffffff")           #==> (255, 255, 255)
hex_to_rgb("#ffffffffffff")     #==> (65535, 65535, 65535)
rgb_to_hex(255, 255, 255)       #==> '#ffffff'
rgb_to_hex(65535, 65535, 65535) #==> '#ffffffffffff'
for i in range(siz[1]):
    for j in range(siz[0]):
        col = image.getpixel((i,j))
        r = col[0]
        g = col[1]
        b = col[2]
        s.append(rgb_to_hex(r, g, b))
print(s)
