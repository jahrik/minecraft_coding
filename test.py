from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
#mc.setBlocks(x, y-1, z, x+4, y-1, z+4, 35, 11)
it = 0       
while it < 10:   
    it = it+1
    mc.setBlocks(x, y-1, z+2, x+2, y-1, z-2, 35, 15)
    mc.setBlocks(x+1, y-1, z, x, y-1, z, 35, 4)
    x=x+1
x, y, z = mc.player.getPos()
mc.setBlock(x, y-1, z, 35, 15)
b = x
while x < it+b:
    x=x+3
    mc.setBlocks(x, y-1, z, x+1, y-1, z, 35, 15)
    x=x+1