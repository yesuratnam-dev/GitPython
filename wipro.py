'''def squares(a,b):

    for i in range(a,b+1):
        j=1
        while j*j<=i:
            if j*j==i:
                 print(i)
            j=j+1
        i=i+1


print(squares(1,300)) '''

'''n=int(input('number: '))
for i in range(1,n+1):
    v=i**2
    print(i,'power 2 = ',v)'''

# leap year
'''n=int(input(' enter the year : '))
if (n%4==0 and n%100!=0) or n%400==0:
    print('leap')
else:
    print('not a leap year')'''


## prime numbers irritated code in wiproNQT2019

m = int(input(' enter lower number: '))
n = int(input(' enter higher number : '))
m = -m
a = []
b = []
for i in range(0, n, 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
    a.append(i)


for i in range(0, m, 1):
    for j in range(2, i):
        if(i%j==0):
            break
    else:
        print(i)
        b.append(-i)
print(a)
print(b)
final=min(b)+max(a)
print('final  sum : ', final)
c = []
for i in range(1,final+1,1):
    j=final%i
    if j > 1:
        j = j % 2
    c.append(j)
print('final bits encoded by RATNAM is: ', c)
d = []
while final+1 > 1:
    k = final % 2
    final = final//2
    d.append(k)

print('final encoded data is : ', d)


# NOW I HAVE TO REVERSE THE LIST TO GET EXACT LIST I WANTED

'''y = []
v = 0
for i in d:
    if i == 0:
        v = 1
    elif i == 1:
        v = 0
    y.append(v)
print(y)'''
