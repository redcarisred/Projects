def printBoard(l):
    print('                                                ')
    print('Column Column Column Column Column Column Column')
    print('   1      2      3      4      5      6      7')
    print('------------------------------------------------')
    print('|  '+l[0]+'  |  '+l[6]+'  |  '+l[12]+'  |  '+l[18]+'  |  '+l[24]+'  |  '+l[30]+'  |  '+l[36]+'  |')
    print('------------------------------------------------')
    print('|  '+l[1]+'  |  '+l[7]+'  |  '+l[13]+'  |  '+l[19]+'  |  '+l[25]+'  |  '+l[31]+'  |  '+l[37]+'  |')
    print('------------------------------------------------')
    print('|  '+l[2]+'  |  '+l[8]+'  |  '+l[14]+'  |  '+l[20]+'  |  '+l[26]+'  |  '+l[32]+'  |  '+l[38]+'  |')
    print('------------------------------------------------')
    print('|  '+l[3]+'  |  '+l[9]+'  |  '+l[15]+'  |  '+l[21]+'  |  '+l[27]+'  |  '+l[33]+'  |  '+l[39]+'  |')
    print('------------------------------------------------')
    print('|  '+l[4]+'  |  '+l[10]+'  |  '+l[16]+'  |  '+l[22]+'  |  '+l[28]+'  |  '+l[34]+'  |  '+l[40]+'  |')
    print('------------------------------------------------')
    print('|  '+l[5]+'  |  '+l[11]+'  |  '+l[17]+'  |  '+l[23]+'  |  '+l[29]+'  |  '+l[35]+'  |  '+l[41]+'  |')
    print('------------------------------------------------')

