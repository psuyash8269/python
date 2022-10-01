n=7
i=1
while i<n:
  j=1
  while j<=i:
    if j==1:
      print("$",end="")
    elif j==2:
      print("#",end="")
    elif j==3:
      print("@",end="")
    elif j==4:
      print("!",end="")
    elif j==5:
      print("2",end="")
    else:
      print("1",end="")
    j+=1
  print()
  i+=1