# Enter your code here. Read input from STDIN. Print output to STDOUT


s = ""
undos = []  # stack for operation 1 & 2
for _ in range(int(input().strip())):
    oper = input().split(" ")
    cmd = oper[0]
    if cmd == "1":
        appendices = oper[1]
        undos.append({2: len(appendices)})  # add size of last few added characters for deletion in undo
        s += appendices
    elif cmd == "2":
        deletion = s[-int(oper[1]):]
        undos.append({1: deletion})  # add last few deleted characters for appending in undo
        s = s[:-(int(oper[1]))]
    elif cmd == "3":
        print(s[int(oper[1]) - 1])
    elif cmd == "4":
        undo = undos.pop()
        if 1 in undo:
            s += undo[1]
        else:
            s = s[:-undo[2]]
