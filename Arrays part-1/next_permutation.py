numbers_list=[1,4,3,2] #user list as a input
wrong_index=0 #initial no wrong_index 
for i in range(-1,-len(numbers_list),-1):
    if(numbers_list[i]<=numbers_list[i-1]):
        if(i == -(len(numbers_list)-1)): #if the number is big then simply return the sorted list
            print(sorted(numbers_list)) 
        continue
    else:
        if(i == -1):
            numbers_list[i],numbers_list[i-1]=numbers_list[i-1],numbers_list[i] #if last number is big than the privious number? then simply swap the both 2 numbers and return list
            print(numbers_list)
            break
        else:
            wrong_index=i-1 #otherwise decrease the index in decending order 
            break
if(wrong_index!=0):
    nearest_greater_number=1 
    new_list=[] #take one new list for storing the sorted subarry 
    for i in range(wrong_index,0,1):
        new_list.append(numbers_list[i])
    while(1<2): #find the nearest number to the wrong_index number 
            if(numbers_list[wrong_index]+nearest_greater_number in new_list):
                 nearest_greater_number=numbers_list[wrong_index]+nearest_greater_number
                 break
            nearest_greater_number+=1 
    new_list.remove(nearest_greater_number) #remove the nearest value 
    new_list=[nearest_greater_number]+sorted(new_list) #new list with nearest value + sorted atrray
    k=0
    for i in range(len(numbers_list)-len(new_list),len(numbers_list)):
             numbers_list[i]=new_list[k] #insert the sorted list values into default array
             k+=1
    print(numbers_list)
            