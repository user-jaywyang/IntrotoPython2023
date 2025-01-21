def main():
    #takes 3 different dictionarys with courses as keys and returns each of 3 values associated with key

    room_dict = {'CS101':'3004' ,'CS102':'4501' ,'CS103':'6755' ,'NT110':'1244' ,'CM241':'1411'}
    instructor_dict = {'CS101':'Haynes' ,'CS102':'Alvarado' ,'CS103':'Rich' ,'NT110':'Burke' ,'CM241':'Lee'}
    time_dict = {'CS101':'8:00 am','CS102':'9:00 am' ,'CS103':'10:00 am' ,'NT110':'11:00 am' ,'CM241':'1:00 pm'}

    choice = input("What class do you want to search? \n")
    if choice in room_dict:                 
        print(f"Class {choice} is in room {room_dict[choice]} with instructor {instructor_dict[choice]} at {time_dict[choice]}.")

if __name__ == '__main__':
    main()
