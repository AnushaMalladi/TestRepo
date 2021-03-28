from pip._vendor.html5lib import _inputstream

###Prob1
# dict2={}
# count= int(input("Please input the size of a dict")) 
# 
# for i in range(0,count):
#     key=input ("please enter key of a dict")
#     dict2[key] =[float(input("enter values of alist")) for i in range(3)]
#     
# print(dict2)
# avgred= input("please enter students name")
# suma =0
# new_dict ={}
# for key,value in dict2.items():
#     if avgred in dict2.keys():
#         for i in value:
#             suma=suma+i
#         count = len(value)
#         avg= suma/count       
#          
#     #new_dict=new_dict.append({key:avg})
#     new_dict[key] = round(avg,2)
     
#print("the average of is" + str(new_dict[avgred]))
 
# prob2
# lis=[]
# n = int(input())
# lis = [int(input())for i in range(n)]
# print(lis)
# max_num= max(lis)
# min_num=min(lis)
# print("max_num"+str(max_num)+"Min_num"+str(min_num))
# for i in lis:
#     if (i > min_num and i != max_num):
#         min_num=i
# print("the runner up score"+str(min_num))

#prob3
# n=int(input("the size of actual list"))
# m=int(input("the size of marks list"))
# listofvalues=[[input("name of student"),int(input("marks attained"))] for i in range(n) for j in range(m)]
# print(listofvalues)
# #listofvalues=[['alpha', 20], ['beta', 30]]
# marks_dict = {i[0]:i[1] for i in listofvalues }
# # for i in listofvalues:
# #     print("listof values"+str(i))
# #     key=i[0]
# #     value=i[1]
# #     print("key,value"+str(key)+" "+str(value))
# print(marks_dict)
# max_value=max(marks_dict.values())
# top_scorer_name = [key for key,value in marks_dict.items()  if max_value==value]
# #print("top_scorer_names are   \n"+str(''.join(top_scorer_name)))
# for i in top_scorer_name:
#     print(i)

#prob4
# list =[1,2,3,4,5,2,3,4]
# value= int(input("Please enter a number "))
# index_position= int(input("please enter index position"))
# list.insert(index_position,value)
# print("The new list is "+str(list))
# list.remove(2)
# print("The final list after removing the value is "+ str(list))
# list.append(2)
# print("The final list after appending the value is "+ str(list))
# list.sort()
# print("The list after sorting "+str(list))
# list.pop()
# print("The list after popping"+str(list))
# list.reverse()
# print("The list after reversing is "+str(list))


#Prob 5

# def swap_case(s):
#     list1=[]
#     for i in s :
#         if i.isupper():
#             i=i.lower()
#         else:
#             i=i.upper()
#         list1.append(i)
#     
#     return ''.join(list1)
# 
# if __name__ == '__main__':
#     
#     requiredstring=input("Please enter the string to be swapcased : ")
#     print("The final statement after swap case is " +str(swap_case(requiredstring)))


#Prob 6

# def split_and_join(line):
#     
#     final_input_list=Input_String.split()
#     final_input_string='-'.join(final_input_list)
#     return final_input_list,final_input_string
# 
# if __name__ == '__main__':
#     Input_String =input("Please enter the input string : -")
#     final_input_list,final_input_string =split_and_join(Input_String)
#     
#     print(final_input_string)
    


#Prob 7

# def print_full_name(a, b):
#     print("Hello "+str(a)+" "+str(b)+"! You just delved into python.")
# 
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


#Prob8

# def mutate_string(string, position, character):
#     string_1 = string[:position] + c + string[position+1:]
#     return string_1
# 
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

#Prob 9
# def main():
#     string = input()
#     substr = input()
#     strlen = len(string)
#     substrlen = len(substr)
#     occ = 0
#     for i in range(strlen-substrlen+1):
#         if string[i:i+substrlen] == substr:
#             occ += 1
#     print(occ)
# 
# main()


#Prob10

# if __name__ == '__main__':
#     s = input()
#     print(s.isalnum())
#     print(s.isalpha())
#     print(s.isdigit())
#     print(s.islower())
#     print(s.isupper())

#Prob11

# import textwrap
# def wrap(string, max_width):
#     lst=textwrap.wrap(string, max_width)
#     return '\n'.join(lst)
# 
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


#Prob 12
#!/bin/python3

# import itertools
# 
# a = [int(x) for x in input().split()]
# b = [int(x) for x in input().split()]
# 
# print(' '.join(str(t) for t in itertools.product(a,b)))

#Prob 13
# from collections import Counter
# list_1= [int(x) for x in input().split()]
# count=0
# for  key ,value in Counter(list_1):
#         count=count+value
# 
# print(value)

#Prob14
# def average(array):
#     sum_1 = sum(set(array))
#     lentgth=len(set(array))
#     avg=sum_1/lentgth
#     return avg
# 
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

# #Prob 15
# M=int(input())
# M_items=list(map(int, input().split()))
# N=int(input())
# N__items= list(map(int, input().split()))
# 
# final_set=set(M_items).symmetric_difference(N__items)
# final_set_1=sorted(final_set)
# 
# for  i in final_set_1:
#     print(i)


#Prob16
# M=int(input())
# M_items=[input() for i in range(0,M)]
# list_count = len(M_items)
# set_list1=len(set(list(M_items)))
# print(set_list1)


#Prob 17
a= int(input())
b=int(input())
c= input()
try:
    k=a/b
   
except ZeroDivisionError as e:
    print(e)



















