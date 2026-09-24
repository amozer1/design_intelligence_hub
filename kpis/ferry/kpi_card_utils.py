from kpis.ferry.kpi_card_styles import (
    GREEN,
    RED,
    AMBER,
    BLUE,
)


def trend_colour(delta):

    if delta > 0:
        return GREEN

    if delta < 0:
        return RED

    return BLUE


def variance_colour(days):

    if days <= -15:
        return RED

    if days <= -5:
        return AMBER

    return GREEN


def float_colour(days):

    if days >= 15:
        return GREEN

    if days >= 5:
        return AMBER

    return RED
