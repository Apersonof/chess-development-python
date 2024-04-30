 
def Chess():
    
    n = 8
    BOARD = ChessSetup()
    for M in range(n):
        print(*BOARD[M])
def ChessSetup():
    blank = ['*','*','*','*','*','*','*','*']
    BOARD = [['r','b','n','q','k','n','b','r'],['p','p','p','p','p','p','p','p'],blank,blank,blank,blank,['P','P','P','P','P','P','P','P'],['R','B','N','Q','K','N','B','R']]
    return BOARD
    

Chess()
            
