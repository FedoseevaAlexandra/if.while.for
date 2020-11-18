n=int(input('introduceti nr '))
i=1
s1=0
s2=0
for i in range(1,n+1) :
	s1+=i**3
	s2+=i
	
print('s1=',s1     ,'s2=',s2**2)
s1=0
s2=n**3+n**2
for i in range(1,n+1) :
    s1+=i**2
    s2+=i
    
print('s1=',s1*3     ,'s2=',s2)
