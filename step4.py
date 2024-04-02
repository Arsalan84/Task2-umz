import random
import threading
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