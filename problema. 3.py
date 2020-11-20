n=int(input('dati primul nr '))
m=int(input('dati al doilea nr '))
if (m>n) and (n>1):
	while m/n>1:
		m=m/n
	if m/n==1:
		print('da')
	else :
		print('nu')
else:
	print('nu')