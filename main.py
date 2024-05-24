import requests
from datetime import datetime

USERNAME = "USERNAME"
TOKEN = "SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"
date = "20240320"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN.encode("utf-8")
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
today = datetime(year=2024, month=3, day=20)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilo did you cycle today? ")
}

new_pixel = {
    "quantity": "100",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ichou",
}

response = requests.put(url=update_endpoint,json=new_pixel, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)