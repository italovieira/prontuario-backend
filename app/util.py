from datetime import datetime

def format_date(date):
        return date.isoformat(' ') if type(date) is datetime else date
