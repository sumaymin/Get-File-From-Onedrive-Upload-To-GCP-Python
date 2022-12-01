import requests
import json
import pandas as pd

# Set Authorization and connect to OneDrive
token = {your_access_token}
URL = 'https://graph.microsoft.com/v1.0/'
HEADERS = {'Authorization': 'Bearer ' + token}
response = requests.get(URL + 'me/drive/', headers = HEADERS)
if (response.status_code == 200):
    response = json.loads(response.text)
    print('Connected to the OneDrive of', response['owner']['user']['displayName']+' (',response['driveType']+' ).', \
         '\nConnection valid for one hour. Reauthenticate if required.')
elif (response.status_code == 401):
    response = json.loads(response.text)
    print('API Error! : ', response['error']['code'],\
         '\nSee response for more details.')
else:
    response = json.loads(response.text)
    print('Unknown error! See response for more details.')

# List all files in OneDrive
items = json.loads(requests.get(URL + 'me/drive/root/children', headers=HEADERS).text)
items = items['value']
for entries in range(len(items)):
    print(items[entries]['name'], '| item-id >', items[entries]['id'])

# Set created_date & modified_date to specific file
created_date = '2022-09-29'
modified_date = '2022-09-30'

# Get only excel file that match to created_date & modified_date, you can apply with different file
file = []
for i in range(len(items)):
    items_id = items[i]['id'] 
    url = URL + 'me/drive/items/'+items_id+'/children'
    items_s = json.loads(requests.get(url, headers=HEADERS).text)
    items_s = items_s['value']
    for j in range(len(items_s)):
        if ((items_s[j]['fileSystemInfo']['createdDateTime'])[0:10] == created_date) and ((items_s[j]['fileSystemInfo']['lastModifiedDateTime'])[0:10] == modified_date):
            print(items_s[j]['name'], '|  createdDateTime >',items_s[j]['fileSystemInfo']['createdDateTime'])
            print(items_s[j]['name'], '|  lastModifiedDateTime >',items_s[j]['fileSystemInfo']['lastModifiedDateTime'])
            if len(items_s[j]['name'].split('.')) == 2 :
                if items_s[j]['name'].split('.')[1] == 'xlsx':
                    file.append(items_s[j]['name'])

# Collect data from content to excel file
files = list(range(len(file)))
for i in range(len(file)):
    url = URL + 'me/drive/root:/'+file[i]+':/content'
    data = requests.get(url, headers=HEADERS)
    open(file[i], 'wb').write(data.content)
    files[i] = pd.read_excel(file[i])