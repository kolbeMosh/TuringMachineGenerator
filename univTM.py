# Written By: Kolbe Mosher
# Purpose: Emulates a universal Turing Machine
#          & Keeps track of every move it makes

class UniversalTuringMachine:
    def __init__(self, TMFile: str):
        self._TMFile = TMFile

    # Returns a tuple where the first value is whether the input
    # is accepted by the TM and the second is an array with the 
    # list of moves made used to render images of each state
    def accepts(self, s: str) -> tuple[bool, list]:
        moveSet = []

        parse = self._parseDelta()
        initial, blank, accept, delta = parse

        tape = s
        head = 0
        state = initial
    
        #Used to keep track of the order of moves for the photo rendering
        i = 0

        if head == len(tape):
            tape += blank

        while True:
            i += 1

            if state in accept:
                return ( True, moveSet )
            
            move = self._lookup_move(state, tape[head], delta)
            
            if not move:
                return ( False, moveSet )
            
            moveSet.append((self._TMFile, str(i), (state, tape[head], move[0], move[1], move[2])))

            new_state, symbol, direction = move        

            tape = tape[:head] + symbol + tape[head + 1:]

            # move the head
            if direction == 'L':
                if head == 0:
                    tape = blank + tape
                else:
                    head -= 1
            else:
                head += 1
                if head == len(tape):
                    tape += blank

            # update the state
            state = new_state

    def _lookup_move(self, state: int, symbol: chr, delta: dict) -> tuple:
        return delta.get((state, symbol))


    # Creates delta transitions [start, blank, [accepting states],transitions]
    def _parseDelta(self) -> tuple[int, str, list, dict]:
        
        # counter for line number
        i = 0

        delta = {}
        
        # Start State
        initial = None
        accepting = []
        B = None

        f = open(self._TMFile)
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if (i == 0):
                initial = line
            elif (i == 1):
                B = line
            elif (i == 2):
                accepting = [ char for char in line ]
            else:
                delta[(line[0], line[1])] = (line[2], line[3], line[4])

            i += 1
        
        return (initial, B, accepting, delta)