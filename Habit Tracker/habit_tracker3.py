import os
from datetime import date, datetime

import requests

TOKEN = "YOUR TOKEN"
USERNAME =  "YOUR USERNAME"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"



graph_config = {
    "id": GRAPH_ID,
    "name": "workout Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you workout today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data,headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "12",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)