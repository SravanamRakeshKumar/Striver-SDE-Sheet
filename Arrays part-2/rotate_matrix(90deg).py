matrix=[
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
q=len(matrix)
x=0
y=0
for i in range(len(matrix)-1):
	for j in range(i,q-1):
		x=i
		y=j
		start=matrix[x][y]
		for k in range(4):
			for l in range(i,q-1):
				if(j==0):
					if(k==0):
						y=y+1
					elif(k==1):
						x=x+1
					elif(k==2):
						y=y-1
					else:
						x=x-1
				else:
					if(k==0):
						if(y==q-1):
							x=x+1
						else:
							y=y+1
					elif(k==1):
						if(x == q-1):
							y=y-1
						else:
							x=x+1
					elif(k==2):
						if(y==i):
							x=x-1
						else:
							y=y-1
					else:
						if(x==i):
							y=y+1
						else:
							x=x-1
			start,matrix[x][y]=matrix[x][y],start
	q=q-1
print(matrix)