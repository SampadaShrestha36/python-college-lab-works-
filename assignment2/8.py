'''
1
2 3
4 5 6
7 8 9 10
'''
k=1
for i in range(0,4):
    for j in range(0,i+1):
        print(k,end=" ")
        k+=1
    print()