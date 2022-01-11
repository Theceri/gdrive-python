from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# print('============================================================')
# print(type(service))
# print('============================================================')

file_id = '143pxSPZSI5N5OmRScyuDYdzfaW4vFDZz'

request_body = {
    'role': 'reader',
    'type': 'anyone'
}

response_permission = service.permissions().create(
    fileId = file_id,
    body = request_body
).execute()

print(response_permission)
# print('============================================================')
# print(type(response_permission))
# print('============================================================')

"""
{'kind': 'drive#permission', 'id': 'anyoneWithLink',
'type': 'anyone', 'role': 'reader', 'allowFileDiscovery': False}
"""

response_share_link = service.files().get(
    fileId = file_id,
    fields = 'webViewLink'
).execute()

print(response_share_link)

"""
{'webViewLink': 'https://drive.google.com/file/d/143pxSPZSI5N5OmRScyuDYdzfaW4vFDZz/view?usp=drivesdk'}
"""