# Upload predictions to Google Analytics (GA)

import argparse
from urllib.error import HTTPError
from googleapiclient import discovery
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from googleapiclient.http import MediaFileUpload

# Variables Setup

ACCOUNT_ID = '<Company GA account Id>'
WEB_PROPERTY_ID = '<Company GA property Id>'
CUSTOM_DATA_SOURCE_ID = '<Company GA data source Id>'  
CSV_IMPORT_FILE_LOCATION = '<location of file to upload>'
CREDENTIALS_KEY_FILE_LOCATION = '<api_key.json>'  

def get_service(api_name, api_version, scopes, key_file_location):
    
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, scopes)

    # Build the service object
    service = build(api_name, api_version, credentials=credentials)

    return service


def uploadCSV(service):
    try:
        media = MediaFileUpload(CSV_IMPORT_FILE_LOCATION,
                                mimetype='application/octet-stream',
                                resumable=False)
        daily_upload = service.management().uploads().uploadData(
                    accountId=ACCOUNT_ID,
                    webPropertyId=WEB_PROPERTY_ID,
                    customDataSourceId=CUSTOM_DATA_SOURCE_ID,
                    media_body=media).execute()

        # to get the status of the upload
        print(daily_upload)


    except TypeError as error:
        # Handle errors in constructing a query.
        print ('There was an error in constructing your query : %s' % error)

    except HTTPError as error:
        # Handle API errors.
            print ('There was an API error : %s : %s' %
                (error.resp.status, error.resp.reason))  


def main():
    # Define the auth scopes to request.
    scope = ['https://www.googleapis.com/auth/analytics.edit','https://www.googleapis.com/auth/analytics']

    # Authenticate and construct service.
    service = get_service('analytics', 'v3', scope, CREDENTIALS_KEY_FILE_LOCATION)

    # Execute the function: Upload CSV Data
    uploadCSV(service)


if __name__ == '__main__':
    main()