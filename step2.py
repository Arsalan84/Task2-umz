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

