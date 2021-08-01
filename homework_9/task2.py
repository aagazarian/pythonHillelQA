from datetime import datetime, timedelta, date


def date_days_ago(days: int) -> date:
    past_date = (datetime.now() - timedelta(days)).date()
    return past_date


if __name__ == "__main__":
    print(date_days_ago(7))
