import random
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