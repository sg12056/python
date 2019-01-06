from IPython.display import clear_output

clear = lambda: os.system('cls')

inputoptions = ['X','O']
gameInProgg = False

def pat(args):
    
    a = ' {0} | {1} | {2}  \n-----------\n {3} | {4} | {5}  \n-----------\n {6} | {7} | {8}'.format(args[0],args[1],
                                                                                                   args[2],args[3],args[4],
                                                                                                   args[5],args[6],args[7],
                                                                                                   args[8])
    
    return a

def winner(player,data,playerChoice):
    if (data['1']+data['2']+data['3'] == playerChoice*3
       or data['4']+data['5']+data['6'] == playerChoice*3
       or data['7']+data['8']+data['9'] == playerChoice*3
       or data['1']+data['4']+data['7'] == playerChoice*3
       or data['2']+data['5']+data['8'] == playerChoice*3
       or data['3']+data['6']+data['9'] == playerChoice*3
       or data['1']+data['5']+data['9'] == playerChoice*3
       or data['3']+data['5']+data['7'] == playerChoice*3):
        print(f'Congrats!! {player} , You won!! ')
        return True
    return False

p2 = inputoptions[0]

p1 = input('P1 : Do you choose X or O ? : ').upper()

if(p1.upper() in inputoptions and p1.upper() == inputoptions[0]):
    p2 = inputoptions[1]

print(f'Player 1 : {p1} , Player 2 : {p2} and the board orentation is :')    
    
print(pat([1,2,3,4,5,6,7,8,9]))


start = input('Shall we start? yes or no ? : ')
clear_output(wait=True)
if(start.lower() == 'yes'):
    gameInProgg = True

data ={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
i=0
while gameInProgg :
    
    
    i1 = input('P1 : Choose position (1-9) : ')
    data[i1] = p1
    clear_output(wait=True)
    print(pat(list(data.values())))
    i+=1
    if( winner('P1',data,p1) or i >= 9):
        #play_again = input('Do you want to play again')
        gameInProgg = False
        if(i >= 9):
            print('Its a Tie...')
        break
    
 
    i2 = input('P2 : Choose position (1-9) : ')
    data[i2] = p2
    clear_output(wait=True)
    print(pat(list(data.values())))
    i+=1
    if( winner('P2',data,p2) or i >= 9):
        gameInProgg = False
        if(i >= 9):
            print('Its a Tie...')
        break

print('Game Concluded...')
