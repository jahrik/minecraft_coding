from mcpi.minecraft import Minecraft
from random import randrange

mc = Minecraft.create()

x, y, z = mc.player.getPos()

mainRoadLength = 2

mc.setBlocks(127.7, -1, 120, -127.7, 63, -120, 0)
mc.setBlocks(127.7, -1, 120, -127.7, -1, -120, 2)

#mc.setBlocks(x+4, y-1, z, x-4, y-1, z+3, 43)
#mc.setBlocks(x+2, y-1, z, x-2, y-1, z+3, 35, 15)
#mc.setBlocks(x, y-1, z+1, x, y-1, z+2, 35, 4)
