#!/usr/bin python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Summay Inc.
#
"""Python client for Google Calendar V3 REST API.


"""
__author__ = 'static@siftcal.com (Ashutosh Priyadarshy)'


from requests_oauthlib import OAuth2Session

class GoogleCalendarAPI(object):

    def __init__(self, client_id=None, client_secret=None,
                 acc_token=None, ref_token=None, expires_in=None,
                 token_updater=None):
        """Construct a new authenticated instance of GoogleCalendarAPI V3.

        :param client_id: Client Id obtained in application creation.
        :param client_secret: Client Secret obtained in application creation.
        :param access_token: Token obtained via standard OAuth2 flow.
        :param refresh_token: Additional token obtained via standard OAuth2 flow.
        :param expires_in: Time until access_token expires.
        :param auto_refresh_url: HTTP endpoint to request new access token on refresh.
        :param token_updater: Method with one argument, token, to be used to update
                              your token database on automatic token refresh. If not
                              set a TokenUpdated warning will be raised when a token
                              has been refreshed. This warning will carry the token
                              in its token argument.
        :param kwargs: Arguments to pass to the Session (requests.session) constructor.
        """
        self.refresh_url = u'https://accounts.google.com/o/oauth2/token'
        self.base_url = u'https://www.googleapis.com/calendar/v3/'
        self.client_id = client_id
        self.client_secret = client_secret
        self.acc_token = acc_token
        self.ref_token = ref_token
        self.expires_in = expires_in
        token_dict = self.__construct_token_dictionary()
        refresh_dict = self.__construct_refresh_dictionary()
        self.session = OAuth2Session(client_id, token=token_dict,
                                     auto_refresh_url=self.refresh_url,
                                     auto_refresh_kwargs=refresh_dict,
                                     token_updater=token_updater)

    def __repr__(self):
        return u'<GoogleCalendarAPI Instance>'

    # Parameter constructors.

    def __construct_token_dictionary(self):
        return {u'access_token': self.acc_token,
                u'refresh_token': self.ref_token,
                u'token_type': u'Bearer',
                u'expires_in': self.expires_in}

    def __construct_refresh_dictionary(self):
        return {u'client_id':self.client_id,
                u'client_secret':self.client_secret}

    # URL Construction helpers.

    def __events_exturl_calendar_id(self, calendar_id):
        return self.base_url + u'calendars/{calendarId}/events/'.format(calendarId=calendar_id)

    def __events_exturl_calendar_id_event_id(self, calendar_id, event_id):
        return self.__events_exturl_calendar_id(calendar_id) + u'{eventId}/'.format(eventId=event_id)

    def __calendar_list_base_url(self):
        return self.base_url + u'users/me/calendarList/'

    def __calendar_list_ext_url_calendar_id(self, calendar_id):
        return self.base_url + u'users/me/calendarList/{calendarId}/'.format(calendarId=calendar_id)

    def __calendars_base_url(self):
        return self.base_url + u'calendars/'

    def __calendars_ext_url_calendar_id(self, calendar_id):
        self.__calendars_base_url() + u'{calendarId}/'.format(calendarId=calendar_id)

    def __settings_base_url(self):
        return self.base_url + u'/users/me/settings/'

    def __acl_base_url(self, calendar_id):
        return self.base_url + u'/calendars/{calendarId}/acl/'.format(calendarId=calendar_id)

    def __acl_ext_url_rule_id(self, calendar_id, rule_id):
        return __acl_base_url(calendar_id) + u'{ruleId}/'.format(ruleId=rule_id)

    # Acl Resource Calls.

    def acl_delete(self, calendar_id, rule_id):
        url = self.__acl_ext_url_rule_id(calendar_id, rule_id)
        return self.session.delete(url)

    def acl_get(self, calendar_id, rule_id):
        url = self.__acl_ext_url_rule_id(calendar_id, rule_id)
        return self.session.get(url)

    def acl_insert(self, calendar_id, body):
        url = self.__acl_base_url(calendar_id)
        return self.session.post(url, data=body)

    def acl_list(self, calendar_id, **kwargs):
        url = self.__acl_base_url(calendar_id)
        return self.session.get(url, {u'params':kwargs})

    def acl_patch(self, calendar_id, rule_id, body):
        url = self.__acl_ext_url_rule_id(calendar_id, rule_id)
        return self.session.patch(url, data=body)

    def acl_update(self, calendar_id, rule_id, body):
        url = self.__acl_ext_url_rule_id(calendar_id, rule_id)
        return self.session.put(url, data=body)

    def acl_watch(self, calendarId, body):
        url = self.__acl_base_url(calendar_id) + u'watch/'
        return self.session.post(url, data=body)

    # CalendarList Resource Calls.

    def calendar_list_delete(self, calendar_id):
        url =  __calendar_list_ext_url_calendar_id(calendar_id)
        return self.session.delete(url)

    def calendar_list_get(self, calendar_id):
        url =  __calendar_list_ext_url_calendar_id(calendar_id)
        return self.session.get(url)

    def calendar_list_insert(self, body, **kwargs):
        url = __calendar_list_base_url()
        return self.session.post(url, data=body, **{'params':kwargs})

    def calendar_list_list(self, **kwargs):
        url = __calendar_list_base_url()
        return self.session.get(url, **{'params':kwargs})

    def calendar_list_patch(self, body, **kwargs):
        url =  __calendar_list_ext_url_calendar_id(calendar_id)
        return self.session.patch(url, data=body, **{'params':kwargs})

    def calendar_list_update(self, body, **kwargs):
        url =  __calendar_list_ext_url_calendar_id(calendar_id)
        return self.session.put(url, data=body, **{'params':kwargs})

    def calendar_list_watch(self, body):
        url = __calendar_list_base_url() + u'watch/'
        return self.session.post(url, data=body)

    # Calendars Resource Calls.

    def calendars_clear(self, calendar_id):
        url = self.__calendars_ext_url_calendar_id(calendar_id) + u'clear/'
        return self.session.post(url)

    def calendars_delete(self, calendar_id):
        url = self.__calendars_ext_url_calendar_id(calendar_id)
        return self.session.delete(url)

    def calendars_get(self, calendar_id):
        url = self.__calendars_ext_url_calendar_id(calendar_id)
        return self.session.get(url)

    def calendars_insert(self, body):
        url = self.__calendars_base_url()
        return self.session.post(url, data=body)

    def calendars_patch(self, calendar_id, body):
        url = self.__calendars_ext_url_calendar_id(calendar_id)
        return self.session.patch(url, data=body)

    def calendars_update(self, calendar_id, body):
        url = self.__calendars_ext_url_calendar_id(calendar_id)
        return self.session.put(url, data=body)

    # Colors Resource Calls.

    def colors_get(self):
        url = self.base_url + u'colors/'
        return self.session.get(url)

    # Events Resource Calls.

    def events_delete(self, calendar_id, event_id, **kwargs):
        url = self. __events_exturl_calendar_id_event_id(calendar_id, event_id)
        return self.session.delete(url, **{'params':kwargs})

    def events_get(self, calendar_id, event_id, **kwargs):
        url = self.__events_exturl_calendar_id_event_id(calendar_id, event_id)
        return self.session.get(url, **{'params':kwargs})

    def events_import(self, calendar_id, body):
        url = self.__events_exturl_calendar_id(calendar_id) + u'import/'
        return self.session.post(url, data=body, **{'params':kwargs})

    def events_insert(self, calendar_id, body, **kwargs):
        url = self.__events_exturl_calendar_id(calendar_id)
        return self.session.post(url, data=body, **{'params':kwargs})

    def events_instances(self, calendar_id, event_id, **kwargs):
        url = self.__events_exturl_calendar_id_event_id(calendar_id, event_id) + u'instances/'
        return self.session.get(url, **{'params':kwargs})

    def events_list(self, calendar_id, **kwargs):
        url = self.__events_exturl_calendar_id(calendar_id)
        return self.session.get(url, **{'params':kwargs})

    def events_move(self, calendar_id, event_id, destination, **kwargs):
        url = self.__events_exturl_calendar_id_event_id(calendar_id, event_id) + u'move/'
        kwargs[u'destination'] = destination # Add
        return self.session.post(url, data=body, **{'params':kwargs})

    def events_patch(self, calendar_id, event_id, body, **kwargs):
        url = self.__events_exturl_calendar_id_event_id(calendar_id, event_id)
        return self.session.patch(url, data=body, **{'params':kwargs})

    def events_quick_add(self, calendar_id, text, **kwargs):
        url = self.__events_exturl_calendar_id(calendar_id) + u'quickAdd/'
        kwargs[u'text'] = text
        return self.session.post(url, **{'params':kwargs})

    def events_update(self, calendar_id, event_id, body, **kwargs):
        url = self.__events_exturl_calendar_id_event_id(calendar_id, event_id)
        return self.session.put(url, data=body, **{'params':kwargs})

    def events_watch(self, calendar_id, body):
        url = self.__events_exturl_calendar_id(calendar_id) + u'watch/'
        return self.session.post(url, data=body)

    # Freebusy Resource Calls.

    def freebusy_query(self, body):
        url = self.base_url + u'freeBusy/'
        return self.session.post(url, data=body)

    # Settings Resource Calls.

    def settings_get(self, setting):
        url = __settings_base_url() + u'{setting}/'.format(setting=setting)
        return self.session.get(url)

    def settings_list(self, **kwargs):
        url = __settings_base_url()
        return self.session.get(url, **{u'params':kwargs})

    def settings_watch(self, body):
        url = __settings_base_url + u'watch/'
        return self.session.post(url, data=body)

    # Channels Resource Calls.

    def channels_stop(self, body):
        url = self.base_url + u'channels/stop/'
        return self.session.post(url, data=body)











