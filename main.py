import requests
from datetime import datetime
USER_NAME = "clemo"
GRAPH_ID = "graph123"
TOKEN = "bfabshjbdsjbzjvzjbvfjvbhfbz"
pixela_end_point = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_end_point, json=user_params)
#print(response.text)

graph_end_point = f"{pixela_end_point}/{USER_NAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Progress graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_end_point, json=graph_config,headers=headers)
# print(response.text)
today = datetime.now()
#today = datetime(year=2022,month=6,day=15)
print(today)

pixela_creation_endpoint = f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many killometers did you cycle today?: "),
}

response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5",
}

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_end_point}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response=requests.delete(url=delete_endpoint,headers=headers)
#print(response.text)
