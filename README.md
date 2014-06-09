google-calendar-v3
==================

Google Calendar V3 Python Client

Google Calendar V3 provides an API client that can be authenticated
using the following:
    access_token, refresh_token, client_id, and client_secret

How to Install:

```
pip install GoogleCalendarV3
```

How to use:

```
# Import the GoogleCalendarAPI Class.
from google_calendar_v3 import GoogleCalendarAPI

# Define a token handler for use on token refresh.
def new_token_handler(token):
    # Do something with your token. Like stick it in a db.
    print "A new token arrived: "
    print token

# Enter in your various credentials here.
access_token = "<YOUR_ACCESS_TOKEN>"
refresh_token = "<YOUR_REFRESH_TOKEN>"
client_id = "<YOUR_CLIENT_ID>"
client_secret = "<YOUR_CLIENT_SECRET>"

# Create an instance of the Google Calendar API.
gapi = GoogleCalendarAPI(client_id=client_id, client_secret=client_secret,
             acc_token=access_token, ref_token=refresh_token, expires_in=-30,
             token_updater=new_tokenzzz)

# Do something with it.
r  = gapi.settings_list("dateFieldOrder")
print t.text
```

Once authenticated you can easily call any of the methods for the
various resources associated with the API.

Each instance method of the GoogleCalendarAPI is a method for a resource.
Required parameters are enforced by the function header and any additional
query parameters arguments or the body data must be constructed and passed
in as kwargs or as body respectively.

