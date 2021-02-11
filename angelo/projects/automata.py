def decision_tree(inputs):
    if inputs[0] == False:
        if inputs[1] == False:
            if inputs[2] == False:
                return False
            else:
                return False
        else:
            if inputs[2] == False:
                return False
            else:
                return False
    else:
        if inputs[1] == False:
            if inputs[2] == False:
                return True
            else:
                return True
        else:
            if inputs[2] == False:
                return True
            else:
                return False
                
def step(inputs):
    # pad with 0s on either edge
    inputs = [False] + inputs + [False]
    outputs = []
    # construct output
    for i in range(len(inputs) - 2):
        outputs.append(decision_tree(inputs[i: i + 3]))
    return outputs
    
    
def run(inputs, n):
    for i in range(n):
        inputs = step(inputs)
        render(inputs)
    return inputs
    
def render(inputs):
    graphics.clear()
    length = graphics.width / len(inputs)
    for i in range(len(inputs)):
        if inputs[i]:
            graphics.drawRect(i * length, 0, (i + 1) * length, length, 255, 255, 255)
    graphics.sleep(1000)
        
    
print(run([False, True, True, True, False, True, False, True, True, False], 10))