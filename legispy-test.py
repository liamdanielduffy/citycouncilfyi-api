# legispy-test.py
# from api import Legistar
from datetime import datetime, date, timedelta
import requests
from legistarnyc import base, events
import pytz
# from scraperlegistar import LegistarAPIScraper, LegistarEventsScraper


# class LegistarAPIScraper(base.LegistarAPIScraper):
#     API_KEY = 'Uvxb0j9syjm3aI8h46DhQvnX5skN4aSUL0x_Ee3ty9M.ew0KICAiVmVyc2lvbiI6IDEsDQogICJOYW1lIjogIk5ZQyByZWFkIHRva2VuIDIwMTcxMDI2IiwNCiAgIkRhdGUiOiAiMjAxNy0xMC0yNlQxNjoyNjo1Mi42ODM0MDYtMDU6MDAiLA0KICAiV3JpdGUiOiBmYWxzZQ0KfQ'
#     BASE_URL = 'https://webapi.legistar.com/v1/nyc'

#     def search(self, route, item_key, search_conditions):
#         """
#         Base function for searching the Legistar API.

#         Arguments:

#         route -- The path to search, i.e. /matters/, /events/, etc
#         item_key -- The unique id field for the items that you are searching.
#                     This is necessary for proper pagination. examples
#                     might be MatterId or EventId
#         search_conditions -- a string in the OData format for the
#                              your search conditions http://www.odata.org/documentation/odata-version-3-0/url-conventions/#url5.1.2

#                              It would be nice if we could provide a
#                              friendly search API. Something like https://github.com/tuomur/python-odata


#         Examples:
#         # Search for bills introduced after Jan. 1, 2017
#         search('/matters/', 'MatterId', "MatterIntroDate gt datetime'2017-01-01'")
#         """

#         search_url = self.BASE_URL + route

#         params = {'$filter': search_conditions, 'token': self.API_KEY}

#         try:
#             yield from self.pages(search_url,
#                                   params=params,
#                                   item_key=item_key)
#         except requests.HTTPError as e:
#             if e.response.status_code == 400:
#                 raise ValueError(e.response.json()['Message'])
#             raise

# Overwrite our own version of the EventScraperZip which is needed to scrape meeting topic info
# class LegistarAPIEventScraperZip(events.LegistarAPIEventScraperZip):
#     '''
#     There are some inSite sites that have information that only appears
#     event listing page, like NYC's 'Meeting Topic.' This scraper visits
#     the listing page and attempts to zip API and web events together
#     '''
#     def _event_key(self, event, web_scraper):
#         '''Since Legistar InSite contains more information about events than
#         are available in the API, we need to scrape both. Then, we have
#         to line them up. This method makes a key that should be
#         uniquely identify every event and will allow us to link
#         events from the two data sources.
#         '''
#         response = web_scraper.get(event['iCalendar']['url'], verify=False)
#         event_time = web_scraper.ical(response.text).subcomponents[0]['DTSTART'].dt
#         event_time = events.pytz.timezone(self.TIMEZONE).localize(event_time)
#         key = (event['Name'], # CHANGED FROM THE ORIGINAL
#                event_time)

#         return key

# scraper.retry_attempts = 0
# scraper.requests_per_minute = 0


eventsScraper = events.LegistarAPIEventScraperZip()

# def test():
#     return scraper.search('/matters/', 'MatterId', "MatterIntroDate gt datetime'2023-01-01'")

# def eventsTest():
#     today = date.today()
#     two_weeks = today + timedelta(days=14)
#     events_generator = scraper.search('/events/', 'EventId', f"EventDate gt datetime'{today}' and EventDate lt datetime'{two_weeks}'")
#     for event in events_generator:
#         event_details = eventsScraper.web_detail(event)
#         print(event_details)
#     # ??


# Example object from API:
# Note that it is missing 1 particular thing: Meeting Topic
example = {
    'EventAgendaFile': 'https://nyc.legistar1.com/nyc/meetings/2023/2/19808_A_Committee_on_Higher_Education_23-02-08_Committee_Green_Sheet.pdf',
    'EventAgendaLastPublishedUTC': '2023-01-30T14:39:54.157',
    'EventAgendaStatusId': 2,
    'EventAgendaStatusName': 'Final',
    'EventBodyId': 15,
    'EventBodyName': 'Committee on Higher Education',
    'EventComment': 'Jointly with the Committee on Education.',
    'EventDate': '2023-02-08T00:00:00',
    'EventGuid': '9B254A6C-2D2E-4A6D-9708-775BA3191117',
    'EventId': 19808,
    'EventInSiteURL': 'https://nyc.legistar.com/MeetingDetail.aspx?LEGID=19808&GID=61&G=2FD004F1-D85B-4588-A648-0A736C77D6E3',
    'EventItems': [],
    'EventLastModifiedUtc': '2023-01-30T14:39:54.307',
    'EventLocation': 'Council Chambers - City Hall',
    'EventMedia': None,
    'EventMinutesFile': None,
    'EventMinutesLastPublishedUTC': None,
    'EventMinutesStatusId': 1,
    'EventMinutesStatusName': 'Draft',
    'EventRowVersion': 'AAAAAOargFE=',
    'EventTime': '1:00 PM',
    'EventVideoPath': None,
    'EventVideoStatus': 'Public'
  }

# Example object from Scraper:
test = {
    'Name': 'Subcommittee on Zoning and Franchises',
    'Meeting Date': '1/24/2023',
    'iCalendar': {'url': 'https://nyc.legistar.com/View.ashx?M=IC&ID=1076123&GUID=4F9CBED2-E16D-4DF5-9796-3CE600A7435D'},
    'Meeting Time': '10:00 AM',
    'Meeting Location': '250 Broadway - Committee Room, 14th Floor',
    'Meeting\xa0Topic': 'Multiple meeting items, please see Meeting Details for more information',
    'Meeting Details': {
        'label': 'Meeting\xa0details',
        'url': 'https://nyc.legistar.com/MeetingDetail.aspx?ID=1076123&GUID=4F9CBED2-E16D-4DF5-9796-3CE600A7435D&Options=info|&Search='
    },
    'Agenda': {
        'label': 'Agenda',
        'url': 'https://nyc.legistar.com/View.ashx?M=A&ID=1076123&GUID=4F9CBED2-E16D-4DF5-9796-3CE600A7435D'
    }, 
    'Minutes': {
        'label': 'Minutes',
        'url': 'https://nyc.legistar.com/View.ashx?M=M&ID=1076123&GUID=4F9CBED2-E16D-4DF5-9796-3CE600A7435D'
    },
    'Multimedia': {
        'label': 'Video', 
        'url': 'https://nyc.legistar.com/Video.aspx?Mode=Auto&URL=aHR0cHM6Ly9jb3VuY2lsbnljLnZpZWJpdC5jb20vdm9kLz9zPXRydWUmdj1OWUNDLVBWLTI1MC0xNF8yMzAxMjQtMTAyMTQxY3V0Lm1wNA%3d%3d&Mode2=Video'
    }
    }


tz = pytz.timezone('US/Eastern')
# why is this the event key? Why not just use the EventID? I guess because there IS NO EventID on the web interface. OF course...
event_key = ('Subcommittee on Zoning and Franchises', datetime(2023, 1, 24, 10, 0, tzinfo=tz))


# event_details = eventsScraper.web_detail(example)
# event_details = eventsScraper
[print(event) for event in eventsScraper._events]
# TODO: Figure out how to get the events for ONLY the ones from our API Call
breakpoint()