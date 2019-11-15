from mcpi.minecraft import Minecraft
from random import randrange

mc = Minecraft.create()

def createRoad(length, direction):
    loops = 0
    x, y, z = mc.player.getPos()

    while loops < length:
        # We will increment in the direction we want.
        if direction == "North":
            mc.setBlocks(x+4, y-1, z, x-4, y-1, z+3, 43)     #stone slabs
            mc.setBlocks(x+2, y-1, z, x-2, y-1, z+3, 35, 15) #black wool
            mc.setBlocks(x, y-1, z+1, x, y-1, z+2, 35, 4)
            z = z + 4
        elif direction == "South":
            mc.setBlocks(x+4, y-1, z, x-4, y-1, z+3, 43)
            mc.setBlocks(x+2, y-1, z, x-2, y-1, z+3, 35, 15)
            mc.setBlocks(x, y-1, z+1, x, y-1, z+2, 35, 4)
            z = z - 4
        elif direction == "East":
            mc.setBlocks(x, y-1, z+4, x+3, y-1, z-4, 43)
            mc.setBlocks(x, y-1, z+2, x+3, y-1, z-2, 35, 15)
            mc.setBlocks(x+1, y-1, z, x+2, y-1, z, 35, 4)
            x = x + 4
        elif direction == "West":
            mc.setBlocks(x, y-1, z+4, x+3, y-1, z-4, 43)
            mc.setBlocks(x, y-1, z+2, x+3, y-1, z-2, 35, 15)
            mc.setBlocks(x+1, y-1, z, x+2, y-1, z, 35, 4)
            x = x - 4
        else:
            exit(1)
        
        loops = loops + 1
        

def createIntersection():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x+3, y-1, z-3, x-3, y-1, z+3, 35, 15)

# Clear the map
mc.setBlocks(127, -1, 127, -127, 63, -127, 0)
mc.setBlocks(127, -1, 127, -127, -1, -127, 2)

# Create cross-roads
createRoad(10, "North")
createRoad(10, "South")
createRoad(10, "East")
createRoad(10, "West")

# Lay down the intersection
createIntersection()