def check(l, n):
    # Checking vertically
    if l[0] == n and l[1] == n and l[2] == n and l[3] == n:
        return True
    elif l[1] == n and l[2] == n and l[3] == n and l[4]== n:
        return True
    elif l[2] == n and l[3] == n and l[4] == n and l[5] == n:
        return True
    
    elif l[6] == n and l[7] == n and l[8] == n and l[9] == n:
        return True
    elif l[7] == n and l[8] == n and l[9] == n and l[10] == n:
        return True
    elif l[8] == n and l[9] == n and l[10] == n and l[11] == n:
        return True

    elif l[12] == n and l[13] == n and l[14] == n and l[15] == n:
        return True
    elif l[13] == n and l[14] == n and l[15] == n and l[16] == n:
        return True
    elif l[14] == n and l[15] == n and l[16] == n and l[17] == n:
        return True

    elif l[18] == n and l[19] == n and l[20] == n and l[21] == n:
        return True
    elif l[19] == n and l[20]== n and l[21] == n and l[22] == n:
        return True
    elif l[20] == n and l[21] == n and l[22] == n and l[23] == n:
        return True

    elif l[24] == n and l[25] == n and l[26] == n and l[27] == n:
        return True
    elif l[25] == n and l[26] == n and l[27] == n and l[28] == n:
        return True
    elif l[26] == n and l[27] == n and l[28] == n and l[29] == n:
        return True

    elif l[30] == n and l[31] == n and l[32] == n and l[33] == n:
        return True
    elif l[31] == n and l[32] == n and l[33] == n and l[34] == n:
        return True
    elif l[32] == n and l[33] == n and l[34] == n and l[35] == n:
        return True

    elif l[36] == n and l[37] == n and l[38] == n and l[39] == n:
        return True
    elif l[37] == n and l[38] == n and l[39] == n and l[40] == n:
        return True
    elif l[38] == n and l[39] == n and l[40] == n and l[41] == n:
        return True

    # Checking horizantally

    elif l[0] == n and l[6] == n and l[12] == n and l[18] == n:
        return True
    elif l[6] == n and l[12] == n and l[18] == n and l[24] == n:
        return True
    elif l[12] == n and l[18] == n and l[24] == n and l[30] == n:
        return True
    elif l[18] == n and l[24] == n and l[30] == n and l[36] == n:
        return True

    elif l[1] == n and l[7] == n and l[13] == n and l[19] == n:
        return True
    elif l[7] == n and l[13] == n and l[19] == n and l[25] == n:
        return True
    elif l[13] == n and l[19] == n and l[25] == n and l[31] == n:
        return True
    elif l[19] == n and l[25] == n and l[31] == n and l[37] == n:
        return True

    elif l[2] == n and l[8] == n and l[14] == n and l[20] == n:
        return True
    elif l[8] == n and l[14] == n and l[20] == n and l[26] == n:
        return True
    elif l[14] == n and l[20] == n and l[26] == n and l[32] == n:
        return True
    elif l[20] == n and l[26] == n and l[32] == n and l[38] == n:
        return True

    elif l[3] == n and l[9] == n and l[15] == n and l[21] == n:
        return True
    elif l[9] == n and l[15] == n and l[21] == n and l[27] == n:
        return True
    elif l[15] == n and l[21] == n and l[27] == n and l[33] == n:
        return True
    elif l[21] == n and l[27] == n and l[33] == n and l[39] == n:
        return True

    elif l[4] == n and l[10] == n and l[16] == n and l[22] == n:
        return True
    elif l[10] == n and l[16] == n and l[22] == n and l[28] == n:
        return True
    elif l[16] == n and l[22] == n and l[28] == n and l[34] == n:
        return True
    elif l[22] == n and l[28] == n and l[34] == n and l[40] == n:
        return True

    elif l[5] == n and l[11] == n and l[17] == n and l[23] == n:
        return True
    elif l[11] == n and l[17] == n and l[23] == n and l[29] == n:
        return True
    elif l[17] == n and l[23] == n and l[29] == n and l[35] == n:
        return True
    elif l[23] == n and l[29] == n and l[35] == n and l[41] == n:
        return True

    # Checking diagonally

    elif l[0] == n and l[7] == n and l[14] == n and l[21] == n:
        return True
    elif l[1] == n and l[8] == n and l[15] == n and l[22] == n:
        return True
    elif l[2] == n and l[9] == n and l[16] == n and l[23] == n:
        return True
    elif l[3] == n and l[8] == n and l[13] == n and l[18] == n:
        return True
    elif l[4] == n and l[9] == n and l[14] == n and l[19] == n:
        return True
    elif l[5] == n and l[10] == n and l[15] == n and l[20] == n:
        return True
    
    elif l[6] == n and l[13] == n and l[20] == n and l[27] == n:
        return True
    elif l[7] == n and l[14] == n and l[21] == n and l[28] == n:
        return True
    elif l[8] == n and l[15] == n and l[22] == n and l[29] == n:
        return True
    elif l[9] == n and l[14] == n and l[19] == n and l[24] == n:
        return True
    elif l[10] == n and l[15] == n and l[20] == n and l[25] == n:
        return True
    elif l[11] == n and l[16] == n and l[21] == n and l[26] == n:
        return True
    
    elif l[12] == n and l[19] == n and l[26] == n and l[33] == n:
        return True
    elif l[13] == n and l[20] == n and l[27] == n and l[34] == n:
        return True
    elif l[14] == n and l[21] == n and l[28] == n and l[35] == n:
        return True
    elif l[15] == n and l[20] == n and l[25] == n and l[30] == n:
        return True
    elif l[16] == n and l[21] == n and l[26] == n and l[31] == n:
        return True
    elif l[17] == n and l[22] == n and l[27] == n and l[32] == n:
        return True

    elif l[18] == n and l[25] == n and l[32] == n and l[39] == n:
        return True
    elif l[18] == n and l[13] == n and l[8] == n and l[3] == n:
        return True
    elif l[19] == n and l[26] == n and l[33] == n and l[40] == n:
        return True
    elif l[19] == n and l[14] == n and l[9] == n and l[4] == n:
        return True
    elif l[20] == n and l[27] == n and l[34] == n and l[41] == n:
        return True
    elif l[20] == n and l[15] == n and l[10] == n and l[5] == n:
        return True
    elif l[21] == n and l[26] == n and l[31] == n and l[36] == n:
        return True
    elif l[21] == n and l[14] == n and l[7] == n and l[0] == n:
        return True
    elif l[22] == n and l[27] == n and l[32] == n and l[37] == n:
        return True
    elif l[22] == n and l[15] == n and l[8] == n and l[1] == n:
        return True
    elif l[23] == n and l[28] == n and l[33] == n and l[38] == n:
        return True
    elif l[23] == n and l[16] == n and l[9] == n and l[2] == n:
        return True

    elif l[24] == n and l[19] == n and l[14] == n and l[9] == n:
        return True
    elif l[25] == n and l[20] == n and l[15] == n and l[10] == n:
        return True
    elif l[26] == n and l[21] == n and l[16] == n and l[11] == n:
        return True
    elif l[27] == n and l[20] == n and l[13] == n and l[6] == n:
        return True
    elif l[28] == n and l[21] == n and l[22] == n and l[7] == n:
        return True
    elif l[29] == n and l[22] == n and l[23] == n and l[8] == n:
        return True

    elif l[30] == n and l[25] == n and l[20] == n and l[15] == n:
        return True
    elif l[31] == n and l[26] == n and l[21] == n and l[16] == n:
        return True
    elif l[32] == n and l[27] == n and l[22] == n and l[17] == n:
        return True
    elif l[33] == n and l[26] == n and l[19] == n and l[12] == n:
        return True
    elif l[34] == n and l[27] == n and l[20] == n and l[13] == n:
        return True
    elif l[35] == n and l[28] == n and l[21] == n and l[14] == n:
        return True

    elif l[36] == n and l[31] == n and l[26] == n and l[21] == n:
        return True
    elif l[37] == n and l[32] == n and l[27] == n and l[22] == n:
        return True
    elif l[38] == n and l[33] == n and l[28] == n and l[23] == n:
        return True
    elif l[39] == n and l[32] == n and l[25] == n and l[18] == n:
        return True
    elif l[40] == n and l[33] == n and l[26] == n and l[19] == n:
        return True
    elif l[41] == n and l[34] == n and l[27] == n and l[20] == n:
        return True
    
    return False
