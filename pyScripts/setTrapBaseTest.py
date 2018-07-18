import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import time
import math
mc = minecraft.Minecraft.create("cadulldock.cloudapp.net")
trapPos = Vec3(-91, 2,-98)
# IDs see http://minecraft-ids.grahamedgecombe.com/
mc.setBlocks(trapPos.x - 4, trapPos.y - 5, trapPos.z - 4, trapPos.x + 4, trapPos.y - 5, trapPos.z + 4, 209, 0) # 209 = End Gateway
mc.setBlocks(trapPos.x - 4, trapPos.y - 6, trapPos.z - 4, trapPos.x + 4, trapPos.y - 6, trapPos.z + 4, 80, 0) # 80 = Snow Block
