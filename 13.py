def resizeBits(a, b):
	while(len(a) != len(b)):
		b = a[0] + b
	return b

def setQ(a, b):
	while(len(a) != len(b)):
		b = '0' + b
	return b

def setNegQ(a, b):
	while(len(a) != len(b)):
		b = '1' + b
	return b

c = int(input("Enter multiplicant: "))
if (c == 0):
    M = 0
elif (c == -1 or c == -3 or c == -7 or c == -15):
    M = bin(~(c-3)).lstrip('0b')
elif (c == -2 or c == -6 or c == -14):
    M = bin(~(c-5)).lstrip('0b')
elif (c == -5 or c == -13):
    M = bin(~(c-7)).lstrip('0b')
elif (c == -4 or c == -12):
    M = bin(~(c-9)).lstrip('0b')
elif (c == -11):
    M = bin(~(c-11)).lstrip('0b')
elif (c == -10):
    M = bin(~(c-13)).lstrip('0b')
elif (c == -9):
    M = bin(~(c-15)).lstrip('0b')
elif (c == -8):
    M = bin(~(c-17)).lstrip('0b')
elif (c == 1 or c == 2 or c == 4 or c == 8):
    M = bin(c).lstrip('0b')
elif (c == 3 or 4 < c < 16):
    d = bin(c).lstrip('0b')
    M = '0' + d
l = len(M)
q = int(input("Enter q "))
if(q > 0):
    B = bin(q).lstrip('0b')
    l1 = len(B)
    Q = setQ(M, B)
    # if (l == l1):
    #     print(B)
    # else:
    #     d1 = l - l1
    #     if(d1 == 1):
    #         Q = '0' + B
    #     elif(d1 == 2):
    #         Q = '00' + B
    #     elif(d1 == 3):
    #         Q = '000' + B
    #     elif(d1 == 4):
    #         Q = '0000' + B
else:
    if (q == -1 or q == -3 or q == -7 or q == -15):
        B = bin(~(q-3)).lstrip('0b')
    elif (q == -2 or q == -6 or q == -14):
        B = bin(~(q-5)).lstrip('0b')
    elif (q == -5 or q == -13):
        B = bin(~(q-7)).lstrip('0b')
    elif (q == -4 or q == -12):
        B = bin(~(q-9)).lstrip('0b')
    elif (q == -11):
        B = bin(~(q-11)).lstrip('0b')
    elif (q == -10):
        B = bin(~(q-13)).lstrip('0b')
    elif (q == -9):
        B = bin(~(q-15)).lstrip('0b')
    elif (q == -8):
        B = bin(~(q-17)).lstrip('0b')
    l2 = len(B)
    Q = setNegQ(M, B)
    # if (l == l2):
    #     print(B)
    # else:
    #     d2 = l - l2
    #     if(d2 == 1):
    #         Q = '1' + B
    #     elif(d2 == 2):
    #         Q = '11' + B
    #     elif(d2 == 3):
    #         Q = '111' + B
    #     elif(d2 == 4):
    #         Q = '1111' + B
e = -c
if (e == -1 or e == -3 or e == -7 or e == -15):
    M1 = bin(~(e-3)).lstrip('0b')
elif (e == -2 or e == -6 or e == -14):
    M1 = bin(~(e-5)).lstrip('0b')
elif (e == -5 or e == -13):
    M1 = bin(~(e-7)).lstrip('0b')
elif (e == -4 or e == -12):
    M1 = bin(~(e-9)).lstrip('0b')
elif (e == -11):
    M1 = bin(~(e-11)).lstrip('0b')
elif (e == -10):
    M1 = bin(~(e-13)).lstrip('0b')
elif (e == -9):
    M1 = bin(~(e-15)).lstrip('0b')
elif (e == -8):
    M1 = bin(~(e-17)).lstrip('0b')
elif (e == 1 or e == 2 or e == 4 or e == 8):
    M1 = bin(e).lstrip('0b')
elif (e == 3 or 4 < e < 16):
    d = bin(e).lstrip('0b')
    M1 = '0' + d
print("M: ", M)
print("Q: ", Q)
print("M1:",M1)
l3 = len(Q)
a = bin(0).lstrip('0b')
l4 = len(a)
d3 = l3 - l4
if(d3 == 1):
	A = '0' + a
elif(d3 == 2):
	A = '00' + a
elif(d3 == 3):
	A = '000' + a
elif(d3 == 4):
	A = '0000' + a
elif(d3 == 5):
	A = '00000' + a
print("A: ", A)
count = l3
Q1 = '0'
while (count!=0):
    w = '00'
    x = '01'
    y = '10'
    z = '11'
    v = Q[-1]
    
    n = v + Q1
    if (n == w or n == z):
        u = A + Q + Q1
        t = int(u,2)
        t = t >> 1 
        s = bin(t).lstrip('0b')
        r = s
        r = resizeBits(u, r)
        #print("Condition 1 R: ", r)
        
    if (n == x):
        #print("Condition is true")
        sum = bin(int(A, 2) + int(M, 2)).lstrip('0b')
        l4 = len(A)
        l5 = len(sum)
        #print("l4 and l5 are ", l4, " ", l5)
        if l4 == l5:
        	e = sum
        else:
        	e = sum[1:]
        u = e + Q + Q1
        t = int(u, 2)
        #print("t : ", t)
        t = t >> 1
        s = bin(t).lstrip('0b')
        r =  s
        r = resizeBits(u, r)
        #print("U: ", u , " t: ", t, " s: ", s, " r: ", r)


    if (n == y):
        sum = bin(int(A,2) + int(M1,2)).lstrip('0b')
        print(sum, " ", M1)
        if count == len(M):
        	sum = setQ(M1, sum)
        #print(sum)
        l4 = len(A)
        l5 = len(sum)
        print(l4,l5)
        if(l4 == l5):
            e = sum
        else:
            e = sum[1:]
        u = e + Q + Q1
        print(u)
        t = int(u,2)
        t = t >> 1
        s = bin(t).lstrip('0b')
        r = s
        r = resizeBits(u, r)
    # else:
    # 	print("All condtions were false")
    print("R is ", r)
    print("A is",r[0:(len(r)-1)//2])
    print("Q is",r[(len(r)-1)//2:len(r)-1])
    print("Q1 is",r[-1])
    A = r[0:(len(r)-1)//2]
    Q = r[(len(r)-1)//2:len(r) - 1]
    Q1 = r[-1]
    count = count - 1

ans = A + Q
# ans2 = ""
# if A[0] == '1':
# 	for i in range(len(ans)):
# 		if ans[i]==1:
# 			ans2[i] = 0
# 		else:
# 			ans2[i] = 1

print("Product is : ", ans)



    
    
