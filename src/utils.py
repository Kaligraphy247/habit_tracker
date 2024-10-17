import datetime


def compare_datetimes(dt0: datetime.datetime, dt1: datetime.datetime) -> bool:
    """Compare two datetimes. Returns True if dt1 == dt2."""
    fmt = "%Y-%m-%d"  # Format with strf
    return dt0.strftime(fmt) == dt1.strftime(fmt)
