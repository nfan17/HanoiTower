'''
nfan17

Hanoi Tower:
This is the main class for my Hanoi Tower game. HanoiTower implements ArrayStacks 
from MyArrayStack and a personal disc object to simulate rods and discs. hanoiSolve() 
plays through and solves the game implementation using recursion. playGame() begins
and new console (no graphics) game of Hanoi Tower. 
'''

from HanoiTower import HanoiTower

def hanoiSolve(n, startRod = 1, endRod = 3, auxRod = 2):
    '''
    Solves initiated game of hanoi tower with n discs
    '''
    #base case: n = 1, with one disc, move disc from start to end
    if n == 1:
        HTGame.move(startRod, endRod)
        print(HTGame)
    else:
        #move n - 1 discs from start to auxillary rod, at n = 1, largest 
        # disc will be moved from start to end (1 to 3)
        hanoiSolve(n - 1, startRod, auxRod, endRod)
        HTGame.move(startRod, endRod)
        print(HTGame)
        #largest disc is now in end rod, all others in auxillary rod so
        # move n - 1 discs from auxillary rod to endRod
        hanoiSolve(n - 1, auxRod, endRod, startRod)

def playGame():
    run = True
    while run == True:
        turns = 0
        inp = input("\nWelcome to Hanoi Tower!\nPress 1 to start new game, 2 to see game rules, or 0 to exit: ")
        if inp == "1":
            valid = False
            while valid == False:
                discs = input("Please enter the number of discs: ")
                try:
                    discs = float(discs)
                except ValueError:
                    print("Invalid input, please enter a postive integer.")
                    continue
                if discs > 0 and discs // 1 == discs:
                    valid = True
                else:
                    print("Invalid input, please enter a postive integer.")
            HTGame = HanoiTower(int(discs))
            HTGame.startGame()
            while inp != 0:
                print(f"\n{HTGame}")
                inp = input("\nEnter a rod to move from, or press 0 to exit: ")
                try:
                    inp = int(inp)
                except ValueError:
                    print(f"Invalid input. Please try again.\n")
                    continue
                if inp == 0:
                    run = False
                    break
                elif inp >= 1 and inp <= 3:
                    valid = False
                    while valid == False:
                        inp2 = input("Enter a rod to move to: ")
                        if not HTGame.isEmpty(inp - 1):
                            try:
                                inp2 = int(inp2)
                            except ValueError:
                                print(f"Invalid input. Please try again.\n")
                                break
                            if inp2 <= 3 and inp2 > 0 and HTGame.move(inp, inp2):
                                turns += 1
                                break
                        print(f"Invalid move. Please try again.\n")
                        break
                    if HTGame.gameWin():
                        print(f"\n{HTGame}")
                        replay = input(f"You won in {turns} turns!\nPress 1 to play again or 0 to exit: ")
                        if replay == "1":
                            break
                        else:
                            run = False
                        break
                else:
                    print("Input not valid, please try again.")    
        elif inp == "2":
            print('''Rules:\n
            1) Only one disc can be moved at a time
            2) Discs are moved from the top of one stack to the top of another
            3) Any given disc may never be placed on top of a smaller disc
            4) To win, move all discs from the left-most rod to the right-most rod
            ''')
            ret = False
            while ret == False:
                inp3 = input("Enter any key to return to menu: ")
                ret = True
                break
        elif inp == "0":
            run = False
            break
        else:
            print("Invalid input. Please try again.")
    print("Thanks for Playing!")

if __name__ == '__main__':
    run1 = True
    while run1 == True:
        mode = input("Enter 1 to play game, 2 to get solution, or 0 to exit: ")
        if mode == "1":
            playGame()
            break
        elif mode == "2":
            valid = False
            while valid == False:
                discInp = input("Enter number of discs: ")
                try:
                    N = int(discInp)
                    valid = True
                except ValueError:
                    print("Invalid input, please try again.")      
                    del discInp          
            N = int(discInp)
            HTGame = HanoiTower(N)
            HTGame.startGame()
            print(HTGame)
            hanoiSolve(N)
            if HTGame.gameWin() == True:
                print("Game won!")
            break
        elif mode == "0":
            print("Exiting now.")
            run1 = False
            break
        else: 
            print("Invalid input, please try again.")
            del input
    

