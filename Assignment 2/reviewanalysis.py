from nltk.sentiment.vader import SentimentIntensityAnalyzer
from imdbpie import Imdb
"""import natural language processing package and Imdb package"""

imdb = Imdb()
print ("please enter a movie title:")
name = input()
"""User enters movie title"""

movie_id= imdb.search_for_title(name)[0]['imdb_id']
reviews = imdb.get_title_user_reviews(movie_id)
"""function identifies movie id based on its title"""

print(reviews['reviews'][0]['reviewText'])

review_1 = reviews['reviews'][0]['reviewText']
score = SentimentIntensityAnalyzer().polarity_scores(review_1)
""" feeds the written review from Imdb into the sentiment analyzer.
    provides output in form of a polarity score: pos. neg. neu. compound
"""
print(score)
