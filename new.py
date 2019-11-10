from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlocks(x-10, y-2, z-10, x+10, y+1, z+10, 0)