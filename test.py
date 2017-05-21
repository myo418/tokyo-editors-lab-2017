from model import articles
from model import config
from model import curl
import pycurl

def getGeometry(text):
    conf = config.getData()
    queryArray = {
        'key': conf['google']['key'],
        'query': text
    }

    data = curl.getJson(conf['google']['placeUrl'], queryArray)
    try:
        return data['results'][0]['geometry']['location']
    except:
        return []

if __name__ == '__main__':
    print(getGeometry('広島'))
    """
    lat = 32.80589
    lng = 130.69181
    article = articles.getArticles(lat, lng)
    print(article)
    """
