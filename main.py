from Rendering.renderer import renderer
from PlayerScripts.keyboardInput import up_arrow, down_arrow, right_arrow, left_arrow
from PlayerScripts.playerMovement import playerUp, playerDown, playerRight, playerLeft
from time import sleep

renderer = renderer()
renderer.setPlayerPos(1, 1)
renderer.render()


def inputLook():
    while True:
        if(up_arrow()):
            playerUp(renderer)
            sleep(0.2)
        if(down_arrow()):
            playerDown(renderer)
            sleep(0.2)
        if(left_arrow()):
            playerLeft(renderer)
            sleep(0.2)
        if(right_arrow()):
            playerRight(renderer)
            sleep(0.2)


inputLook()
