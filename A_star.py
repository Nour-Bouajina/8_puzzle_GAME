import copy
 
initial_state = [[2, 8, 3], [1, 6, 4], [7, ' ', 5]]
#initial_state = [[1, 2, 3], [8, 7, 5], [6, 0, 4]]
final_state = [[1, 2, 3], [8, ' ', 4], [7, 6, 5]]
bordesize = (3,3)
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
def Empty(state: list):
    for i in range(3):
        for j in range(3):
            if state[i][j]==' ':
                return i,j
 
def compareStates(state1 : list, state2 : list) -> bool:
    for i in range(bordesize[0]):
        for j in range(bordesize[1]):
            if state1[i][j] !=  state2[i][j]:
                   return False
    return True
 
def isfinal(state):
    return compareStates(state,final_state)
 
def number(state,x,y):
    return state[x][y] 
 
def permute(state , c1 , c2):
    temp = copy.deepcopy(state)
    x1,y1 = c1
    x2,y2 = c2
    try:
        temp[x1][y1] , temp[x2][y2] = temp[x2][y2] , temp[x1][y1]
    except:
            pass
    return temp

def move(state,m : list):
    x1,y1 = Empty(state)
    x2,y2 = x1+m[0],y1+m[1]
    generated = permute(state , (x1,y1) , (x2,y2))
    return generated

def succesors(state,moves):
    return [move(state,m) for m in moves]

def calculate_misplaced_tiles(state):
    misplaced_tiles = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != final_state[i][j]:
                misplaced_tiles += 1
    return misplaced_tiles

def get_best_state(states, depth):
    min_misplaced = float('inf')
    best_state = None
    for state in states:
        misplaced = calculate_misplaced_tiles(state)+ depth
        if misplaced < min_misplaced:
            min_misplaced = misplaced
            best_state = state
    return best_state


def afficher(state):
    border = '+---' * 3 + '+'
    for row in state:
        print(border)
        format_row = f"| {row[0] if row[0] else ' '} | {row[1]if row[1] else ' '} | {row[2] if row[2] else ' '} |"
        print(format_row)
    print(border)

def seen(state,openN,closeN):
    allN = openN+closeN
    for s in allN:
        if compareStates(state,s):
            return True
    return False

class A_star:
    def __init__(self, istate) -> None:
        self.freeNodes    = [istate]
        self.closedNondes = []
        self.sucess = False
        self.goal = istate
        self.states_explored =0
        self.show = []
        self.depth =0
    def inc(self):
        best = get_best_state(self.freeNodes, self.depth)
        self.show = best
        (self.freeNodes).remove(best)
        self.closedNondes.append(best)
        
        if isfinal(best):
                self.sucess = True
                self.goal = best
                self.show = best
                return
        
        self.depth += 1
        
        generated = succesors(best,moves)
        generated = [i for i in generated if not seen(i, self.freeNodes, self.closedNondes)]
        self.freeNodes = generated + self.freeNodes
        self.states_explored += len(generated)
        