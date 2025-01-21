import Q2class

def main():
    #construct three instances of class Employee
    subject1 = Q2class.Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    subject2 = Q2class.Employee('Mark Jones', 39119, 'IT', 'Programmer')
    subject3 = Q2class.Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    print(subject1)
    print(subject2)
    print(subject3)


if __name__ == '__main__':
    main()
