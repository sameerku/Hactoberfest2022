 #Importing os and pickle module in program  
import os  
import pickle  
# Creating utils for Gmail APIs  
from googleapiclient.discovery import build  
from google_auth_oauthlib.flow import InstalledAppFlow  
from google.auth.transport.requests import Request  
# Importing libraries for encoding/decoding messages in base64  
from base64 import urlsafe_b64decode, urlsafe_b64encode  
# Importing libraries for dealing with the attachment of MIME types in Gmail  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage  
from email.mime.audio import MIMEAudio  
from email.mime.base import MIMEBase  
from email.mime.multipart import MIMEMultipart  
from mimetypes import guess_type as guess_mime_type  
  
# Request all access from Gmail APIs and project  
SCOPES = ['https://mail.google.com/']  
OurEmailID = 'OurMail@gmail.com' # giving our Gmail Id  
  
# using a default function to authenticate Gmail APIs  
def authenticateGmailAPIs():  
    creds = None  
    # Authorizing the Gmail APIs with tokens of pickles  
    if os.path.exists("token.pickle"): # using if else statement  
        with open("token.pickle", "rb") as token:  
            creds = pickle.load(token)  
    # If there are no valid credentials available in device, we will let the user sign in manually  
    if not creds or not creds.valid:  
        if creds and creds.expired and creds.refresh_token:  
            creds.refresh(Request())  
        else:  
            flow = InstalledAppFlow.from_client_secrets_file('client_secret_107196167488-dh4b2pmpivffe011kic4em9a4ugrcooi.apps.googleusercontent.com.json', SCOPES) # downloaded credential name  
            creds = flow.run_local_server(port=0) # running credentials  
        # Save the credentials for the next run  
        with open("token.pickle", "wb") as token:  
            pickle.dump(creds, token)  
    return build('Gmail', 'v1', credentials=creds) # using Gmail to authenticate  
  
# Get the Gmail API service by calling the function  
service = authenticateGmailAPIs()  
