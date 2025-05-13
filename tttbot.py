# Title:TicTacToe, grid, choose X or O, display X or O, random.choice who will go first, Choose 1-9 or Computer chooses randomly, choice, grid ..., win, loss, tie, play again
# Index 1-9: (0, 4), (0, 11), (0, 18); (2, 4), (2, 11), (2, 18); (4, 4), (4, 11), (4, 18)
import random
class TicTacToeBot:
    def __init__(self):
        print("TicTacToe\n")
        self.x = [
            "      |      |       ",
            "---------------------",
            "      |      |       ",
            "---------------------",
            "      |      |       "
        ]                
        self.index_grid={1: [0, 3], 2: [0, 10], 3: [0, 17], 4: [2, 3], 5: [2, 10], 6: [2, 17], 7: [4, 3], 8: [4, 10], 9: [4, 17]}       
        self.win_options=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]        
        self.com_list=[]
        self.player_list=[]
        self.s=0
        self.print_grid()
        self.char_choice()
   
    def print_grid(self):
            for row in self.x:
                print(row)             
            if self.s>0:
                self.check_win()         
    def grid_update(self, human_value, com_value):
            if com_value is None:
                value_indexh=self.index_grid[int(human_value)]
                a, b = value_indexh
                if self.x[a][b] in [self.start_player, self.start_com]:
                    print("Invalid Input! Choose again.")
                    return self.human_choice()                   
                else:
                    self.x[a] = self.x[a][:b] + self.start_player + self.x[a][b + 1:]
                    self.player_list.append(human_value)    
            else:
                value_indexc=self.index_grid[int(com_value)]
                c, d = value_indexc
                self.x[c] = self.x[c][:d] + self.start_com + self.x[c][d+1:]
                self.com_list.append(com_value)
            self.s+=1
             
    def char_choice(self):
        choice=["X", "O"]
        self.inp_choice=input("\nChoose X or O: ").upper()
        if self.inp_choice not in choice:
            print("Invalid character! Choose again.")
            self.char_choice()
        else:
            random_beginner=random.choice(choice)
            if random_beginner !=self.inp_choice:
                print("\nThe computer will go first.")
                self.start_com=random_beginner
                self.start_player = choice[1 - choice.index(random_beginner)]
                self.computer() # branch
            else:
                self.start_player = random_beginner
                self.start_com = choice[1 - choice.index(random_beginner)]
                print("\nThe player will go first.")
                self.human_choice()        # branch
                
    def human_choice(self):
        while True:
            y=input("Choose a number ranging from 1-9: ")
            if not (y.isdigit()) or int(y) not in range(1, 10):
                print("Invalid Input! Choose again.")
                continue
            break    
        self.grid_update(int(y), None)        
        if self.s !=9: self.computer()
        self.print_grid() # yeah

    def computer(self):
        if self.s ==0 or self.s==1 and self.x[2][10] not in ["X", "O"]: # center is free
            self.grid_update(None, 5)
            self.print_grid()
            self.human_choice()  
        elif self.s ==1: # else go corner
                print("Corner")
                self.grid_update(None, random.choice([1, 3, 7, 9]))
                self.print_grid()
                self.human_choice() 
        else:
            result=self.com_move()    
            self.print_grid()
            self.human_choice()  
        # if human first, then look at possible combinations for human and block, if center is free then go center, then if human has two places try to block it ...   

    def com_move(self):
        self.possible_moves_com=[]
        self.possible_moves_player=[]
        for elm in self.win_options:
            for elmnt in elm:
                if elmnt in self.com_list and not(any(x in elm for x in self.player_list)):
                    for e in elm:
                        if e not in self.com_list:
                            self.possible_moves_com.append(e)                    
                if elmnt in self.player_list and not(any(y in elm for y in self.com_list)):
                    for e in elm:
                        if e not in self.player_list:
                            self.possible_moves_player.append(e) 
        both=[num for num in self.possible_moves_com if num in self.possible_moves_player]
        good_block=[t for t in self.possible_moves_player if self.possible_moves_player.count(t) >= 2 ]       
        good_move=[l for l in self.possible_moves_com if self.possible_moves_com.count(l) >= 2]
        if self.possible_moves_com:  self.possible_moves_com=random.shuffle(self.possible_moves_com)
        list_moves=[good_block, good_move, both, self.possible_moves_com]
        all_moves=[m for l in list_moves if l is not(None) for m in l] 
        all_moves=[b for num, b in enumerate(all_moves) if all_moves.index(b)==num]
        random_move=[n for n in range(1, 10) if not(n in self.com_list or n in self.player_list)]
        self.grid_update(None, all_moves[0]) if all_moves else self.grid_update(None, random_move[0])

    def check_win(self):
        for sublist in self.win_options:
            if all(element in self.player_list for element in sublist):
                self.play_again("Player won!")                                 
            elif all(element in self.com_list for element in sublist):
                self.play_again("Computer won!")                                 
        if self.s == 9:
            self.play_again("It's a tie!")
            
    def play_again(self, msg):
        print(msg)
        r=input("Play again? (y/n): ").lower()
        if r == "y":
            restart=TicTacToeBot()
        else:
            exit()
start=TicTacToeBot()
