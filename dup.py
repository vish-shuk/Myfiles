new_list = []

def unique_list(listt):
    list_uni = list(set(listt))
    return list_uni
    
list_1 = raw_input("Enter List-1 (use spaces to separate each element) :")
list_2 = raw_input("Enter a List-2 (use spaces to separate each element) :")

list_1 = list_1.split()
list_1 = [int(a) for a in list_1]
list_1.sort()

list_2 = list_2.split()
list_2 = [int(a) for a in list_2]
list_2.sort()

print " List-1: ", list_1
print " List-2: ", list_2

list1 = unique_list(list_1)
list2 = unique_list(list_2)

def common_ele(list1, list2):
    for a in list1:
        if a in list2:
            new_list.append(a)
    return new_list

common_ele(list1, list2)     
print " The list of elements common to List-1 and List-2 is: ", new_list
            
            


