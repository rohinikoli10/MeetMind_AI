from enum import Enum


class MeetingType(str, Enum):
    BUSINESS = "Business"
    LECTURE = "Lecture"
    WEBINAR = "Webinar"
    WORKSHOP = "Workshop"
    INTERVIEW = "Interview"
    PERSONAL = "Personal"


   