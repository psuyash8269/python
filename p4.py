N = int(input("Enter N: "))
S = int(input("Enter S: "))
L = []
for x in range(N):
    L.append(int(input()))


for i in range(0, N):
    for j in range(0, N//2):
        if (L[i] + L[j]) == S:
            if (L[i]<L[j]):
                print(L[i], L[j])
            else:
                print(L[j],L[i])
            