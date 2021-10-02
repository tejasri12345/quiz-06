#taking input from user
string = input("Enter sentence: ");
str=string.split();
#print(str);

#checking words in dictionary.If it is already exits in dictionary its value is incremented by one otherwise it will set to one.
empty_dict={};
for i in str:
    if i in empty_dict:
        empty_dict[i] +=1;
    else:
        empty_dict[i] = 1;

#sorting keys and values in descending order
des_values = sorted(empty_dict.values(),reverse=True)
des_keys = sorted(empty_dict.keys(),reverse=True)
print(des_values)
print(des_keys)

#merging 2 lists as dictionary
dic={}
for i in range(0,len(des_values)):
    dic[des_keys[i]]=des_values[i]
print(dic);

