#taking input from user
string = input("Enter a your password: ");
print(string);
lower=upper=numeric=special_chars=False;

#checking all the given conditions
if len(string)>=8:
    for i in string:
        if i>='a' and i<='z':
            lower=True;
        elif i>='A' and i<='Z':
            upper=True;
        elif i.isnumeric():
            numeric=True;
        elif(i=='@' or i=='#' or i=='$'):
            special_chars=True;
else:
    print("length atleast 8 chars");

#if users password is satisfied with all the conditions or not.
if lower and upper and numeric and special_chars:
    print('That is a valid password.')
else:
    print('That password is not valid.')
