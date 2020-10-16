import random as rand
n=int(input("Enter Queens : "))
heu=n*(n-1)/2
oldHeu=heu+1
def print_board():
    for i in range(0,n):
        for j in range(0,n):
            print(board[i][j],end="\t")
        print()
        
def count_clashes():
    heu=n*(n-1)/2                          #Maximum clashes
    for curr_row in range(0,n): #FOR each row
        #print("***************************************")
        original=queen_pos[curr_row]
        for x in range(0,n):    #To change Q in every column
            ctr=0
            board[curr_row][original]='?'
            board[curr_row][x]='Q'
            queen_pos[curr_row]=x
            #print("\n Queen[",curr_row,"] placed at : ",x)
            #print_board()
                
            for row in range(0,n):   #To calculate Heuristic of Q placement
                col=queen_pos[row]
                #Checking conflicting queens in LOWER COLUMN
                if(row+1<n):
                    for i in range(row+1,n):
                        if(board[i][col]=='Q'):  #i=check all rows, col=same column
                            ctr=ctr+1 
                            #print("\n ",row," col [",i,"][",col,"]",end="")

                #Check conflicts in LOWER diagonal positions
                i=row+1
                j=col-1
                while(i<n and j>=0):      
                #LEFT diognal
                    if(board[i][j]=='Q'):
                        ctr=ctr+1
                        #print("\n ",row," ld [",i,"][",j,"]",end="")
                    i=i+1
                    j=j-1

                i=row+1
                j=col+1
                while(i<n and j<n):      
                #RIGHT diognal
                    if(board[i][j]=='Q'):
                        ctr=ctr+1
                        #print("\n ",row," rd [",i,"][",j,"]",end="")
                    i=i+1
                    j=j+1
                    
            #print("\n TOTAL CLASHES = ",ctr)
            board[curr_row][x]='?'
            board[curr_row][original]='Q'
            queen_pos[curr_row]=original
            if(ctr<heu):
                heu=ctr
                minRow=curr_row
                minHeuQueen=x
    if(heu<oldHeu):
        print("\nMinimum Heuristic at [",minRow,"][",minHeuQueen,"]"," with total Clashes=",heu)
        #change Queen's position as it has less heuristic
        board[minRow][queen_pos[minRow]]="?"
        board[minRow][minHeuQueen]="Q"
        queen_pos[minRow]=minHeuQueen
    return heu

if(n<=2):
    print("NO SOLUTION EXIST")
else:
    board = [["?" for i in range(0,n)] for j in range(0,n)]       #Initliazing board
    queen_pos=[0 for i in range(0,n)]
    for row in range(0,n):                                        #Random placement of Queens,each row will have exact one Q
        col=rand.randint(0,n-1)
        queen_pos[row]=col
        board[row][col]='Q'

    print_board()
    count=0
    while(heu!=0):
        heu=count_clashes()                                           #calculate heuristic
        if(heu<oldHeu):
            print_board()
        if(heu==0):
            print("Congrats! You have found the solution")
            break;
        if(heu==oldHeu):
            count=count+1
            break
        oldHeu=heu
