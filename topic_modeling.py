import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora, models


nltk.downloader.download('stopwords')
nltk.downloader.download('punkt')
nltk.downloader.download('wordnet')

topn_words = 3
topic_words = {}
    

def modeling(tweets):
    tweets_df = pd.DataFrame(tweets)

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    tweets_df['preprocessed_text'] = tweets_df['text'].apply(lambda x: [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(x.lower()) if word not in stop_words])
    tweets_df['preprocessed_text'] = tweets_df['preprocessed_text'].apply(lambda x: [word for word in x if word != ' '])

    dictionary = corpora.Dictionary(tweets_df['preprocessed_text'])

    corpus = [dictionary.doc2bow(text) for text in tweets_df['preprocessed_text']]

    lda_model = models.ldamodel.LdaModel(corpus, num_topics=4, id2word=dictionary, passes=10)

    for topic, words in lda_model.show_topics(num_topics=4, num_words=topn_words, formatted=False):
        topic_words['Topic #{}'.format(topic+1)] = [word[0] for word in words]
    topic1_words = topic_words['Topic #1']
    topic2_words = topic_words['Topic #2']
    topic3_words = topic_words['Topic #3']
    topic4_words = topic_words['Topic #4']

    return [topic1_words, topic2_words, topic3_words, topic4_words]


