from mcpi.minecraft import Minecraft
from random import randrange
mc = Minecraft.create()
random_gm = randrange(1, 100) #gm = gridmap
#gm_1 setup
gm_1_mod_1 = randrange(1,2)

def createRoad(length, direction):
    loops = 0
    x, y, z = mc.player.getPos()
    
    while loops < length:
        # We will increment in the direction we want.
        if direction == "North":
            mc.setBlocks(x+5, y-1, z, x-5, y-1, z+3, 43)
            mc.setBlocks(x+2, y-1, z, x-2, y-1, z+3, 35, 15)
            mc.setBlocks(x, y-1, z+1, x, y-1, z+2, 35, 4)
            z = z + 4
        elif direction == "South":
            mc.setBlocks(x+5, y-1, z, x-5, y-1, z+3, 43)
            mc.setBlocks(x+2, y-1, z, x-2, y-1, z+3, 35, 15)
            mc.setBlocks(x, y-1, z+1, x, y-1, z+2, 35, 4)
            z = z - 4
        elif direction == "East":
            mc.setBlocks(x, y-1, z+5, x+3, y-1, z-5, 43)
            mc.setBlocks(x, y-1, z+2, x+3, y-1, z-2, 35, 15)
            mc.setBlocks(x+1, y-1, z, x+2, y-1, z, 35, 4)
            x = x + 4
        elif direction == "West":
            mc.setBlocks(x, y-1, z+5, x+3, y-1, z-5, 43)
            mc.setBlocks(x, y-1, z+2, x+3, y-1, z-2, 35, 15)
            mc.setBlocks(x+1, y-1, z, x+2, y-1, z, 35, 4)
            x = x - 4
        else:
            exit(1)
        loops = loops + 1

mc.player.setPos(0, -30, 0)
mc.setBlocks(120, 63, 120, -120, -30, -120, 0)#clear map
x, y, z = mc.player.getPos()
mc.setBlocks(120, y-1, 120, -120, y-1, -120, 2)#grass

#grid_1 road building
mc.setBlocks(x+5, y-1, z+5, x-5, y-1, z-5, 35, 15)
mc.setBlocks(x+5, y-1, z+5, x+3, y-1, z+3, 43)
mc.setBlocks(x-5, y-1, z-5, x-3, y-1, z-3, 43)
mc.setBlocks(x+5, y-1, z-5, x+3, y-1, z-3, 43)
mc.setBlocks(x-5, y-1, z+5, x-3, y-1, z+3, 43)
mc.setBlocks(x+3, y-1, z+3, x-3, y-1, z-3, 35, 15)
mc.player.setPos(x+5, y, z)
createRoad(4, "East")
mc.player.setPos(x-8, y, z)
createRoad(4, "West")
mc.player.setPos(x, y, z+5)
createRoad(4, "North")
mc.player.setPos(x, y, z-8)
createRoad(4, "South")
#gridMap_1_module_1
#if gm_1_mod_1 == 1:
#    mc.player.setPos(x+5, y, z)
#    createRoad(3, "East")