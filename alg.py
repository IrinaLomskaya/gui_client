import math



def eq(V, k):
    return ((V * V) * math.sin(2*k*(math.pi/180))/10000)


#print(eq(400, 52))



x = 18
y = 14
r = math.sqrt(x*x + y*y)
#print(r)

aV = []
aK = []
for V in range(100, 1000, 100):
    for k in range(1, 89):
        #print(k, V, eq(V, k), r)
            if abs(r - (eq(V, k) )) < 0.1:
                aV.insert(V, k)
                aK.insert(k, V)
print(aV)
print(aK)




