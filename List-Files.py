from Google import Create_Service
import pandas as pd

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1MHGf57cymnw8hcXqEH3qWsNdq069BTYy'

# since I just want the files...q stands for query
# grab the files and folders where the folder id is the same as the folder_id value above
query = f"parents = '{folder_id}'"

# you get all the files and folders in the particular folder represented by the folder_id
response = service.files().list(q=query).execute()

# because there can be multiple pages of results in the source folder on Google Drive, in case there is a nextPageToken returned, we can capture that
files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q = query, pageToken = nextPageToken).execute()

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