import Student
import matplotlib.pyplot as plt
import json

def main():
    # Final Project Question 3 Client
    # Author: Jay Yang
    # Date: 12/14/2023
    # A program navigates a menu with ability to add Student objects to list
    # Program allows various methods comparing instances and displaying grade data 

    student_list = []
    print("Welcome to the Client program!")
    menu(student_list)

def menu(student_list):
    #hands menu selection and navigates to other methods, other methods call to this function and loop with carried list
    print ("___________________________________________________________________________________ ")
    print("Please pick a number")
    print("1. Quit (exit the program) \n"+ \
          "2. Add student to list \n" + \
          "3. Output the details of all students in list \n" + \
          "4. Compute and output the average overall mark for students \n" + \
          "5. Display how many students obtained an mark equal to average mark \n" + \
          "6. Display the distribution of grades (matplotlib) \n" + \
          "7. Given a student number (ID), view all details of the student \n" + \
          "8. Given a student’s name (first and last – ignoring case), view details of student \n" + \
          "9. Sort the list of students into ascending order of students’ numbers output list")
    choice = eval(input("Menu choice (1-9):  "))

    if choice == 1:
        return
    elif choice == 2:
        add(student_list)
    elif choice == 3:
        output_list(student_list)
    elif choice == 4:
        average(student_list)
    elif choice == 5:
        average_display(student_list)
    elif choice == 6:
        distribution(student_list)
    elif choice == 7:
        id_search(student_list)
    elif choice == 8:
        name_search(student_list)
    elif choice == 9:
        sort_id(student_list)
    else:
        print("Please select a number in the menu (1-9)")
        menu(student_list)

def add(student_list):
    #Add new instance of Student to list and loop to menu
    new = Student.Student("","",0,"",0,0,0,0)
    new.set_first(input("What is the student's first name? "))
    new.set_last(input("What is the student's last name? "))
    new.set_dob(input("What is the student's date of birth (DD/MM/YYYY)? "))
    new.set_id(input("What is the student's ID number? "))
    new.set_a1(input("What is the student's score for Assignment 1? "))
    new.set_a2(input("What is the student's score for Assignment 2? "))
    new.set_lab(input("What is the student's score for Weekly Labs? "))
    new.set_final(input("What is the student's score for Final Exam? "))
    student_list.append(new)
    menu(student_list)

def output_list(student_list):
    #print all Student data in list and loop to menu
    for x in student_list:
        print(x)
    menu(student_list)

def average(student_list):
    #prints average mark of list and loops to menu
    cache = 0
    count = 0
    for x in student_list:
        x.compute_mark()            #call to assign final mark
        x.compute_grade()           #call to assign final grade
        mark = x.get_mark()
        cache += mark
        count += 1
    print(f"The average final mark of the student list is: {cache/count}")
    menu(student_list)
    
def average_display(student_list):
    #prints student count in relation to average mark and loops to menu
    equal_above = 0
    below = 0
    cache = 0
    count = 0
    for x in student_list:
        x.compute_mark()             #call to assign final mark
        x.compute_grade()            #call to assign final grade
        mark = x.get_mark()
        cache += mark
        count += 1
    avg =  cache/count    

    for x in student_list:
        x.compute_mark()            #call to assign final mark
        x.compute_grade()           #call to assign final grade
        mark = x.get_mark()
        if mark < avg:
            below += 1
        else:
            equal_above += 1
    print(f"{equal_above} students were equal to or above the average score of {avg}, while {below} were below.")
    menu(student_list)

def distribution(student_list):
    #uses matplotlib to show graph of final mark distribution in list
    length = len(student_list)
    score_list = []
    for x in student_list:
        x.compute_mark()             #call to assign final mark
        x.compute_grade()            #call to assign final grade
        mark = x.get_mark()

        score_list.append(mark)

    plt.plot(range(length), score_list, 'g^')
    plt.ylabel('Final Marks')
    plt.xlabel('Students')
    plt.axis([-1, length, 0, 100])
    plt.show()
    
    menu(student_list)


def id_search(student_list):
    #input id number to find correlating student information
    search_id = int(input("Which ID number would like to search? "))
    for x in student_list:
        if x.get_id() == search_id:
            print(x)
            menu(student_list)
        else:
            print(f"ERROR:no student with ID#{search_id} exists.")
            menu(student_list)

def name_search(student_list):
    #input name to find correlating student information

    search_first = input("What is the first name you would like to search? ")
    search_last = input("And last name? ")
    search_first.upper()
    search_last.upper()
    for x in student_list:
        if x.get_first().upper() == search_first:
            if x.get_last().upper() == search_last:
                print(x)
                menu(student_list)
            else:
                print(f"ERROR:no student with name {search_first} {search_last} exists.")
                menu(student_list)
        else:
                print(f"ERROR:no student with name {search_first} {search_last} exists.")
                menu(student_list)

def sort_id(student_list):
    #prints sorted list in descending order of ID number values
    new_list = []                   #new list to insert id values
    for x in student_list:
        new_list.append(x.get_id())
    new_list.sort()                 #sort ids in order

    sorted_list = []                #another new list to insert whole objects
    for x in new_list:
        for y in student_list:
            if x == y.get_id():   
                sorted_list.append(y)  #insert objects 
    for r in sorted_list:
        print(str(r))                 #print str method of each student in sorted order
    menu(student_list)
    


if __name__ == '__main__':
    main()
