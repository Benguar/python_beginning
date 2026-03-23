# Dictionaries are data types used to store data in keys and values it is similar to objects i javascript
first_dictionary = {'Ben':{'Phy':80,'Eng':30,'Mth':20},'Sam':'17','Tolu':'20'}
#in the example above, the key Ben is mapped to string 18 key sam is mapped to key 17 key tolu is mapped to string 20 also it is important to know that keys are immutable. 
# A key in a dictionary is just a custom index e.g list[1] can be dictionary['Sam'] in a dictionary
# print(first_dictionary['Ben']['Phy'])



# for index in first_dictionary:
#     print(first_dictionary[index])

#When you run a loop for a dictionary what it returns is the keys not value


# s = 'BeGuA Vr vgT'
# s_lower = s
# print(s_lower)

# def find_grades(dictionary,value):
#     List = []
#     for index in dictionary:
#         if type(value) == str:
#             if index == value:
#                 List.append(dictionary[index])
#         elif type(value) == list:
#             if index in value:
#                 List.append(dictionary[index])

#     return List

# print(find_grades(first_dictionary,'Sam'))


#================
# Adding an element to a dictionary
# ================

# first_dictionary['Bolu'] = 'A' #Adding an element in a dictionary uses the same format of change an element in a list at a particular index

#================
# Changing an element in a dictionary
# ================

# first_dictionary['Bolu'] = 'C' #It goes to the element in key 'Bolu' and changes the value in it

# #================
# # Deleting an element in a dictionary
# # ================

# del(first_dictionary['Ben']) #Deletes Ben from the dictionary

# d1 = {1:3,7:4,1:9}
# d2 = {3:3,7:4,13:9}
# d3 = {4:3,5:4,7:9,3:3}

# # def check(ld,k):
# #     for index in ld:
# #         if k in index:
# #             return True
# #             break
# #     return False


# def check(ld,k):
#     L =[]
#     # for index in ld:
#     #     if k in index:
#     #         L.append(True)
#     #     else:
#     #         L.append(False)
#     # if False in L:
#     #     return False
#     # else:
#     #     return True

#     for index in ld:
#         if k not in index:
#             return False
#             break
#     retu rn True

# print(check([d1,d2,d3],7))


#To grab all the keys in a list we use dictionary.keys() e.g

# first_dictionary.keys()
# print(list(first_dictionary.keys()))  #putting each keys in a list


#To grab all the values in a list we use dictionary.keys() e.g

# first_dictionary.values()
# print(list(first_dictionary.values()))  #putting each keys in a list


#To grab all the keys and values in a list we use dictionary.keys() and returns them in a list+ tuples form e.g

# first_dictionary.items()
# print(list(first_dictionary.items()))  #putting each keys in a list


# def count_matches(d):
#     count = 0
#     for a,b in d.items():
#         if a == b:
#             count +=1
#     return(count)

# print(count_matches(d1))


#to copy an element d.copy is used e.g dcopy = d.copy() if you do dcopy = d you are making dcopy an alias of d
ben = 'Animal'

def count(song):
    List = song.split()
    dic = {}
    for index in List:
        index = index.lower()
        if index in dic:
            dic[index] += 1
        else:
            dic[index] = 1
    # print(dic)
    list_dic = list(dic.items())
    for items_list in range(len(list_dic)):
        for index in range(len(list_dic)):
            if index > items_list:
                if list_dic[items_list][1] < list_dic[index][1]:
                    ls = list_dic[items_list]
                    lb = list_dic[index]
                    list_dic[index] = ls
                    list_dic[items_list] = lb
                    # print(list_dic)
    # print(list_dic)
    return list_dic
    # print(arrange(list_dic))
        
def arrange(list):
    [('you', 4), ('my', 3), ('brain', 3), ('i', 2), ('fit', 1), ('lie', 1), ('dey', 1), ('love', 1), ('no', 1)]
    tracker = True
    new_list = []
    list_copy = list[:]
    v = 0
    for elements in list:
        # print(f'This is list_copy{list_copy}')
        temp_list = []
        whole_remove_list = [elements]
        for elements2 in list_copy:
            if elements[1] == elements2[1]:
                    temp_list.append(elements2[0])
                    whole_remove_list.append(elements2)
            
        for remove_elements in whole_remove_list:
            v +=1
            if remove_elements in list_copy:
                list_copy.remove(remove_elements)
                print(f'this is copy after remove {list_copy}')
        if temp_list != []:       
            new_list.append((temp_list,elements[1]))
    return new_list
   



song = "i love you i no fit fit lie you dey my brain you brain brAin you my my Love love love love"
ll =count(song)
print(ll)
print(arrange(ll))