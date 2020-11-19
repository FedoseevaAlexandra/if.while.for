a=float(input('dati nr a '))
b=float(input('dati nr b '))
c=float(input('dati nr c '))
if (a>0) and(b>0) and(c>0)and(a<b+c) and(b<a+c)and(c<b+a): 
    if (a==b) and (b==c):
        print('triunghi echilateral')
    elif (a**2==b**2+c**2)or(b**2==a**2+c**2)or(c**2==a**2+b**2):
        print('triunghi dreptunghic')
    else: 
        print('triunghi scalen')
else:
    print("nu pot fi laturile unui triunghi")   
