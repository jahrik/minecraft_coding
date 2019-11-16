from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
#mc.setBlocks(x, y-1, z, x+4, y-1, z+4, 35, 11)
mc.setBlocks(x+5, y-1, z+5, x-5, y-1, z-5, 35, 15)
mc.setBlocks(x+5, y-1, z+5, x+3, y-1, z-5, 43)
mc.setBlocks(x-5, y-1, z-5, x+2, y-1, z-3, 43)
mc.setBlocks(x-5, y-1, z+5, x+2, y-1, z+3, 43)
mc.setBlocks(x-3, y-1, z, x-2, y-1, z, 35, 4)