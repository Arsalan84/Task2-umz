final_list=[first_mission[0],str(second_mission[0]),str(third_mission[0]),str(fourth_mission[0]),fifth_mission[0]] #the output are obtained from the previous steps
ramz="" 
def unlock_vault(clues):
    """putting together the first letter of each output"""
    global ramz
    for i in clues:
        j=i[0]
        ramz+=j
    return ramz 

print(unlock_vault(final_list))   