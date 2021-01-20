import re
from bs4 import BeautifulSoup


def cleanTitle(text):
    return text.replace("\n", "").splitlines()[0].replace(" ", "")


def extractHours(text):
    hours = ""

    match_hours = re.search(r"\((\d+(h|:))?(\d+(m?))?\)", text)
    if(match_hours):
        hours = "".join(match_hours.group())

    return hours


def extractMinutesCount(hours_text):
    minutes = 0

    match_hours = re.search(r"\d+(?=h|:)", hours_text)
    if(match_hours):
        minutes += int(match_hours.group()) * 60

    match_minutes = re.search(r"\d+(?=m|\))", hours_text)
    if(match_minutes):
        minutes += int(match_minutes.group())

    # print(
        # f"Hours matched: {match_hours.group() if match_hours else 0} \n Minuted matched: {match_minutes.group() if match_minutes else 0} \n -------- Total minutes: {minutes}------------")

    return minutes


def getSoup(text):
    return BeautifulSoup(text, "html.parser")


def getSections(soup):
    return soup.findAll("div", {"class": "section-title"})


def getSectionTitles(sections):
    _sections = []

    for section in sections:
        cleaned_text = cleanTitle(section.text)
        _sections.append(cleaned_text)

    return _sections


def getHoursPerSection(section_titles):
    _hours = []

    for section in section_titles:
        extracted_hours = extractHours(section)
        _hours.append(extracted_hours)

    return _hours


def getTotalHours(hours_per_section):
    _minutes = 0

    for section_hours in hours_per_section:
        minutes_number = extractMinutesCount(section_hours)
        _minutes += minutes_number

    return round(_minutes / 60, 1)
