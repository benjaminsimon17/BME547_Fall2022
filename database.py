from socketserver import ThreadingUnixStreamServer


def create_patient_entry(patient_first_name,
                         patient_last_name,
                         patient_id,
                         patient_age):
    new_patient = {"First Name": patient_first_name,
                   "Last Name": patient_last_name,
                   "ID": patient_id,
                   "Age": patient_age,
                   "Tests": []}
    return new_patient


def print_database(db):
    for patient in db:
        print(patient)
        print("Name: {}, id: {}, age: {}".
              format(get_full_name(patient), patient["ID"], patient["Age"]))


def get_full_name(patient):
    return patient["First Name"] + " " + patient["Last Name"]


def test_result_adder(db, id_number, test_name, test_value):
    patient = find_patient(db, id_number)
    if patient:
        test_tuple = (test_name, test_value)
        patient["Tests"].append(test_tuple)


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


def find_patient(db, id_number):
    for patient in db:
        if patient["ID"] == id_number:
            return patient
    return False


def main():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 30))
    db.append(create_patient_entry("Bob", "Boyles", 2, 34))
    db.append(create_patient_entry("Chris", "Chou", 3, 25))
    print_database(db)
    test_result_adder(db, 3, "HDL", 100)
    print_database(db)
    print("Patient {} is a {}".format(get_full_name(db[2]),
                                      adult_or_minor(db[2])))


if __name__ == '__main__':
    main()
