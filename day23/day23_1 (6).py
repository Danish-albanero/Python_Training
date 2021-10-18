def calPoints(ops):
    history = []
    for op in ops:
        if op == '+':
            history.append(history[-1] + history[-2])
        elif op == 'D':
            history.append(history[-1] * 2)
        elif op == 'C':
            history.pop()
        else:
            history.append(int(op))
        return sum(history)


ops = ["5","2","C","D","+"]
print(calPoints(ops))
