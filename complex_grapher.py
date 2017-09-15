from colorsys import hls_to_rgb #conversion between different color models
from cmath import phase #cmath also has a lot of cool complex functions you can graph
from math import pi, floor
from PIL import Image, ImageDraw


#The below method translates the native coordinates of an image's pixels
#so that (0, 0) is at the center rather than the top left corner. 
#It then negates the y coordinate, so that y increases rather
#than decreases with the height of the pixel.
def image_to_complex_coordinates(x, y, imageWidth, imageHeight):
	center = [imageWidth // 2, imageHeight // 2]
	return x - center[0], -(y - center[1])

def complex_to_hls(z):
	h = 0.5 + (phase(z) / (2*pi))
	l = 1 - 2**(-abs(z))
	s = 1
	return h, l, s

#Graphs the complex function complex_func (which maps complex numbers to complex numbers)
def graph(complex_func, center=0, scale=.01, width=500, height=500):
	im = Image.new("RGB", (width, height), 'white')
	draw = ImageDraw.Draw(im)
	for x in range(width):
		for y in range(height):
			u, v = image_to_complex_coordinates(x, y, width, height)
			z = u + v*1j
			z = (z-center)*scale
			try:
				w = complex_func(z)
			except (ZeroDivisionError, OverflowError, ValueError):
				#We interpret these errors as complex_func being very large at z.
				#No need to color since the image is white by default
				continue
				

			h, l, s = complex_to_hls(w)
			w_rgb = hls_to_rgb(h, l, s)
			w_rgb = tuple(floor(255*t) for t in w_rgb)
			draw.point([x, y], w_rgb)
	
	return im


#Example code

#from cmath import sin
#graph(sin, scale = .05)








