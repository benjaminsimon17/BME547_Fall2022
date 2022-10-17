import requests

# r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
# print(r)
# print(type(r))
# print(r.text)
# print(r.status_code)
# if r.status_code == 200:
#     answer = r.json()
#     print(type(answer))
#     for branch in answer:
#         print(branch["name"])
# else:
#     print("Bad request: {}".format(r.text))

# output_info = {"name": "Benjamin Simon",
#                "net_id": "bds54",
#                "e-mail": "bds54@duke.edu"}


# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                   json=output_info)

output_info = {"user": "bds54",
               "message": "hi dylan"}


r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=output_info)


r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/dc306")


print(r.text)
