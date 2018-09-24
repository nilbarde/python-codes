#!/usr/bin/python
import Image, ImageDraw, math, colorsys
import time
import matplotlib.pyplot as plt

dimensions = (800, 800)
scale = 1.0/(dimensions[0]/3)
#center = (2.2, 1.5)       # Use this for Mandelbrot set
center = (1.5, 1.5)       # Use this for Julia set
iterate_max = 100
colors_max = 255

img = Image.new("RGB", dimensions)
d = ImageDraw.Draw(img)

# Calculate a tolerable palette
palette = [0] * colors_max
for i in xrange(colors_max):
    f = 1-abs((float(i)/colors_max-1)**15)
    r, g, b = colorsys.hsv_to_rgb(.66+f/3, 1-f/2, f)
    palette[i] = (int(r*255), int(g*255), int(b*255))
num = []
r=[]
b=[]
g=[]
for i in xrange(colors_max):
    num.append(i)
    r.append(palette[i][0])
    g.append(palette[i][1])
    b.append(palette[i][2])
    
plt.plot(num, r,color='red')
plt.plot(num, g,color='green')
plt.plot(num, b,color='blue')
plt.xlabel('h color')
plt.ylabel('rgb color')
plt.savefig('hsv.png')

# Calculate the mandelbrot sequence for the point c with start value z
def iterate_mandelbrot(c, z = 0):
    for n in xrange(iterate_max + 1):
        z = z*z +c
        if abs(z) > 2:
            return n
    return None

# Draw our image
for y in xrange(dimensions[1]):
    for x in xrange(dimensions[0]):
        c = complex(x * scale - center[0], y * scale - center[1])

        #n = iterate_mandelbrot(c)            # Use this for Mandelbrot set
        n = iterate_mandelbrot(complex(0.3, 0.6), c)  # 0.3 0.6 Use this for Julia set

        if n is None:
            v = 1
        else:
            v = n/100.0

        d.point((x, y), fill = palette[int(v * (colors_max-1))])
img.show()
img.save("julia4/result.png")
