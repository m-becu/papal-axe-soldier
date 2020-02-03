from pygame_functions import *


H = 600
W = 600
HALF_H = H / 2
HALF_W = W / 2

INV_OPEN = False


# creating the screen
screenSize(H,W)

# set background color
setBackgroundColour("pink")

# loads sprite
player  = makeSprite("assets/side_walk.png", 6)  # links.gif contains 32 separate frames of animation.
sprite_apple = makeSprite("assets/inv_apple.png")
sprite_apple = makeSprite("assets/inv_map.png")


# move the perso at the center of the screen
moveSprite(player,HALF_W,HALF_H,True)
showSprite(player)
transformSprite(player, 0, 15)

nextFrame = clock()
frame = 0

while True:
    if clock() > nextFrame:                         # We only animate our character every 80ms.
        frame = (frame+1)%6                         # There are 8 frames of animation in each direction
        nextFrame += 80                             # so the modulus 8 allows it to loop

    if keyPressed("d"):
        changeSpriteImage(player, 0*6+frame)    # 0*8 because right animations are the 0th set in the sprite sheet

    elif keyPressed("s"):
        changeSpriteImage(player, 0*6+frame)    # down facing animations are the 1st set

    elif keyPressed("q"):
        changeSpriteImage(player, 0*6+frame)    # and so on

    elif keyPressed("z"):
        changeSpriteImage(player, 0*6+frame)

    # open the inventory
    elif keyPressed("i"):
        if INV_OPEN:
            INV_OPEN = False

        else:
            INV_OPEN = True
    else:
        changeSpriteImage(player, 0)  # the static facing front look

    #tick(120)

endWait()
