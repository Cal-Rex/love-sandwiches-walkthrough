import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')
# checks API Works:
# sales = SHEET.worksheet('sales')
#
# data = sales.get_all_values()
#
# print(data)


def get_sales_data():
    """
    Get sales figures input from user
    """
    print("please enter sales data from market")
    print("data should be entered as 6 numerical values")
    print("with no spaces by commas.")
    print("Example: 1,2,3,4,5,6\n")

    data_str = input("Enter your data here: ")
    # print(f"\nThe data provided is {data_str}")
    sales_data = data_str.split(",")
    # print(f"supplied data has now been converted to: {sales_data}")
    validate_data(sales_data)


def validate_data(values):
    """
    docstring 
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"6 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")


get_sales_data()