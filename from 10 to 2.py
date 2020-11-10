d = {
    
}


a = 46458
l = []
while a > 0:
    i = a % n
    a = a // n
    l.append(i)
l.reverse()
l = [str(i) for i in l]
l = ''.join(l)
print(l)