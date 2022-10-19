from Disc import Disc
from MyArrayStack import MyArrayStack

class HanoiTower():
    def __init__(self, numDiscs : int):
        self.discs = numDiscs
        self.sticks = {}
        self.sticks[0] = MyArrayStack()
        self.sticks[1] = MyArrayStack()
        self.sticks[2] = MyArrayStack()

    def startGame(self):
        '''
        Starts new game by filling first rod with x discs
        '''
        i = self.discs
        while i > 0:
            disc = Disc(i)
            self.sticks[0].push(disc)
            i -= 1
        self.win = str(self.sticks[0])

    def gameWin(self):
        '''
        Checks if game has been completed. 

        Returns: 
        True if won, false if not.
        '''
        return str(self.sticks[2]) == self.win

    def isEmpty(self, i : int):
        '''
        Checks if a rod has no discs.

        Returns:
        True if no rods are present, false 
        if there is at least one rod.
        '''
        return self.sticks[i].size() == 0


    def move(self, fromstick : int, tostick : int):
        '''
        Moves top disc from one rod to another
        '''
        fStick = self.sticks[fromstick - 1]
        tStick = self.sticks[tostick - 1]
        if tStick.size() == 0:
            tStick.push(fStick.pop())
            return True
        elif (fStick.peek() < tStick.peek()) == True:
            tStick.push(fStick.pop())
            return True
        else:
            return False
            
    def __str__(self):
        return f'''Hanoi Tower: {self.discs} discs\n{self.sticks[0]}    {self.sticks[1]}    {self.sticks[2]}'''

    