print('Welcome to Connect 4!')
ask = input('Want to play? Yes or no: ')
if ask.lower() == 'yes':
    columns = ['1','2','3','4','5','6','7']
    l = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42']
    player1 = input('Player 1 name (You will be \'X\'): ')
    player2 = input('Player 2 name (You will be \'O\'): ')
    print('%s will go first!'%player1)
    # Gameplay
    printBoard(l)
    while True:
        # Player 1
        print('It is %s\'s turn!'%player1)
        column = input('Which column do you want to place your checker in? ')
        # Placing down checker
        try:
            column = int(column)
        except:
            assert False, 'That is not a number!'
        assert str(column) in columns, 'That is not a column!'
        if column == 1:
            assert l[0] != 'X' and l[0] != 'O','That column is full!'
            if l[1] == 'X' or l[1] == 'O':
                l[0] = 'X'
            elif l[2] == 'X' or l[2] == 'O':
                l[1] = 'X'
            elif l[3] == 'X' or l[3] == 'O':
                l[2] = 'X'
            elif l[4] == 'X' or l[4] == 'O':
                l[3] = 'X'
            elif l[5] == 'X' or l[5] == 'O':
                l[4] = 'X'
            else:
                l[5] = 'X'
        elif column == 2:
            assert l[6] != 'X' and l[6] != 'O','That column is full!'
            if l[7] == 'X' or l[17] == 'O':
                l[6] = 'X'
            elif l[8] == 'X' or l[8] == 'O':
                l[7] = 'X'
            elif l[9] == 'X' or l[9] == 'O':
                l[8] = 'X'
            elif l[10] == 'X' or l[10] == 'O':
                l[9] = 'X'
            elif l[11] == 'X' or l[11] == 'O':
                l[10] = 'X'
            else:
                l[11] = 'X'
        elif column == 3:
            assert l[12] != 'X' and l[12] != 'O','That column is full!'
            if l[13] == 'X' or l[13] == 'O':
                l[12] = 'X'
            elif l[14] == 'X' or l[14] == 'O':
                l[13] = 'X'
            elif l[15] == 'X' or l[15] == 'O':
                l[14] = 'X'
            elif l[16] == 'X' or l[16] == 'O':
                l[15] = 'X'
            elif l[17] == 'X' or l[17] == 'O':
                l[16] = 'X'
            else:
                l[17] = 'X'
        elif column == 4:
            assert l[18] != 'X' and l[18] != 'O','That column is full!'
            if l[19] == 'X' or l[19] == 'O':
                l[18] = 'X'
            elif l[20] == 'X' or l[20] == 'O':
                l[19] = 'X'
            elif l[21] == 'X' or l[21] == 'O':
                l[20] = 'X'
            elif l[22] == 'X' or l[22] == 'O':
                l[21] = 'X'
            elif l[23] == 'X' or l[23] == 'O':
                l[22] = 'X'
            else:
                l[23] = 'X'
        elif column == 5:
            assert l[24] != 'X' and l[24] != 'O','That column is full!'
            if l[25] == 'X' or l[25] == 'O':
                l[24] = 'X'
            elif l[26] == 'X' or l[26] == 'O':
                l[25] = 'X'
            elif l[27] == 'X' or l[27] == 'O':
                l[26] = 'X'
            elif l[28] == 'X' or l[28] == 'O':
                l[27] = 'X'
            elif l[29] == 'X' or l[29] == 'O':
                l[28] = 'X'
            else:
                l[29] = 'X'
        elif column == 6:
            assert l[30] != 'X' and l[30] != 'O','That column is full!'
            if l[31] == 'X' or l[31] == 'O':
                l[30] = 'X'
            elif l[32] == 'X' or l[32] == 'O':
                l[31] = 'X'
            elif l[33] == 'X' or l[33] == 'O':
                l[32] = 'X'
            elif l[34] == 'X' or l[34] == 'O':
                l[33] = 'X'
            elif l[35] == 'X' or l[35] == 'O':
                l[34] = 'X'
            else:
                l[35] = 'X'
        elif column == 7:
            assert l[36] != 'X' and l[36] != 'O','That column is full!'
            if l[37] == 'X' or l[37] == 'O':
                l[36] = 'X'
            elif l[38] == 'X' or l[38] == 'O':
                l[37] = 'X'
            elif l[39] == 'X' or l[39] == 'O':
                l[38] = 'X'
            elif l[40] == 'X' or l[40] == 'O':
                l[39] = 'X'
            elif l[41] == 'X' or l[41] == 'O':
                l[40] = 'X'
            else:
                l[41] = 'X'
        printBoard(l)
        if check(l,'X') == True:
            print('%s has won!'%player1)
            break
        # Player 2
        print('It is %s\'s turn!'%player2)
        column = input('Which column do you want to place your checker in? ')
        # Placing down checker
        try:
            column = int(column)
        except:
            assert False, 'That is not a number!'
        assert str(column) in columns, 'That is not a column!'
        if column == 1:
            assert l[0] != 'X' and l[0] != 'O','That column is full!'
            if l[1] == 'X' or l[1] == 'O':
                l[0] = 'O'
            elif l[2] == 'X' or l[2] == 'O':
                l[1] = 'O'
            elif l[3] == 'X' or l[3] == 'O':
                l[2] = 'O'
            elif l[4] == 'X' or l[4] == 'O':
                l[3] = 'O'
            elif l[5] == 'X' or l[5] == 'O':
                l[4] = 'O'
            else:
                l[5] = 'O'
        elif column == 2:
            assert l[6] != 'X' and l[6] != 'O','That column is full!'
            if l[7] == 'X' or l[7] == 'O':
                l[6] = 'O'
            elif l[8] == 'X' or l[8] == 'O':
                l[7] = 'O'
            elif l[9] == 'X' or l[9] == 'O':
                l[8] = 'O'
            elif l[10] == 'X' or l[10] == 'O':
                l[9] = 'O'
            elif l[11] == 'X' or l[11] == 'O':
                l[10] = 'O'
            else:
                l[11] = 'O'
        elif column == 3:
            assert l[12] != 'X' and l[12] != 'O','That column is full!'
            if l[13] == 'X' or l[13] == 'O':
                l[12] = 'O'
            elif l[14] == 'X' or l[14] == 'O':
                l[13] = 'O'
            elif l[15] == 'X' or l[15] == 'O':
                l[14] = 'O'
            elif l[16] == 'X' or l[16] == 'O':
                l[15] = 'O'
            elif l[17] == 'X' or l[17] == 'O':
                l[16] = 'O'
            else:
                l[17] = 'O'
        elif column == 4:
            assert l[18] != 'X' and l[18] != 'O','That column is full!'
            if l[19] == 'X' or l[19] == 'O':
                l[18] = 'O'
            elif l[20] =='X' or l[20] == 'O':
                l[19] = 'O'
            elif l[21] == 'X' or l[21] == 'O':
                l[20] = 'O'
            elif l[22] == 'X' or l[22] == 'O':
                l[21] = 'O'
            elif l[23] == 'X' or l[23] == 'O':
                l[22] = 'O'
            else:
                l[23] = 'O'
        elif column == 5:
            assert l[24] != 'X' and l[24] != 'O','That column is full!'
            if l[25] == 'X' or l[25] == 'O':
                l[24] = 'O'
            elif l[26] == 'X' or l[26] == 'O':
                l[25] = 'O'
            elif l[27] == 'X' or l[27] == 'O':
                l[26] = 'O'
            elif l[28] == 'X' or l[28] == 'O':
                l[27] = 'O'
            elif l[29] == 'X' or l[29] == 'O':
                l[28] = 'O'
            else:
                l[29] = 'O'
        elif column == 6:
            assert l[30] != 'X' and l[30] != 'O','That column is full!'
            if l[31] == 'X' or l[31] == 'O':
                l[30] = 'O'
            elif l[32] == 'X' or l[32] == 'O':
                l[31] = 'O'
            elif l[33] == 'X' or l[33] == 'O':
                l[32] = 'O'
            elif l[34] == 'X' or l[34] == 'O':
                l[33] = 'O'
            elif l[35] == 'X' or l[35] == 'O':
                l[34] = 'O'
            else:
                l[35] = 'O'
        elif column == 7:
            assert l[36] != 'X' and l[36] != 'O','That column is full!'
            if l[37] == 'X' or l[37] == 'O':
                l[36] = 'O'
            elif l[38] == 'X' or l[38] == 'O':
                l[37] = 'O'
            elif l[39] == 'X' or l[39] == 'O':
                l[38] = 'O'
            elif l[40] == 'X' or l[40] == 'O':
                l[39] = 'O'
            elif l[41] == 'X' or l[41] == 'O':
                l[40] = 'O'
            else:
                l[41] = 'O'
        printBoard(l)
        if check(l,'O') == True:
            print('%s has won!'%player2)
            break
else:
    print('...')

