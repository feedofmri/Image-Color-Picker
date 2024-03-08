from colorthief import ColorThief
import matplotlib.pyplot as plt

img = ColorThief('image.jpg')

# get the dominant colors
dominant_color = img.get_color(quality=1)
palette = img.get_palette(color_count=6)

plt.imshow([palette[i] for i in range(6)])
plt.show()
