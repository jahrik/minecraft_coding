from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()

mc.setBlock(0, 63, 0, 50, 1) #east
mc.setBlock(0, 62, 0, 50, 2) #west
mc.setBlock(0, 61, 0, 50, 3) #south
mc.setBlock(0, 60, 0, 50, 4) #north

blockObj = mc.getBlockWithData(0, 63, 0)
blockObj,west = mc.getBlockWithData(0, 62, 0) # -x
blockObj,south = mc.getBlockWithData(0, 61, 0) # -z
blockObj,north = mc.getBlockWithData(0, 60, 0) # +z
print(north)

mc.setBlock(north+2, y, south, 35, 15)