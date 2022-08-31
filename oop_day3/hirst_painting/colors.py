import colorgram as c

rgb_colors = []
hirst_colors = c.extract('image.jpg', 30)
for color in hirst_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    final_color = (r, g, b)
    rgb_colors.append(final_color)
print(rgb_colors)
