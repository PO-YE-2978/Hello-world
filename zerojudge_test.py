a=list(map(int,input().split(' ')))
total=0
s=[]
q=[]
for i in range(a[0]):
    m=0
    c=[0 for i in range(a[1])]
    e=[]
    b=input().split(' ')
    for j in range(a[1]):
        c[j]=int(b[j])
        m=max(m,c[j])
    total+=m
    s.append(int(m))
    
for i in range(a[0]):
    if total%s[i] == 0:
        q.append(str(s[i]))
print(total)
if len(q) == 0:
    print('-1')
else:
    print(' '.join(q))
