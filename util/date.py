from datetime import datetime, tzinfo, timedelta

def get_formatted_date():
    now = datetime.now(GMT1())
    formatted_now = now.strftime("%a, %d %b %Y %H:%M:%S %Z")
    return formatted_now.encode()

class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=0)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "GMT"
    