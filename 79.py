r1,r2=map(int,input().split())
r3=r1*r2
for i in range(0,r3+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
