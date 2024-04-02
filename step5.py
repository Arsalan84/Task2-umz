user_list=[]
punctuation=["!","@","#","$","%","&","*","~",";",",","?","+","/"] 
check_list=[]
flag=True
#loop to write list of username and password
while flag:
    user=input('please enter username:')
    password=input("please enter password:")
    p=(user,password)
    user_list.append(p)
    result=input("do you want continue:(n/y)")
    if result=="n":
        break
def check_pass():
    """checking passwords that have special conditons"""
    for username , password_check in user_list:
        if len(password_check)<8 :
            continue
        elif not password_check.islower() and not password_check.isupper():
            for i in password_check:
                if i in punctuation:
                    check_list.append(username)
                    break
    return check_list            
fifth_mission=check_pass()  
print(fifth_mission)            