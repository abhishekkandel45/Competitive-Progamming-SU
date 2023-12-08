def towerOfHanoi(n):
    A = list(range(n, 0, -1))  # stack of disks on peg A
    B, C = [], []  # stacks of disks on pegs B and C
    moves = []  # list of moves made

    if n % 2 == 0:  # if number of disks is even, swap B and C
        B, C = C, B

    while len(C) != n:
        move(A, B, moves, 'A', 'B')
        if len(C) == n:
            break
        move(A, C, moves, 'A', 'C')
        if len(C) == n:
            break
        move(B, C, moves, 'B', 'C')

    return moves

def move(source, target, moves, source_name, target_name):
    if len(source) > 0 and (len(target) == 0 or target[-1] > source[-1]):
        target.append(source.pop())
        moves.append([source_name, target_name])
    elif len(target) > 0 and (len(source) == 0 or source[-1] > target[-1]):
        source.append(target.pop())
        moves.append([target_name, source_name])