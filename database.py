from socketserver import ThreadingUnixStreamServer


class Patient:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.patient_id = ""
        self.age = ""
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_first_name,
                         patient_last_name,
                         patient_id,
                         patient_age):
    new_patient = Patient()
    new_patient.first_name = patient_first_name
    new_patient.last_name = patient_last_name
    new_patient.patient_id = patient_id
    new_patient.age = patient_age
    return new_patient


def print_database(db):
    for patient in db:
        print(patient)
        print("Name: {}, id: {}, age: {}".format(get_full_name(db[patient]),
                                                 db[patient]["ID"],
                                                 db[patient]["Age"]))


def get_full_name(patient):
    return patient.full_name()


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
    patient = db[id_number]
    return patient


def main():
    x = Patient()
    x.first_name = "Benjamin"
    x.last_name = "Simon"
    print(x.last_name)

    y = Patient()
    y.first_name = "Edawrd"
    y.last_name = "Smith"
    print(y.last_name)
    exit()
    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 11, 30)
    db[22] = create_patient_entry("Bob", "Boyles", 22, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    print_database(db)
    test_result_adder(db, 3, "HDL", 100)
    print_database(db)
    # print("Patient {} is a {}".format(get_full_name(db[2]),
    #                                   adult_or_minor(db[2])))


if __name__ == '__main__':
    main()
