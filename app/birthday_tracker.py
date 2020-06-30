# app/birthday_tracker.py

import gspread
import os
import json

from pprint import pprint
from datetime import date, datetime
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

APP_ENV = os.getenv("APP_ENV", default="development") # use "production" on a remote server
DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
SHEET_NAME = os.environ.get("SHEET_NAME", "Products")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
MY_NAME = os.environ.get("MY_NAME")

def send_email(subject="[Daily Briefing] This is a test", html="<p>Hello World</p>"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)
    message = Mail(from_email=MY_EMAIL, to_emails=MY_EMAIL, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", e.message)
        return None

#
# AUTHORIZATION
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "auth", "spreadsheet_credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

#> <class 'list'>

email_birthdays = []

def get_todays_birthday():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

    #
    # READ SHEET VALUES
    #

    client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

    doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>

    print("-----------------")
    print("SPREADSHEET:", doc.title)
    print("-----------------")

    sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

    rows = sheet.get_all_records()
    todaysDate = date.today()
    todays_birthdays = []
    for row in rows:
        rowDate = datetime.strptime(row['DOB:'],"%m/%d/%Y").date().replace(year=todaysDate.year)
        if rowDate == todaysDate:
            todays_birthdays.append(row)
    return todays_birthdays

if __name__ == "__main__":

    birthday_results = get_todays_birthday() # invoke with custom params     
    print(birthday_results)

    html = ""
    html += f"<h3>Good Morning, {MY_NAME}!</h3>"

    html += "<h4>Today's Date</h4>"
    html += f"<p>{date.today().strftime('%A, %B %d, %Y')}</p>"

    html += f"<h4>Today's Birthdays</h4>"
    
    html += "<ul>"
    for birthday in birthday_results:
        html += f"<li>{birthday['First Name:']} {birthday['Last Name:']} , {birthday['Age']}</li>"
    html += "</ul>"
 
    send_email(subject="Birthday's Today", html=html)


