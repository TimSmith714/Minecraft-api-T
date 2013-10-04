#My first attempt at using the Minecraft API
#With lots of help from the code at www.stuffaboutcode.com

#import the minecraft.py module
import minecraft.minecraft as minecraft
#import the minecraft block module
import minecraft.block as block
#import time for delays
import time

if __name__ == "__main__":

	time.sleep(2)

	#SAC Connect to minecraft by creating the minecraft object
	#Minecraft needs to be running and in a game
	mc = minecraft.Minecraft.create()

	#SAC suggests posting a message to the chat window to confirm
	mc.postToChat("Hi, Minecraft API connected and about to do stuff")

	time.sleep(5)

	#SAC get the players position
	playerPos = mc.player.getPos()
	#mc.postToChat("Your position is x=" + str(playerPos.x) + "y=" + str(playerPos.y) + " and z=" + str(playerPos.z))

	#SAV Get the player position as integers that we can use with other commands 
	playerPos = minecraft.Vec3(int(playerPos.x), int(playerPos.y), int(playerPos.z))

	#My stuff Making the five lists I'm going to use to make my T
	a = [0,0,1,1,0,0]
	b = [0,0,1,1,0,0]
	c = [0,0,1,1,0,0]
	d = [1,1,1,1,1,1]
	e = [1,1,1,1,1,1]
	
	#First loop to place a
	#for block in a
	#mc.setBlock(playerPos.x + 1, playerPos.y + 1, playerPos.z +5, block.DIAMOND_BLOCK)

	blockRow = 0
	blockX = 0

	for rows in [a, b, c, d, e]:
		for blockType in [0, 1, 2, 3, 4, 5]:
		#mc.postToChat("Row " + str(rows))
			#mc.postToChat(rows[blockType])
			if rows[blockType] == 0:
				#insert air
				mc.setBlock(playerPos.x + blockX - 3, playerPos.y + blockRow, playerPos.z + 5, block.STONE)
			else:	
				mc.setBlock(playerPos.x + blockX - 3, playerPos.y + blockRow, playerPos.z + 5, block.DIAMOND_BLOCK)

			#time.sleep(1.2)
			blockX += 1

		blockRow += 1
		blockX = 0
