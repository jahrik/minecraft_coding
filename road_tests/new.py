from mcpi.minecraft import Minecraft
from random import randrange

mc = Minecraft.create()

def createRoad(length, direction):
    loops = 0
    x, y, z = mc.player.getPos()
    
    while loops < length:
        # We will increment in the direction we want.
        if direction == "North":
            mc.setBlocks(x+4, y-1, z, x-4, y-1, z+3, 43)
            mc.setBlocks(x+2, y-1, z, x-2, y-1, z+3, 35, 15)
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
# This is the function call for a length of road.
# Specify the number of panels inside the parenthesis. -elk
tploops = 0
tpHeight = 30
roadLength = 1
while tploops < 1:
    random_x = randrange(-120, 120)
    random_z = randrange(-120, 120)
    blockObj, blockData = mc.getBlockWithData(random_x, tpHeight, random_z)
    blockObjTwo, blockDataTwo = mc.getBlockWithData(random_x, tpHeight-1, random_z)
    if blockObj == 0 and blockObjTwo == 0:
        print(f'x={random_x}')
        print(f'z={random_z}')
        mc.player.setPos(random_x, tpHeight, random_z)
        random_road = randrange(1, 4)
        if random_road == 1:
            createRoad(roadLength, "North")
        elif random_road == 2:
            createRoad(roadLength, "South")
        elif random_road == 3:
            createRoad(roadLength, "East")
        else:
            createRoad(roadLength, "West")
        tploops = tploops + 1

my_list = []

x, y, z = mc.player.getPos()
b = x
w = x

while b < w + 10:
    blockObjThree, blockDataThree = mc.getBlockWithData(random_x, tpHeight-1, random_z)
    b = b + 1
    random_x = random_x - 1
    print(blockObjThree)
    my_list.append(blockObjThree)
    
total = sum(float(t) for t in my_list)

#if 0 in my_list:
print(total)