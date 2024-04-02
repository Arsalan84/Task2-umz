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