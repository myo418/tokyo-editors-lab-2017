import sys
import json
import pycurl
import urllib
import urllib.parse
from io import BytesIO

def getJson(url, params):
    try:
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, url + '?' + urllib.parse.urlencode(params))
        curl.setopt(pycurl.WRITEDATA, buffer)
        curl.perform()

        jsonString = buffer.getvalue().decode('UTF-8')
        data = json.loads(jsonString)

        return data;
    except:
        print(sys.exc_info())
        return [];

def postJson(url, params):
    try:
        buffer = BytesIO()
        field_data = urllib.parse.urlencode(params)
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.POSTFIELDS, field_data)
        curl.setopt(pycurl.WRITEDATA, buffer)
        curl.perform()
        jsonString = buffer.getvalue().decode('UTF-8')
        data = json.loads(jsonString)

        return data;
    except:
        print(sys.exc_info())
        return [];
