from socketserver import ThreadingUnixStreamServer


def create_patient_entry(patient_Name, patient_id, patient_age):
    new_patient = [patient_Name, patient_id, patient_age, []]
    return new_patient

def print_database(db):
    for patient in db:
        print(db)
        print("Name: {}, id: {}, age: {}".format(patient[0], patient[1],patient[2]))
        
def test_result_adder(db, id_number, test_name, test_value):
    patient = find_patient(db, id_number)
    if patient !=False:
        test_tuple = (test_name,test_value)
        patient[3].append(test_tuple) 
            
def find_patient(db, id_number):
    for patient in db:
        if patient[1] == id_number:
            return patient
    return False

def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1,30))
    db.append(create_patient_entry("Bob Boyles",2,34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    test_result_adder(db,3,"HDL",100)
    print(find_patient(db,3))
    
    
if __name__ == '__main__':
    main()
