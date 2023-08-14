str = '((('
s = []
fl = True

for i in range(len(str)):
        if str[i] in ('(', '[', '{'):
            s.append(str[i])
        else:
            if i == 0:
                print('False')
                break
            if str[i] == ')' and s[-1] == '(':
                s.pop()
            elif str[i] == ']' and s[-1] == '[':
                s.pop()
            elif str[i] == '}' and s[-1] == '{':
                s.pop()
            else:
                print('False')
                break

else:
    if s:
        print('False')
    else:
        print('True')
