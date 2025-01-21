import Patient, Procedure

def main():
    #construct one instance of class Patient and three instances of class Procedure
    patient1 = Patient.Patient('Jay', 'W', 'Yang', '111 1st Ave', 'Seattle', 'WA', '98119', '111-111-1111', 'Sally', '222-222-2222')
    procedure1 = Procedure.Procedure('Physical Exam', '11/9/2022', 'Dr.Irvine', 250.00)
    procedure2 = Procedure.Procedure('X-Ray', '11/9/2022', 'Dr.Jamison', 500.00)
    procedure3 = Procedure.Procedure('Blood Test', '11/9/2022', 'Dr.Smith', 200.00)

    total = procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()
    
    print(patient1)
    print(procedure1)
    print(procedure2)
    print(procedure3)
    print("TOTAL CHARGES:", total)

if __name__ == '__main__':
    main()
