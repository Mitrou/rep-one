c = ''
a = []
s = 'vsyakayazalupa'
for x in range(len(s)):
    try:
        if int(ord(s[x])) <= int(ord(s[x+1])):
            c += s[x]
            # print (c)
        else:
            c += s[x]
            a.append(c)
            c = ''
    except IndexError:
        c += s[x]
        a.append(c)
        break
res = []
maxlength = max(len(q) for q in a)
for i in a:
    if len(i) == maxlength:
        res.append(i)
print('Longest substring in alphabetical order is: ', res[0])
