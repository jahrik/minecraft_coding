from mcpi.minecraft import Minecraft
from random import randrange
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mainRoadLength = 2




#mc.setBlocks(120, -1, 120, -120, 63, -120, 0)
#mc.setBlocks(120, -1, 120, -120, -1, -120, 2)
mc.setBlocks(x+4, y-1, z, x-4, y-1, z+3, 43)
mc.setBlocks(x+2, y-1, z, x-2, y-1, z+3, 35, 15)
mc.setBlocks(114, -1, -119, 114, -1, -118, 35, 4)
