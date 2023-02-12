from datetime import datetime, date, timedelta
import requests
from legistarnyc import base, events
import pytz

eventsScraper = events.LegistarAPIEventScraperZip()

tz = pytz.timezone('US/Eastern')
# why is this the event key? Why not just use the EventID? I guess because there IS NO EventID on the web interface. OF course...
event_key = ('Subcommittee on Zoning and Franchises', datetime(2023, 1, 24, 10, 0, tzinfo=tz))

[print(event) for event in eventsScraper._events]
breakpoint()