def setZeroes(matrix): #take matrix as a parameter
        i_values,j_values=set(),set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    i_values.add(i) #find i value for set Zero value in rows.
                    j_values.add(j) #find j value for set Zero  value in colums.
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i in i_values) or (j in j_values):
                    matrix[i][j]=0  #set Zero, if i or j position is in i_values,j_values sets.
        return matrix
answer=setZeroes([[1,1,1],[1,0,1],[1,1,1]]) # give a matrix as a Argument to setZeroes function.
print(answer)