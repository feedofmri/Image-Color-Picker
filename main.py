from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

img = ColorThief('image.jpg')

# get the dominant colors
dominant_color = img.get_color(quality=1)
palette = img.get_palette(color_count=6)

plt.imshow([palette[i] for i in range(6)])
plt.show()

print("Color Palette:")
for color in palette:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
