def sum(a, b, c):
    return a + b + c

def printgrid(p1, p2):
    zero = 'X' if p1[0] else ('O' if p2[0] else 0)
    one = 'X' if p1[1] else ('O' if p2[1] else 1)
    two = 'X' if p1[2] else ('O' if p2[2] else 2)
    three = 'X' if p1[3] else ('O' if p2[3] else 3)
    four = 'X' if p1[4] else ('O' if p2[4] else 4)
    five = 'X' if p1[5] else ('O' if p2[5] else 5)
    six = 'X' if p1[6] else ('O' if p2[6] else 6)
    seven = 'X' if p1[7] else ('O' if p2[7] else 7)
    eight = 'X' if p1[8] else ('O' if p2[8] else 8) 

    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")

def checkwin(p1, p2):
    poss = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for win in poss:  # win=[0,1,2]
        if sum(p1[win[0]], p1[win[1]], p1[win[2]]) == 3:
            print('Hurray, X won !!!!!!!!')
            return 1
        elif sum(p2[win[0]], p2[win[1]], p2[win[2]]) == 3:
            print('Hurray, O won !!!!!!!!')
            return 0
    return -1

def main():
    p1 = [0] * 9
    p2 = [0] * 9
    turn = 1
    moves = 0
    printgrid(p1, p2)  

    while True:
        if turn == 1:
            print("X's chance")
            val = int(input("Enter a value (0-8): "))
            
            if 0 <= val < 9 and p1[val] == 0 and p2[val] == 0:
                p1[val] = 1
                moves += 1
                turn = 0
            else:
                print("Position already taken or out of range, try again.")
        else:
            print("O's chance")
            val = int(input("Enter a value (0-8): "))
            if 0 <= val < 9 and p1[val] == 0 and p2[val] == 0:
                p2[val] = 1
                moves += 1
                turn = 1
            else:
                print("Position already taken or out of range, try again.")

        printgrid(p1, p2)
        cwin = checkwin(p1, p2)
        if cwin != -1:
            print("Match over")
            break
        elif moves == 9:
            print("Oh, it's a tie!")
            break

if __name__ == '__main__':
    main()
