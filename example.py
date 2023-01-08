if __name__ == '__main__':
    states=[]
    transitions=[]
    initialState=[]
    alphabet=[]
    finalState=[]
    f=open("FA.txt", "r")
    
    input = f.read().split("\n") 
    for line in input:
        lines=line.split(">")
        left=lines[0]
        right=lines[1]  
        state=left.split(",")[0][1:]
        character=left.split(",")[1][0:-1]
        if state not in states:
            if state[0] == "{":
                state=state.replace("{", "").replace("}", "") 
                if state not in initialState:
                    initialState.append(state)
            states.append(state)
        if character not in alphabet:
            alphabet.append(character)
        if right[0] == "(":
            elem=right.replace("(", "").replace(")", "")
            if elem not in finalState:
                finalState.append(elem)
            if elem not in states:
                states.append(elem)
            transitions.append([state, elem])
        if right[0] == "[":
            elem = right.replace("[", "").replace("]", "")
            if elem not in states:
                states.append(elem)
            transitions.append([state, elem])

    print("Initial state: \n", initialState, "\n")
    print("States: \n", states, "\n")        
    print("Alphabet: \n", alphabet, "\n")
    print("Transitions: \n", transitions, "\n")
    print("Final states: \n", finalState, "\n")