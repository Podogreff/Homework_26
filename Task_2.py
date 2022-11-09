
stack = []
flag = True
string = input("Please enter your string: ")

for i in string:
    if i in "([{":
        stack.append(i)
    elif i in ")]}":
        if len(stack) == 0:
            flag = False
            break

        last = stack.pop()
        if last == "(" and i == ")":
            continue
        if last == "[" and i == "]":
            continue
        if last == "{" and i == "}":
            continue

        flag = False
        break

    else:
        print("Please enter only '(){}[]' symbols!")
        break

for i in string:
    if i in "([{":
        if flag and len(stack) == 0:
            print(f"The string '{string}' is balanced")
            break
        else:
            print(f"The string '{string}' is not balanced")
            break