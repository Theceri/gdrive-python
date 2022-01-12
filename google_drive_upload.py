from os import listdir
from os.path import isfile, join
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import pandas as pd

################ variables shared by all the functionalities ####################
file_names = [file for file in listdir('C:/Users/lenovo/Desktop/projects/Google Drive API Tutorial/google_drive_python_documents') if isfile(
    join('C:/Users/lenovo/Desktop/projects/Google Drive API Tutorial/google_drive_python_documents', file))]

# env stuff?
CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

################ variables related to uploading a file to Google Drive ####################
# env?
destination_folder_id = '1MHGf57cymnw8hcXqEH3qWsNdq069BTYy'

# env?
mime_type = 'image/png'

################ variables related to obtaining the url of a file on Google Drive ####################
gdrive_file_id = '143pxSPZSI5N5OmRScyuDYdzfaW4vFDZz'

request_body = {
    'role': 'reader',
    'type': 'anyone'
}

response_permission = service.permissions().create(
    fileId=gdrive_file_id,
    body=request_body
).execute()

################ variables related to listing the urls of the files in a Google Drive folder ####################
# the folder whose file url's are to be listed
origin_folder_id = '1MHGf57cymnw8hcXqEH3qWsNdq069BTYy'

# since I just want the files...q stands for query
# grab the files and folders where the folder id is the same as the origin_folder_id value above
query = f"parents = '{origin_folder_id}'"

# you get all the files and folders in the particular folder represented by the origin_folder_id
response = service.files().list(q=query).execute()

# because there can be multiple pages of results in the source folder on Google Drive, in case there is a nextPageToken returned, we can capture that
files = response.get('files')
nextPageToken = response.get('nextPageToken')


class Google_Drive_Upload_And_Generate_Url:
    def __init__(self, file):
        pass

    def upload(self, file_path):
        for file_name in file_names:
            file_metadata = {
                'name': file_name,
                'parents': [destination_folder_id]
            }

            media = MediaFileUpload(
                './google_drive_python_documents/{0}'.format(file_name), mimetype=mime_type)

            service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()

    def generate_share_url(self, file_id):
        # generating the shareable url
        response_share_link = service.files().get(
            fileId=gdrive_file_id,
            fields='webViewLink'
        ).execute()

        print(response_share_link)

    def list_urls_of_all_files_in_a_google_drive_folder(self):
        while nextPageToken:
            response = service.files().list(q=query, pageToken=nextPageToken).execute()

            # append the results set using the append() method
            files.extend(response.get('files'))

            # get the token for the next page of results so that is there is one, repeat the process as long as there is a nextPageToken
            nextPageToken = response.get('nextPageToken')


        # present the results as a pandas dataframe, and styling the dataframe before printing the data
        pd.set_option('display.max_columns', 100)
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.min_rows', 500)
        pd.set_option('display.max_colwidth', 150)
        pd.set_option('display.width', 200)
        pd.set_option('expand_frame_repr', True)
        df = pd.DataFrame(files)
        print(df)

        print(type(files))
        print(len(files))
        print(files)

        for file in files:
            print(f"https://drive.google.com/file/d/{file['id']}/view")