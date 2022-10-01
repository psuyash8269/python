#write a program to check amongstrong no.
num=int(input("Enter the no that you want to check : "))
p=num
sum=0
while num>0:
  k=num%10
  sum=sum+k*k*k
  num=num//10
if p==sum:
  print("Entered no is amongstrong :")
else:
  print("Entered no is not amongstrong :")