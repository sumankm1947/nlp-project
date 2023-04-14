import matplotlib.pyplot as plt
from wordcloud import WordCloud

def sentiment_analysis_visualisation(tweets):
    sentiment_counts = [len([t for t in tweets if t['sentiment'] == 'positive']),
                    len([t for t in tweets if t['sentiment'] == 'negative']),
                    len([t for t in tweets if t['sentiment'] == 'neutral'])]

    plt.bar(['Positive', 'Negative', 'Neutral'], sentiment_counts)
    plt.title('Sentiment Analysis of Russia-Ukraine War Tweets')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.show()

def topic_model_visualisation(topic_words):
    topic1_words = topic_words[0]
    topic2_words = topic_words[1]
    topic3_words = topic_words[2]
    topic4_words = topic_words[3]
    fig, axs = plt.subplots(2, 2, figsize=(10,10))

    wordcloud1 = WordCloud(background_color='white', width=800, height=600).generate(str(topic1_words))
    axs[0, 0].imshow(wordcloud1)
    axs[0, 0].set_title('Topic 1')

    wordcloud2 = WordCloud(background_color='white', width=800, height=600).generate(str(topic2_words))
    axs[0, 1].imshow(wordcloud2)
    axs[0, 1].set_title('Topic 2')

    wordcloud3 = WordCloud(background_color='white', width=800, height=600).generate(str(topic3_words))
    axs[1, 0].imshow(wordcloud3)
    axs[1, 0].set_title('Topic 3')

    wordcloud4 = WordCloud(background_color='white', width=800, height=600).generate(str(topic4_words))
    axs[1, 1].imshow(wordcloud4)
    axs[1, 1].set_title('Topic 4')

    for ax in axs.flat:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.label_outer()

    fig.suptitle('Word Clouds for Topics')

    plt.show()

