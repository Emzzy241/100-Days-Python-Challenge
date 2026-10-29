# Practicing with the colorgram package.... And essentially becoming much more better at it

import colorgram

# Extract 6 colors from the image.... Well it is a basic image, I doubt it if 6 colors would be found in it
colors = colorgram.extract("./images/Professional-Headshot.png", 6)

rgb_colors = []

# for color in colors:
#     print(color)
# The output of the above is:
# python colorgram-practice.py
# <colorgram.py Color: Rgb(r=38, g=40, b=50), 41.83954385492105%>
# <colorgram.py Color: Rgb(r=206, g=206, b=210), 24.84096343255753%>
# <colorgram.py Color: Rgb(r=171, g=175, b=182), 13.907395278729211%>
# <colorgram.py Color: Rgb(r=121, g=86, b=70), 7.849120519947729%>
# <colorgram.py Color: Rgb(r=76, g=88, b=100), 6.854162684223885%>
# <colorgram.py Color: Rgb(r=182, g=173, b=168), 4.708814229620599%>

# Do not forget () represents tuples in pythons, elements in them can be accessed similarly with python lists

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

# print(colors)

colors = [(38, 40, 50), (206, 206, 210), (171, 175, 182), (121, 86, 70), (76, 88, 100), (182, 173, 168)]
# For my professional headshot image stored in images folder