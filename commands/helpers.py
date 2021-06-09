import os
import discord
import requests
from asyncio import *

def retrieveCourse(course):
    URL = "https://tenta.davebay.net/api/course/" + course + "/exams"
    request = requests.get(url = URL)
    json = request.json()
    return json

def isOrdinarieTenta(json,tenta):
    total = 0
    for entry in json:
        total += entry.get("failed") + entry.get("three") + entry.get("four") + entry.get("five")
    total = total / len(json)
    return (tenta > total + 20)
