def merge(intervals):
    intervals=sorted(intervals)
    for i in range(len(intervals)-1):
        x=i
        if(i == len(intervals)-1 or i == len(intervals) ):
            break
        compared_value=intervals[x][1]
        while(compared_value>=intervals[x+1][0]):
            starting_value=min([intervals[v][0] for v in range(i,x+2)])
            ending_value=max([intervals[v][1] for v in range(i,x+2)])
            for j in range(i,x+2):
                intervals.pop(i)
            intervals.insert(i,[starting_value,ending_value])
            compared_value=intervals[i][1]
            if(len(intervals) == 1) or (i == len(intervals)-1):
                break    
    return intervals
intervals=  [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
