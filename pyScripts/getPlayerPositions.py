import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("cadulldock.cloudapp.net")

players = mc.getPlayerEntityIds() # This one fails if no players are in the game. This can most probably be fixed on github (https://github.com/zhuowei/RaspberryJuice/blob/master/src/main/java/net/zhuoweizhang/raspberryjuice/RemoteSession.java) by not cutting off the '|' when there are no players (code after 'c.equals("world.getPlayerIds")') )

for pId in players:
    print(pId)
    mc.postToChat("PId: " + str(pId))
    print(mc.entity.getPos(pId))
    print(mc.entity.getTilePos(pId))

print(players)


