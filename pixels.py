from time import sleep
from player import Player
# Github: PPixMans
sleep(2)
print("Start Farm Bot!")
player = Player()

try:
    while True:
        player.havestAll()
        player.plantAll()
        player.waterAll()
        player.refillEnergy()
        player.warpNext()
except Exception as e:
    player.log(e)
    pass
