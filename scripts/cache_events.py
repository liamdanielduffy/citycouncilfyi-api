"""Cache all of the events to our Darklang backend & database.

1. Get all future events from the API
2. Get all extra details for those events by scraping the website
3. Merge into one list of future events with details
4. Cache all of those events to our Darklang backend & database by Upserting them (MUST BE an idempotent operation)

"""


from legistarnyc import base, events

def cache_events():
    # Get all future events from the API
    base
    # Get all extra details for those events by scraping the website
    # Merge into one list of future events with details