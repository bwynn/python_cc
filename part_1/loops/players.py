players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4]) #ommitting first value will return 0 through index specified
# print(players[2:]) # no end value returns index through end of array
# print(players[-3:]) # index from end of array

# loop through list
 print("The first three players on my team:")
 for player in players[:3]:
    print(player.title())
