from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
loops = 0

while loops < 5:
    mc.setBlocks(x+5, y-1, z-1, x-5, y-1, z+4, 43)
    mc.setBlocks(x+3, y-1, z-1, x-3, y-1, z+4, 35, 15)
    mc.setBlocks(x, y-1, z+1, x, y-1, z+2, 35, 4)
    loops = loops + 1
    mc.player.setPos(x+4, y, z)