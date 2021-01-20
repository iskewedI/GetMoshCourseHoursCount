import sys
import requests
from CourseHours import getSoup, getSections, getSectionTitles, getHoursPerSection, getTotalHours

try:
    args = sys.argv
    if(len(args) < 2):
        print("URL is required. Exiting...")
        exit()

    url = sys.argv[1]

    search_result = requests.get(url)

    if(search_result.status_code != 200):
        print(f"Invalid URL -> Status received: {search_result.status_code}")
        exit()

    result_Soup = getSoup(search_result.text)

    sections = getSections(result_Soup)

    section_titles = getSectionTitles(sections)

    hours_per_section = getHoursPerSection(section_titles)

    hours_count = getTotalHours(hours_per_section)

    print(hours_count)
except Exception as error:
    print("An error has ocurred -> ", error)
