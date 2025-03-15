def generate(numRows): #take numnRows as a Parameter
        total_list=[] #container to stores the rows of Pascal's triangle.
        for i in range(numRows):
            inside_list=[] #row
            x=0
            for j in range(i+1):
                if (j==0) or (j == i):
                    inside_list.append(1) #assign "1" number in 0th and (n-1)th position in each row.
                else:
                    inside_list.append(last_element[x]+last_element[x+1]) # add privious list values and append present row 
                    x=x+1
            total_list.append(inside_list) # append rows into container
            last_element=total_list[-1] #store last row for adding the these row values in next row
        return total_list
print("give any +number for generating a Pascal's triangle=",end="")
rows=int(input()) #change input string  into a number
print(generate(rows)) #give rows as a Argument to the generate function