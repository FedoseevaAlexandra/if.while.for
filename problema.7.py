n=int(input('introduceti nr de ani impliniti '))
b=1
if (n>1) and (n<20):
    for b in range(2,n+1):
        b+=b*2+b
print('Cand a implinit',n,'ani','a primit',b-1,'dolari')
