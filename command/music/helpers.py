import json
import time

def getLastPlayed(id, env):
    f = open(env["DB_PATH"] + '/musicCache.json')
    jsonFile = json.load(f)
    f.close()
    try:
        return jsonFile[id]
    except:
        return 0

def updateEntry(id, env):
    f = open(env["DB_PATH"] + '/musicCache.json')
    jsonFile = json.load(f)
    f.close()
    jsonFile[id] = time.time()
    f = open(env["DB_PATH"] + '/musicCache.json', "w")
    f.write(json.dumps(jsonFile))
    f.close()

def getCache(env):
    f = open(env["DB_PATH"] + '/musicCache.json')
    jsonText = json.load(f)
    f.close()
    return jsonText
