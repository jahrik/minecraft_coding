from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.getPos()

mc.player.setPos(0.5 + 24, -30, 0.5) # these are the coordinates you teleport to