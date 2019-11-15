from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlocks(x, y, z, x+8, y+5, z+10, 0) #temporary clear measure
mc.setBlocks(x, y-1, z, x+8, y-1, z+10, 2) #grass
mc.setBlocks(x, y, z, x+8, y, z+10, 85)#fence
mc.setBlocks(x+1, y, z+1, x+7, y, z+9, 0)#clear fence
mc.setBlock(x+4, y, z, 107, 2)#fence gate
mc.setBlocks(x+2, y, z+2, x+6, y+2, z+8, 98) #walls
mc.setBlocks(x+4, y, z+2, x+4, y+1, z+2, 0) #doorframe
mc.setBlocks(x+2, y-1, z+2, x+6, y-1, z+8, 5, 0) #floor
mc.setBlocks(x+3, y+3, z+2, x+5, y+3, z+8, 98)
mc.setBlocks(x+4, y+4, z+2, x+4, y+4, z+8, 98)
mc.setBlocks(x+2, y+1, z+4, x+6, y+2, z+6, 102)
mc.setBlocks(x+3, y, z+3, x+5, y+5, z+7, 0) #interior
mc.setBlocks(x+4, y+5, z+2, x+4, y+5, z+8, 44, 2) #roof support beam
mc.setBlock(x+4, y+3, z+7, 50, 4)#torches
mc.setBlock(x+4, y+3, z+3, 50, 3)#torches
mc.setBlock(x+4, y+3, z+1, 50, 4)
mc.setBlock(x, y+1, z, 50)
mc.setBlock(x+8, y+1, z, 50)
mc.setBlock(x, y+1, z+10, 50)
mc.setBlock(x+8, y+1, z+10, 50)
mc.setBlocks(x+2, y+3, z+2, x+2, y+3, z+8, 53, 0)#roof
mc.setBlocks(x+3, y+4, z+2, x+3, y+4, z+8, 53, 0)#roof
mc.setBlocks(x+5, y+4, z+2, x+5, y+4, z+8, 53, 1)#roof
mc.setBlocks(x+6, y+3, z+2, x+6, y+3, z+8, 53, 1)#roof
mc.setBlock(x+3, y, z+7, 58)#crafting bench
mc.setBlock(x+4, y, z+7, 54, 2)#chest
mc.setBlock(x+5, y, z+7, 61, 2)#furnace
mc.setBlock(x+4, y, z+2, 64, 1)#door bottom
mc.setBlock(x+4, y+1, z+2, 64, 8)#door top
mc.setBlock(x+3, y, z+3, 26, 10)#bed top
mc.setBlock(x+3, y, z+4, 26, 2)#bed bottom
mc.setBlocks(x+4, y+1, z+8, x+4, y+2, z+8, 102)
mc.player.setPos(x+4, y, z+5)