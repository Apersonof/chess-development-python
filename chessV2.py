 
def Chess():
    GameEnd = False
    n = 8
    BOARD = ChessSetup()
    for M in range(n):
        print(*BOARD[M])
    print("first character is piece [K, Q, B, N, R, P]")
    print("second character is initial column [a, b, c, d, e, f, g, h]")
    print("third character is initial row [1, 2, 3, 4, 5, 6, 7, 8]")
    print("fourth character if taking put x if not ignore")
    print("end phrase by pressing enter, example position: Ke5")
    print("input next phrase with the ending column and row, letter then number, ex: e6")
    while GameEnd == False:
        valid = False
        movenumber = 0
        while valid == False:
            movenumber += 1
            piecetheir = False
            while piecetheir == False:
                initialposition = input(f"initial position: ")
                finalposition = input("final position: ")
                if (initialposition[0] == BOARD[initialposition[1]][initialposition[2]] and movenumber%2!=0) or (initialposition[0].lower()== BOARD[initialposition[1]][initialposition[2]] and movenumber%2==0):
                    valid = MoveValidation(initialposition,finalposition,BOARD,movenumber)
                else: print("?!"); valid = False
        BOARD[initialposition[1]][initialposition[2]] = '*'
        BOARD[finalposition[0]][finalposition[1]] = initialposition[0]
def ChessSetup():
    blank = ['*','*','*','*','*','*','*','*']
    BOARD = [['r','b','n','q','k','n','b','r'],['p','p','p','p','p','p','p','p'],blank,blank,blank,blank,['P','P','P','P','P','P','P','P'],['R','B','N','Q','K','N','B','R']]
    return BOARD
def MoveValidation(string1,string2,BOARD,movenumber):
    valid = True
    if string1[0] == "K":
        if -1 <= string1[1] - string2[0] <=1:
            valid = True
        else: print("?!"); valid = False
    elif string1[0] == "p":
        white = True
        if movenumber%2!=0:
            white = True
        else: white = False
        try:
            string1[3] = 'x'

        except:
            if white == True:    
                if string1[2] == 2:
                    if string1[1] - string2[0] == 0:
                        if 2 >= string2[1] - string1[2] > 0:
                            valid = True
                        else: print("?!"); valid = False
                    else: print("?!"); valid = False
                else:
                    if string1[1] - string2[0] == 0:
                        if 1 == string2[1] - string1[2]:
                            valid = True
                        else: print("?!"); valid = False
                    else: print("?!"); valid = False
            else:
                if string1[2] == 7:
                    if string1[1] - string2[0] == 0:
                        if 2 >= string1[2] - string2[1] > 0:
                            valid = True
                        else: print("?!"); valid = False
                    else: print("?!"); valid = False
                else:
                    if string2[0] - string1[1] == 0:
                        if 1 == string1[2] - string2[1]:
                            valid = True
                        else: print("?!"); valid = False
                    else: print("?!"); valid = False
        


Chess()
            
