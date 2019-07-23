value=list(input())
if len(value)%2==0:
    value[int(len(value)/2)]='*'
    value[int(len(value)/2)-1]='*'
else:
    value[int(len(value)/2)]='*'
for i in range(len(value)):
    print(value[i],end='')
