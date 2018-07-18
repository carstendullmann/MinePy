import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3
import time
import math

def ProceedTrap():
    global playerTrapped
    global i
    trapColors = [14, 1, 4, 5, 3, 11, 10]
    if playerTrapped:
        mc.setBlocks(trapPos.x - 3, trapPos.y - 3, trapPos.z - 3, trapPos.x + 3, trapPos.y + 3, trapPos.z + 3, block.AIR.id, 0)
    else:
        currentTrapColorIndex = i % 7
        mc.setBlocks(trapPos.x - 3, trapPos.y - 3, trapPos.z - 3, trapPos.x + 3, trapPos.y + 3, trapPos.z + 3, 95, trapColors[currentTrapColorIndex]) # 95 = stained glass

def CheckPlayersToTrap():
    global playerTrapped
    global playerIds
    playerTrapped = False
    for playerId in playerIds:
        playerPos = mc.entity.getTilePos(playerId)
        distance = trapPos - playerPos
        distanceLength = math.sqrt(math.pow(distance.x,2)+math.pow(distance.y,2)+math.pow(distance.z,2))
        if distanceLength < 14:
            playerTrapped = True
            if distanceLength > 7:
                mc.setBlocks(trapPos.x - 3, trapPos.y - 3, trapPos.z - 3, trapPos.x + 3, trapPos.y + 3, trapPos.z + 3, block.AIR.id, 0)
                mc.entity.setTilePos(playerId,trapPos.x,trapPos.y,trapPos.z)
                mc.postToChat("You are trapped!")

def Run():
    global i
    global playerIds
    while True:
        try:
            time.sleep(1)
            playerIds = mc.getPlayerEntityIds() # This one fails if no players are in the game. This can most probably be fixed on github (https://github.com/zhuowei/RaspberryJuice/blob/master/src/main/java/net/zhuoweizhang/raspberryjuice/RemoteSession.java) by not cutting off the '|' when there are no players (code after 'c.equals("world.getPlayerIds")') )
        except Exception:
            playerIds = []
        ProceedTrap()
        CheckPlayersToTrap()
        i+=1

mc = minecraft.Minecraft.create("cadulldock.cloudapp.net")
trapPos = Vec3(-91, 2,-98)
playerTrapped = False
playerIds = []
# IDs see http://minecraft-ids.grahamedgecombe.com/
# IDs see http://minecraft-ids.grahamedgecombe.com/
mc.setBlocks(trapPos.x - 4, trapPos.y - 5, trapPos.z - 4, trapPos.x + 4, trapPos.y - 5, trapPos.z + 4, 209, 0) # 209 = End Gateway
mc.setBlocks(trapPos.x - 4, trapPos.y - 6, trapPos.z - 4, trapPos.x + 4, trapPos.y - 6, trapPos.z + 4, 80, 0) # 80 = Snow Block
mc.setBlocks(trapPos.x - 4, trapPos.y - 4, trapPos.z - 4, trapPos.x + 4, trapPos.y + 4, trapPos.z + 4, block.GLASS.id, 1)
i=0
print("Starting the trap.")
Run()