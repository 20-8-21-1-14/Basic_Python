#fibonacci 
a, b = 0, 1
n = eval(input('Input length of fibo:'))
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b 

#2D shapes
#square
side = eval(input('Input side:'))
for i in range(side):
    for j in range(side):
        if (i == 0 or i == side-1 or j == 0 or j == side-1):
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()    
print('\n')
#Rectangle
print("Rectangle shape!")
length = eval(input('Input length size: '))
width = eval(input('Input width size: '))
for j in range(width):
    for i in range(length):
        if i==0 or i == length-1 or j == 0 or j==(width- 1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print('\n')

#triangle upside down
for i in range(7,1,-1):
    print('*'*(i-1))                

#diamond shapes
rows = 4
colums = rows*2-1
for i in range(rows):
    for j in range(colums):
        if((colums//2)-i <= j <= (colums//2)+i):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(rows):
    for j in range(colums):
        if(i < j < (colums-1-i)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()            