# from google.oauth2 import service_account
# from googleapiclient.discovery import build
import pandas as pd
import urllib.parse
from  sqlalchemy import create_engine 

def get_con():
    # SQL Server Connections
    server = 'localhost,1433'
    db = 'Practise_db'
    user = 'SA'
    password = 'Mahikolhe@23'
    driver = 'ODBC Driver 18 for SQL Server'
    
    params = urllib.parse.quote_plus(f'DRIVER={driver};SERVER={server};DATABASE={db};UID={user};PWD={password};TrustServerCertificate=yes')
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
    conn = engine.connect()
    return conn

# def get_data_from_sql():
#     data = pd.read_sql("SELECT * FROM study_notifier",con=get_con())
#     return data

# def load_data_to_sql():
#     SAMPLE_SPREADSHEET_ID = "1N_4zq8nnwCLv6QpGRxSpVSupSqzrwSR_3uEa_KXKHcc"
#     SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

#     creds = None
#     creds = service_account.Credentials.from_service_account_file("key.json",scopes = SCOPES)

#     service = build("sheets", "v4", credentials=creds)

#     sheet = service.spreadsheets()
#     result = (sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Plan!A1:D29').execute())
#     values = result.get("values", [])

#     data = pd.DataFrame(values)                                                 # Take Data from google sheet
#     data.columns = data.iloc[0]                                                 # Assigning First Row as header
#     data = data[1:]                                                             # Dropping First Row
#     data = data.reset_index(drop=True)                                          # Reseting index
#     data = data.infer_objects()                                                 # Convert Data types string to int 
#     data.to_sql('study_notifier',con=get_con(),if_exists='replace',index=False) # Load into SQL Table
#     data.to_sql('Emp',con=get_con(),if_exists='replace',index=False) # Load into SQL Table
#     print('Data load success')


