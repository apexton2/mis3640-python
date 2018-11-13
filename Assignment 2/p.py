import requests
import simplejson
import urllib
 
#----------------------------------------------------------------------
def getMovieDetails(key, title):
    """
    Get additional movie details
    """
    if "Shrek 2" in title:
        parts = title.split(" ")
        title = "+".join(parts)
 
    link = "http://api.rottentomatoes.com/api/public/v1.0/movies.json"
    url = "%s?apikey=%s&q=%s&page_limit=1"
    url = url % (link, key, title)
    res = requests.get(url)
    js = simplejson.loads(res.content)
 
    for movie in js["movies"]:
        ratings = movie["ratings"]
        print ("critics score: %s" % ratings["critics_score"])
        print ("audience score: %s" % ratings["audience_score"])