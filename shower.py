from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = x
shwrY = y
shwrZ = z

width = 6
height = 9
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and shwrY <= y < shwrY + height and shwrZ <= z < shwrZ + length
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 8)
else:
    mc.setBlocks(shwrX, shwrY + height, shwrZ,
                 shwrX + wifth, shwrY + height, shwrZ + length, 0)
