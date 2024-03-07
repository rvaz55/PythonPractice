#Link to the question: 
'''
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

Example

Index the array from . The number on each cloud is its index in the list so the player must avoid the clouds at indices  and . They could follow these two paths:  or . The first path takes  jumps while the second takes . Return .


'''
from itertools import count
import operator

clouds = [0,0,1,0]
cloudsCount = len(clouds) #len gives the number of items in a list
totalJumps = 0
i = 0
nextToLastIndex = cloudsCount - 1 

while i < nextToLastIndex:
    if i + 2 < cloudsCount and clouds[i+2] == 0:
        totalJumps += 1
        i += 2
    elif i + 1 < cloudsCount and clouds[i+1] == 0:
        totalJumps += 1
        i += 1

print(f"finalCountOfJumps:  {totalJumps}") 