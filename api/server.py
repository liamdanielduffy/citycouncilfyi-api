from flask import Flask, request, jsonify
from datetime import datetime
from legistarnyc import base, events
import warnings

# we make https requests to the city council website, which creates lots of noise in logs
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

app = Flask(__name__)

def get_date_from_mm_dd_yyyy(date_str):
    return datetime.strptime(date_str, "%m/%d/%Y").date()

def list_past_events_until(date_str):
    gte_date = get_date_from_mm_dd_yyyy(date_str)
    events = eventsScraper._events
    past_events = []
    for event_tuple in events:
        event = event_tuple[1]
        event_date_string = event['Meeting Date']
        event_date = get_date_from_mm_dd_yyyy(event_date_string)
        if gte_date <= event_date:
            past_events.append(event)
        else:
            break
    return past_events

eventsScraper = events.LegistarAPIEventScraperZip()

app = Flask(__name__)

@app.route('/')
def hi():
    return 'hi'

@app.route('/events_on_or_after', methods=['POST'])
def get_past_events():
    gte_date = request.json['date']
    past_events = list_past_events_until(gte_date)
    return jsonify({'past_events': past_events})

if __name__ == '__main__':
    app.run(debug=True)