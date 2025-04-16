x = input()
c = 0
d = 0
for m in x:
    c = c + 1 if m == '1' else 0
    d = d + 1 if m == '0' else 0
    if c == 7 or d == 7:
        print("YES")
        break
else:
    print("NO")