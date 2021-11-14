from datetime import datetime, timedelta
from cal_setup import get_calendar_service

def main(a,b,c,d,e,f):
   service = get_calendar_service()

   tomorrow = datetime(int(a),int(b),int(c),int(d),int(e))+timedelta(days=1)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary":f,
           "description": "K-äratus",
           "start": {"dateTime": start, "timeZone": 'Europe/Tallinn'},
           "end": {"dateTime": end, "timeZone": 'Europe/Tallinn'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])