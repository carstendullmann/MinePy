import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *

mc = minecraft.Minecraft.create("cadulldock.cloudapp.net")
height = 60
width = 80
z = 10
mc.setBlocks(-width, 0, z, width, height, z, 0)
for x in range(-width, width):
    
    # HIER die Funktion einsetzen bzw. ändern:
    y = 0.25 * x
    
    if y <= height and y >= 0:
        mc.setBlock(x, y, z, 95, 14) # red stained glass

# and then continue with this: https://stackoverflow.com/questions/10303248/true-dynamic-and-anonymous-functions-possible-in-python
