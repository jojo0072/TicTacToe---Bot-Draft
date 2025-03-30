"""
       |         |
---------------------
       |         |
---------------------
       |         |
"""
# Title:TicTacToe, grid, choose X or O, display X or O, random.choice who will go first, Choose 1-9 or Computer chooses randomly, choice, grid ..., win, loss, tie, play again
# Index 1-9: (0, 4), (0, 11), (0, 18); (2, 4), (2, 11), (2, 18); (4, 4), (4, 11), (4, 18)
import random
def start():
    global x, s
    print("TicTacToe\n")
    #x=[[6*" "+ "|" + 6* " "+ "|" + 7* " "],
    #          [ 21 * "-" ],   
    #         [6*" "+ "|" + 6* " "+ "|" + 7* " "],
    #        [ 21 * "-" ],   
    #       [6*" "+ "|" + 6* " "+ "|" + 7* " "]]
    x = [
        "      |      |       ",
        "---------------------",
        "      |      |       ",
        "---------------------",
        "      |      |       "
    ]
   
    s= -1
    print_grid()
    char_choice()
   
def print_grid():
        global x, s
        for row in x:
            print(row)
        s+=1
        #print(s)
        if s !=0 :
            check_win()         
   
def char_choice():
    global start_com, start_player, inp_choice
    #import random
    choice=["X", "O"]
    inp_choice=input("\nChoose X or O: ").upper()
    if inp_choice not in choice:
        print("Invalid character! Choose again.")
        char_choice()
    else:
        random_beginner=random.choice(choice)
        if random_beginner !=inp_choice:
            print("\nThe computer will go first.")
            start_com=random_beginner
            start_player = choice[1 - choice.index(random_beginner)]
            computer(start_com, inp_choice)
        else:
            start_player = random_beginner
            start_com = choice[1 - choice.index(random_beginner)]
            print("\nThe player will go first.")
            human_choice()
      
             
def human_choice():
    global start_com, start_player        
    while True:
        y=input("Choose a number ranging from 1-9: ")
        if not (y.isdigit()) or int(y) not in range(1, 10):
            print("Invalid Input! Choose again.")
            continue
        break    
    grid_update(y, None)
    print_grid()
    computer(start_com, start_player)
    
def grid_update(human_value, com_value):
        global x, s, index_grid, start_com, index_grid, start_player       
        index_grid={1: [0, 3], 2: [0, 10], 3: [0, 17], 4: [2, 3], 5: [2, 10], 6: [2, 17], 7: [4, 3], 8: [4, 10], 9: [4, 17]}
        if com_value is None:
            value_indexh=index_grid[int(human_value)]
            a, b = value_indexh
            if x[a][b] in [start_player, start_com]:
                print("Invalid Input! Choose again.")
                human_choice()
            else:
                x[a] = x[a][:b] + start_player + x[a][b + 1:]    
        else:
            value_indexc=index_grid[int(com_value)]
            c, d = value_indexc
            x[c] = x[c][:d] + start_com + x[c][d+1:]
        return x        
             
def center_free():
    global x
    return x[2][10] not in ["X", "O"]

def corner_start():
     global player_list, com_list
     if len(player_list) ==1 and len(com_list)==0:
                        if player_list[0] in [1, 3, 7, 9]:
                            if player_list[0] ==1:
                                return grid_update(None, 9)
                            elif player_list[0] ==3:
                                return grid_update(None, 7)
                            elif player_list[0] ==7:
                                return grid_update(None, 3)
                            elif player_list[0] ==9:
                                return grid_update(None, 1)                                                                                          
                        
def pos_free(pos):
    global index_grid, x
    z=index_grid[pos[0]]
    print(z)
    print("test:", x[z[0]][z[1]])
    test=x[z[0]][z[1]]
    if test != "X" and test !="O":
        return True
    else:
        return False    
            
def computer(start_com, start_player):
    global s
    print("f", start_com)
    if s ==1 and corner_start() is not None:
        print_grid()
        human_choice()
    elif s ==0 or s==1 and center_free():
        grid_update(None, 5)
        print_grid()
        human_choice()   
    else:
            result=com_move()    
            print_grid()
            human_choice()  
    # if human first, then look at possible combinations for human and block, if center is free then go center, then if human has two places try to block it ...   

def com_move():
    global com_list, player_list, index_grid, win_options, possible_moves_com, possible_moves_player
    print("tytz")
    possible_moves_com=[]
    possible_moves_player=[]
    #firstelm=x_list[0]
   
    for elm in win_options:
        for elmnt in elm:
            if elmnt in com_list:
                possible_moves_com.append(win_options.index(elm))
                
            if elmnt in player_list:
                possible_moves_player.append(win_options.index(elm))
    both=[num for num in possible_moves_com if num in possible_moves_player]
    print("Both: ", both)
    possible_moves_player=[o for o in possible_moves_player if o not in both]
    possible_moves_com=[j for j in possible_moves_com if j not in both]
    
    print("Bothx: ", both)
    print("Com: ",possible_moves_com,"Player: " ,possible_moves_player)
    good_block=[t for t in possible_moves_player if possible_moves_player.count(t) == 2 ]
    good_move=[l for l in possible_moves_com if possible_moves_com.count(l) == 2]
    
    if good_move:
        result=good_movef(com_list, good_move, possible_moves_com, win_options)
        if result is not None:
            return result
            print("see: ",result)       
    if good_block:
        result=good_blockf(player_list, good_block, possible_moves_player, win_options)
        if result is not None:
            return result
            print("see: ",result)       
    if both:
        result=both_possible_moves(both, possible_moves_com, possible_moves_player, player_list, com_list, win_options)
        if result is not None:
            return result
            print("see: ",result)       
    result=random_choice_player(possible_moves_player, player_list, win_options)             
    if result is not None:
        return result    
        print("see: ",result)               
    result=random_choice_com(possible_moves_com, com_list, win_options)
    if result is not None:
        return result
        print("see: ",result)           
        
