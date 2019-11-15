from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def loopRoad(loops):
    x, y, z = mc.player.getPos()
    
    while loops < 3:
        mc.setBlocks(x+2, y-1, z, x-2, y-1, z+3, 35, 15)
        mc.setBlocks(x, y-1, z+1, x, y-1, z+2, 35, 4)
        loops = loops + 1
        z = z + 4
# Y is the altitude
# X is left/right
# Z is forward/backward
#def createRoad(x_target, y_target, z_target):
#    if x_target > -1:
#        x_direction = 5        
 #   elif x_target < -1:
#        x_direction = -5
 #   else:
 #       exit(1)
    
 #   mc.setBlocks(x_target, y_target - 1, z_target, x_target + x_direction, y_target - 1, z_target + 5, 35, 15)



#createRoad(-2, 21, 10)
        
loopRoad(0)