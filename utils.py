
from datetime import datetime


def get_timestamp():
    # timestamp
    unformatted_time = datetime.now()
    timestamp = unformatted_time.strftime("%Y%m%d%H%M%S")

    return timestamp
