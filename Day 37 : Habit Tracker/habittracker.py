import requests
from datetime import datetime as dt

TOKEN = "ThisIsATestProgram"
USERNAME = "jayesh22"
GRAPH_ID = "graph1"

pixela_user_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "NotMinor": "yes"
}

# response = requests.post(url=pixela_user_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_user_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id": GRAPH_ID,
    "name": "Jogging Graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)

today = dt.now()

pixels_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you jog today?"),
}

# response = requests.post(url=pixels_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixels_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixels_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.put(url=delete_endpoint, headers=headers)
# print(response.text)
