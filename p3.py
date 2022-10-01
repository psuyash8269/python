for i in range(int(input())):
  arr=[]
  for i in range(1,int(input("Enter the lenght of list : "))+1):
    arr.append(int(input("Enter element of array : ")))
  print(arr)
  for i in (arr):
    a=arr.count(i)
    if a==1:
        print(i)