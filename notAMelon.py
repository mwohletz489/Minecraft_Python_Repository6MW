from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
melon = 103
block = mc.getblock(x, y, z)

noMelon = 13

mc.postToChat("You need to get some food: " + str(noMelon))
