import random
import threading
import turtle
f=open("E:\\tamrin2\mysterious.txt","r") #file location
file_1=f.read()
f.close()
def decrypt_clue(text):
    """find keyword python in text"""
    keyword_python=("and","as","assert","async","await","break","class","continue","def","del","elif","else","except","False","finally",
                "for","from","global","if","import","in","is","lambda","none","nonlocal","not","or","pass","raise",
                "return","True","try","while","with","yield")
    result=[]
    for word in keyword_python:
        if word in text:
            result.append(word)
    return result
first_mission=decrypt_clue(file_1)
print(first_mission)

f=open("E:\\tamrin2\puzzles.txt","r") #file location
file_2=f.read().splitlines()
f.close()
def solve_puzzels(text):
    """evaluation expressions and their results in boolean form"""
    result=[]
    for word in text:
        try:
            x=eval(word)
            y=bool(x)
            result.append(y)
        except : #for unknown data
            result.append(None)
    return result
second_mission=solve_puzzels(file_2)
print(second_mission)
while True: #to generate two random numbers as start and end
    num1=random.randint(0,1000)
    num2=random.randint(0,1000)
    if num2>num1:
        break
def calculate_magic_numbers(start,end):
    """create a list of magic numbers"""
    result=[]
    selected=[]
    for i in range(random.randint(start,end)): #the numbers of list elements is random
        number=random.randint(start,end)
        if number not in selected: #check that the random number is not repeated
            result.append(number)
            selected.append(number)
    return result
third_mission=calculate_magic_numbers(num1,num2)      
print(third_mission)      
count_correct=0
count_incorrect=0
timeout=20
flag=True
def exam_numbers():
    global count_correct,count_incorrect
    list_answer=[]
    while flag:
        random_number=random.randint(0,15)
        binary_number=bin(random_number)
        print(binary_number[2:])
        number=int(input("please enter desimal form number:"))
        list_answer.append(number)
        if number==int(binary_number,0):
            print("correct!!")
            count_correct+=1
        else:
            print("incorect!!")
            count_incorrect+=1
    return list_answer      
def finish_exam():
    global flag
    flag=False
    print("time is up")
    print("correct answer:",count_correct)
    print("incrrect answer",count_incorrect)
t=threading.Timer(timeout, finish_exam)
t.start()            
fourth_mission=exam_numbers()
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
def draw_la():
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
def draw_tar():
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(45)
    turtle.forward(100)
def dot():
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
def draw_ji():
    turtle.backward(45)
    turtle.left(90)
    turtle.forward(80)
    turtle.right(135)
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(30)
turtle.pensize(10)
turtle.speed(2)
turtle.shape("turtle")
draw_la()
turtle.penup()
turtle.goto(-50,-150)
turtle.pendown()
draw_tar()
turtle.penup()
turtle.goto(-60,-100)
turtle.pendown()
dot()
turtle.penup()
turtle.goto(-90,-100)
turtle.pendown()
dot()
turtle.penup()
turtle.goto(-250,-160)
turtle.pendown()
draw_ji()
turtle.penup()
turtle.goto(-210,-230)
turtle.pendown()
dot()
turtle.mainloop()
final_list=[first_mission[0],str(second_mission[0]),str(third_mission[0]),str(fourth_mission[0]),fifth_mission[0]] 
ramz="" 
def unlock_vault(clues):
    """putting together the first letter of each output"""
    global ramz
    for i in clues:
        j=i[0]
        ramz+=j
    return ramz 
print(unlock_vault(final_list))   