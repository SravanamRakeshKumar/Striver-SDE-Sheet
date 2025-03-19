a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(a)//2):
	for j in range(i,(len(a)-1)-i):
		a[i][j],a[(len(a)-1)-j][i]=a[(len(a)-1)-j][i],a[i][j]
		a[(len(a)-1)-j][i],a[(len(a)-1)-i][(len(a)-1)-j]=a[(len(a)-1)-i][(len(a)-1)-j],a[(len(a)-1)-j][i]
		a[(len(a)-1)-i][(len(a)-1)-j],a[j][(len(a)-1)-i]=a[j][(len(a)-1)-i],a[(len(a)-1)-i][(len(a)-1)-j]
print(a)