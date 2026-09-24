from datetime import datetime


DATE_FORMAT = "%d %b %Y"


def calculate_variance(actual_date, baseline_date):

    actual = datetime.strptime(
        actual_date,
        DATE_FORMAT
    )

    baseline = datetime.strptime(
        baseline_date,
        DATE_FORMAT
    )

    return (actual - baseline).days


def variance_colour(days):

    if days > 0:
        return "#DC2626"

    return "#16A34A"


def variance_text(days):

    if days > 0:
        return f"+{days} Days"

    return f"{days} Days"
