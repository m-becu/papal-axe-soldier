from pygame_functions import *


W = 600
H = 600
HALF_W = W / 2
HALF_H = H / 2

INV_OPEN = False


# creating the screen
screenSize(W,H,fullscreen=True)

# set background color
setBackgroundColour("pink")

# loads sprite
player  = makeSprite("assets/side_walk.png", 6)  # links.gif contains 32 separate frames of animation.
sprite_apple = makeSprite("assets/inv_apple.png")
sprite_map = makeSprite("assets/inv_map.png")


# move the perso at the center of the screen
moveSprite(player,HALF_W,HALF_H,True)
showSprite(player)
transformSprite(player,0,4)



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
            moveSprite(sprite_apple,HALF_H+HALF_H/2,HALF_W)
            moveSprite(sprite_map,HALF_H-HALF_H/2,HALF_W)
            showSprite(sprite_apple)
            showSprite(sprite_map)

        else:
            INV_OPEN = True
            hideSprite(sprite_apple)
            hideSprite(sprite_map)
    else:
        changeSpriteImage(player, 0)  # the static facing front look

    #tick(120)

endWait()
