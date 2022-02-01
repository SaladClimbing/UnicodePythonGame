def playerUp(renderer):
    if(renderer.checkPlayerCollision(renderer.getPlayerPosX(), renderer.getPlayerPosY() - 1)):
        renderer.setPlayerPos(renderer.getPlayerPosX(),
                              renderer.getPlayerPosY() - 1)
        renderer.render()


def playerDown(renderer):
    if(renderer.checkPlayerCollision(renderer.getPlayerPosX(), renderer.getPlayerPosY() + 1)):
        renderer.setPlayerPos(renderer.getPlayerPosX(),
                              renderer.getPlayerPosY() + 1)
        renderer.render()


def playerLeft(renderer):
    if(renderer.checkPlayerCollision(renderer.getPlayerPosX() - 1, renderer.getPlayerPosY())):
        renderer.setPlayerPos(renderer.getPlayerPosX() - 1,
                              renderer.getPlayerPosY())
        renderer.render()


def playerRight(renderer):
    if(renderer.checkPlayerCollision(renderer.getPlayerPosX() + 1, renderer.getPlayerPosY())):
        renderer.setPlayerPos(renderer.getPlayerPosX() + 1,
                              renderer.getPlayerPosY())
        renderer.render()
