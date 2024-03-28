s = input()
# d = {'(':')', '[':']', '{':'}'}
stack = []
try:
    for i in s:
        if i=='(':
            stack.append(i)
        elif i==')':
            stack.pop()
        else:
            print("Invalid String!")
            break
except:
    print("Not balanced one!")

else:
    print("Balanced one!")
