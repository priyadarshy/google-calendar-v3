===================
Google Calendar V3
===================

Google Calendar V3 provides an API client that can be authenticated
using the following:
    access_token, refresh_token, client_id, and client_secret

Once authenticated you can easily call any of the methods for the
various resources associated with the API.

Each instance method of the GoogleCalendarAPI is a method for a resource.
Required parameters are enforced by the function header and any additional
query parameters arguments or the body data must be constructed and passed
in as kwargs or as body respectively.
