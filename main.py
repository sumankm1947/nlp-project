from data_collection import get_data
from data_annotation import classify_sentiment
from topic_modeling import modeling
from visualisation import sentiment_analysis_visualisation, topic_model_visualisation

import os
from dotenv import load_dotenv
load_dotenv()

BEARER_TOKEN = os.getenv('BEARER_TOKEN')
query = 'ukrainewar -is:retweet'
data = []
tweets = []
topic_words = []

#####################################
############## GET DATA #############
#####################################
data = get_data(query=query, BEARER_TOKEN=BEARER_TOKEN)
# with open('data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         if line.strip():
#             data.append(line.strip())

#####################################
### CONVERT DATA TO PROPER FORMAT ###
######## AND WITH SENTIMENT #########
#####################################
for d in data:
    temp = {'text': d, 'sentiment': classify_sentiment(d)}
    tweets.append(temp)

#####################################
############# MODELING ##############
#####################################
topic_words = modeling(tweets=tweets)

#####################################
########### VISUALISATION ###########
#####################################
sentiment_analysis_visualisation(tweets=tweets)
topic_model_visualisation(topic_words=topic_words)
