from os import listdir
from os.path import isfile, join
from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1MHGf57cymnw8hcXqEH3qWsNdq069BTYy'

# file_names = ['accounts.xlsx', 'company.png']

# A mime type is associated with a particular file extension
# found these by searching for .xlsx and .png here: https://learndataanalysis.org/commonly-used-mime-types/
mime_type = 'image/png'

file_names = [file for file in listdir('C:/Users/lenovo/Desktop/projects/Google Drive API Tutorial/google_drive_python_documents') if isfile(join('C:/Users/lenovo/Desktop/projects/Google Drive API Tutorial/google_drive_python_documents', file))]
# print(type(file_names))
# print(len(file_names))
# print(file_names)

# use the zip function to zip the file names and the mime types together
# for file_name, mime_type in zip(file_names, mime_types):
#     file_metadata = {
#         'name': file_name,
#         'parents': [folder_id]
#     }

#     media = MediaFileUpload('./google_drive_python_documents/{0}'.format(file_name), mimetype=mime_type)

#     service.files().create(
#         body = file_metadata,
#         media_body = media,
#         fields = 'id'
#     ).execute()

for file_name in file_names:
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload('./google_drive_python_documents/{0}'.format(file_name), mimetype=mime_type)

    service.files().create(
        body = file_metadata,
        media_body = media,
        fields = 'id'
    ).execute()