def merge_the_tools(string, k):
    n=len(string)//k 
    print(n)
    l=0   
    for i in k :
        str=""
        for j in range(n):
            str+=string[l]
            l+=1
        print(str)

string=input()
k = int(input("Enter k "))
merge_the_tools(string, k)