def good_movef(com_list, good_move, possible_moves_com, win_options):        
        d=-2
        for g in good_move:
            d+=2
            if d >= len(good_move)-1:
                break 
            if g == good_move[d]:
                com_list=set(com_list)
                win_options[good_move[d]]=set(win_options[good_move[d]])
                print(com_list, win_options[good_move[d]])
                position=win_options[good_move[d]].difference(com_list)
                com_list=list(com_list)
                win_options[good_move[d]]=set(win_options[good_move[d]])
                position=list(position)
                print(position[0], "Good move")
                if not (pos_free(position)):
                     print("fail")
                     possible_moves_player.remove(g)
                     possible_moves_player.remove(g)   
                    
                elif pos_free(position):
                     print("wwwwwwwww")
                     return grid_update(None, position[0])    
                        
def good_blockf(player_list, good_block, possible_moves_player, win_options):
        p=-2
        for r in good_block:
            p+=2
            if p >= len(good_block)-1:
                break 
            if r == good_block[p]:
                player_list=set(player_list)
                win_options[good_block[p]]=set(win_options[good_block[p]])
                print(player_list, win_options[good_block[p]])
                position=win_options[good_block[p]].difference(player_list)
                player_list=list(player_list)
                win_options[good_block[p]]=list(win_options[good_block[p]])
                position=list(position)
                print(position[0], "Good block")
                if not (pos_free(position)):
                     print("fail")
                     possible_moves_player.remove(r)
                     possible_moves_player.remove(r)   
                    
                elif pos_free(position):
                     print("wwwwwwwww")
                     return grid_update(None, position[0])                    
                     
def both_possible_moves(both, possible_moves_com, possible_moves_player, player_list, com_list, win_options):                     
        u=-1                   
        while len(both) <=1:
                    u+=1
                    player_list=set(player_list)
                    win_options[both[u]]=set(win_options[both[u]])
                    position=win_options[both[u]].difference(player_list)
                    position=list(position)
                    player_list=list(player_list)
                    win_options[both[u]]=list(win_options[both[u]])
                    position=[pos for pos in position if pos not in com_list]
                    print(position)
                    print(position[0], "both move")
                    if not(pos_free(position)):
                          del both[u]          
                    elif pos_free(position):
                       return grid_update(None, position[0])                                  
                    
def random_choice_com(possible_moves_com, com_list, win_options):                       
    while possible_moves_com:
        v=random.choice(possible_moves_com)                  
        com_list=set(com_list)
        win_options[v]=set(win_options[v])
        position=win_options[v].difference(com_list)
        position=list(position)
        com_list=list(com_list)
        win_options[v]=list(win_options[v])
        print(position[0], "com move")
        if not(pos_free(position)):
                       del position[0]
                       if not(position):
                           possible_moves_com.remove(v)
                       else:
                           if not(pos_free(position)):
                               possible_moves_com.remove(v)
                           elif pos_free(position):
                               return grid_update(None, position[0])
                                                                                                                      
        elif pos_free(position):
                       return grid_update(None, v)
                                                                 
def random_choice_player(possible_moves_player, player_list, win_options):                                              
    while possible_moves_player:
        w=random.choice(possible_moves_player)           
        player_list=set(player_list)
        win_options[w]=set(win_options[w])
        position=win_options[w].difference(player_list)
        position=list(position)
        player_list=list(player_list)
        win_options[w]=list(win_options[w])
        print(position[0], "player move")
        if not(pos_free(position)):
                       del position[0]
                       if not(position):
                           possible_moves_player.remove(w)
                       else:
                           if not(pos_free(position)):
                               possible_moves_player.remove(w)
                           elif pos_free(position):
                               return grid_update(None, position[0])
                                                                                                                      
        elif pos_free(position):
                       return grid_update(None, position[0])  

def check_win():
    print("moin")
    global x, s, index_grid, com_list, player_list, win_options, start_com, start_player
    win_options=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    com_list=[]
    player_list=[]
    for pos, [row, col] in index_grid.items():
        if x[row][col] == start_player:
            player_list.append(pos)
        if x[row][col] == start_com:
            com_list.append(pos)               

    print("com: ",com_list,"player: ", player_list)                           
                  
    # 1, 2, 3 or 4, 5, 6 or 7, 8, 9 or 1, 4, 7 or 2, 5, 8, or 3, 6, 9 or 1, 5, 9 or 3, 5, 7
    for sublist in win_options:
        if all(element in player_list for element in sublist):
            print("Player won!")        
            play_again()                                 
        elif all(element in com_list for element in sublist):
            print("Computer won!")        
            play_again()                                 
    if s == 9:
        print("It's a tie!")       
        play_again()
        
def play_again():
            r=input("Play again? (y/n): ").lower()
            if r == "y":
                start()
            else:
                exit()
start()          