from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
loops = 0

while loops < 3:
    mc.setBlocks(x, y-1, z+4, x+3, y-1, z-4, 43)
    mc.setBlocks(x, y-1, z+2, x+3, y-1, z-2, 35, 15)
    mc.setBlocks(x+1, y-1, z, x+2, y-1, z, 35, 4)
    loops = loops + 1
    mc.player.setPos(x+4, y, z)