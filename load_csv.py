import requests
import pandas as pd
from io import StringIO
import google_sheet_to_sql as db

url = 'https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv'
page = requests.get(url)

df = pd.read_csv(StringIO(page.text), sep=',')
print(df)
conn = db.get_con()
df.to_sql('Emp', con=conn, if_exists='replace',
          index=False)  # Load into SQL Table
