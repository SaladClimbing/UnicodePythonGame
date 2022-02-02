from os import system, chdir


class renderer():

    def __init__(self):
        self.playerX = None
        self.playerY = None
        self.playerChar = '■'
        self.walkableChar = '□'
        # TODO Add collisions
        self.collideChar1 = '['
        self.collideChar2 = ']'

    def render(self):
        system('cls')
        if self.playerX != None and self.playerY != None:
            print(self.placePlayerPosition(
                self.playerX, self.playerY, self.playerChar))
        else:
            print(self.getBackground())

    # SECTION Set statements
    def setPlayerPos(self, x, y):
        self.playerX = x
        self.playerY = y
    # !SECTION

    def placePlayerPosition(self, playerX, playerY, playerChar):
        toDisplay = self.getBackground()
        toDisplay[playerY][playerX] = playerChar
        returnDisplay = ""
        for list in toDisplay:
            for item in list:
                returnDisplay = returnDisplay + item
            returnDisplay = returnDisplay + '\n'
        return returnDisplay

    def checkPlayerCollision(self, playerX, playerY):
        if(self.getBackground()[playerY][playerX] == self.walkableChar):
            return True
        elif(self.getBackground()[playerY][playerX] != self.walkableChar):
            return False
        else:
            return "Error"

    # SECTION Get Statements
    # * ANCHOR Get statement for player positions
    def getPlayerPosX(self):
        return self.playerX

    def getPlayerPosY(self):
        return self.playerY

    # * ANCHOR Returns the grid in which the game is played
    # TODO Make easier to edit
    def getBackground(self):
        mapDir = "Maps\map.txt"
        chdir("")
        file = open("Maps\map.txt", 'r')
        lines = file.readlines()
        print(lines)
        file.close()
    # !SECTION
