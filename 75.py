r1=list(input())
if len(r1)%2==0:
    r1[int(len(r1)/2)]='*'
    r1[int(len(r1)/2)-1]='*'
else:
    r1[int(len(r1)/2)]='*'
for i in range(len(r1)):
    print(r1[i],end='')
