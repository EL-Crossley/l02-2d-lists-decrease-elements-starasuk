# Put your function here

def decreaseElements(list):
    
    for i in range(0,len(list)):
        for j in range(0,len(list[i])):
            list[i][j] = list[i][j] - 1
    return list
    # credit to https://www.geeksforgeeks.org/how-to-replace-values-in-a-list-in-python/ for teaching me how to replace items in a list

# testing
nums = [[96, 5, 23, 16, 45, 63],[20,106,50,27,38,15]]
print(decreaseElements(nums))
