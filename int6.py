str = '[][][]()(){(([(])))}'
s = []
fl = True

for ch in str:
        if ch in ('(', '[', '{'):
            s.append(ch)
        else:
            if ch == ')' and s[-1] == '(':
                s.pop()
            elif ch == ']' and s[-1] == '[':
                s.pop()
            elif ch == '}' and s[-1] == '{':
                s.pop()
            else:
                print('False')
                break

else:
    print('True')