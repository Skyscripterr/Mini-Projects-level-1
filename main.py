import gspread
from google.oauth2.service_account import Credentials

# Define the scope (access level)
scopes = ['https://www.googleapis.com/auth/spreadsheets']
# Load the credentials from the JSON file
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

# Authorize the client
client = gspread.authorize(creds) 

#access to the id of the sheet
sheet_url = "https://docs.google.com/spreadsheets/d/10jlGoI-1Cb66WM_4wFc1FIo8gbNjixB38YB-ca1umjU/edit?gid=0#gid=0"
#open the spreadsheet
workbook = client.open_by_url(sheet_url)

# TEST
# --value_list = sheet.sheet1.row_values(1)--
# --print(value_list)--

#list out all the worksheets we have 
# TEST
# sheets = map(lambda x: x.title, workbook.worksheets())
# print(list(sheets))
# TEST
# sheet = workbook.worksheet("Hello World")
# value = sheet.acell("A1").value
# print(value)

values = [
    ["Name","Price","Quality"],
    ["Basketball", 29.99, 1],
    ["jeans", 33.3, 2],
    ["Soap", 7.99, 3],
]

worksheet_list = map(lambda x: x.title, workbook.worksheets())
new_worksheet_name = "Values"

if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(new_worksheet_name, rows=10, cols=10)

sheet.clear()

sheet.update(f"A1:C{len(values)}", values)

sheet.update_cell(len(values)+ 1, 2, "=sum(B2:B4)")
sheet.update_cell(len(values)+ 1, 3, "=sum(C2:C4)")

sheet.format("A1:C1",{"textFormat":{"bold": True}})

#values_list = sheet.sheet1.row_values(1)
#print(values_list)