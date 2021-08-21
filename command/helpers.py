import requests


def retrieveCourse(course):
    URL = "https://tenta.davebay.net/api/v1/course/" + course + "/exams"
    request = requests.get(url=URL)
    json = request.json()
    return json
