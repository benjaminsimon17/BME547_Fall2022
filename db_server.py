from curses import KEY_SLEFT
from flask import Flask, request, jsonify

db = []
app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_on():
    return "DB server is on"


def add_patient(patient_name, patient_id, blood_type):
    new_patient = {"name": patient_name,
                   "id": patient_id,
                   "blood_type": blood_type,
                   "test_name": [],
                   "test_result": []}
    db.append(new_patient)


def init_server():
    add_patient("Ann Ables", 1, "A+")
    add_patient("Bob Boyles", 2, "B+")


@app.route("/new_patient", methods=["POST"])
def add_new_patient_to_server():
    """
    recieve data from POST request
    call other functions to do all the work
    return information
    """
    in_data = request.get_json()
    message, status_code = add_new_patien_worker(in_data)
    return message, status_code


def add_new_patien_worker(in_data):
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400
    add_patient(in_data["name"],
                in_data["id"],
                in_data["blood_type"])
    return "Patient succesfully added", 200


@app.route("/new_patient", method=["POST"])
def new_patient():
    in_data = request.get_json()
    add_new_patien_worker(in_data)
    return "Patient succesfully added", 200


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results(patient_id):
    for i in db:
        if i["id"] == patient_id:
            return i["test_result"]
        else:
            return "Patient not found"


@app.route("/add_test", method=["POST"])
def add_test_flask_handler():
    in_data = request.get_json()
    msg, status_code = add_test_worker(in_data)
    return msg, status_code


def add_test_worker(in_data):
    msg = add_test_validation(in_data)
    if msg is not True:
        return msg, 400
    add_test_to_patient(in_data)
    return "Test added", 200


def add_test_to_patient(in_data):
    patient = find_patient(in_data["id"])
    patient["test_name"].append(in_data["test_name"])
    patient["test_result"].append(in_data["test_result"])


def add_test_validation(in_data):
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    for ex_key, ex_type in zip(expected_keys, expected_types):
        if ex_key not in in_data:
            return "Key missing"
        if type(in_data[ex_key]) is not ex_type:
            return "Bad Value Type"
    return True


def find_patient(patient_id):
    for patient in db:
        if patient["id"] == patient_id:
            return patient
    return False


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    for key in expected_keys:
        if key not in in_data:
            return "Key {} is missing from POST data".format(key)
    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key] is not ex_type):
            return "Key {} has the wrong data type".format(key)
    return True


if __name__ == '__main__':
    init_server()
    app.run()
