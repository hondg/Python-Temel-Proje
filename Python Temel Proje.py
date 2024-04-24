
def flatterList(my_list):
    flatten_list=[]
    for i in my_list:
        if type(i)==list:
            flatten_list.extend(flatterList(i))
        else:
            flatten_list.append(i)
    return flatten_list

def reverserList(my_list):
    reversing_index = len(my_list)-2
    while reversing_index >= 0:
        my_list.append(my_list[reversing_index])
        my_list.remove(my_list[reversing_index])
        reversing_index = reversing_index - 1
    return my_list


""" my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
print(flatterList(my_list))
print(reverserList(my_list)) """
    