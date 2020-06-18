import pandas as pd
import itertools
import matplotlib.pyplot as plt

from collections import Counter
from wordcloud import WordCloud


#Import datasets
reviews_top_negative_books = pd.read_csv('./top/reviews_top_negative_books.csv')
reviews_top_negative_dvd = pd.read_csv('./top/reviews_top_negative_dvd.csv')
reviews_top_negative_videogames = pd.read_csv('./top/reviews_top_negative_videogames.csv')

reviews_top_positive_books = pd.read_csv('./top/reviews_top_positive_books.csv')
reviews_top_positive_dvd = pd.read_csv('./top/reviews_top_positive_dvd.csv')
reviews_top_positive_videogames = pd.read_csv('./top/reviews_top_positive_videogames.csv')


def wordcloud (df):
    i=0
    while i<len(df):
        l = df['tokens_stemming'][i].replace("'", "").replace("[","").replace("]","").replace(" ","").split(',')
        df['tokens_stemming'][i] = l
        i=i+1        
            
    i=0
    while i<len(df):
        l = df['tokens'][i].replace("'", "").replace("[","").replace("]","").replace(" ","").split(',')
        df['tokens'][i] = l
        i=i+1
    
    sentences = (list(itertools.chain(df["tokens_stemming"])))
    flat_list = [item for sublist in sentences for item in sublist] 
    c = Counter(flat_list)
    
    print(c.most_common(10))
    
    fig = plt.figure(figsize=(20,14))
    wordcloud = WordCloud(background_color="white").generate(" ".join(flat_list))
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    
wordcloud(reviews_top_negative_books)
wordcloud(reviews_top_negative_dvd)
wordcloud(reviews_top_negative_videogames)   

wordcloud(reviews_top_positive_books)
wordcloud(reviews_top_positive_dvd)
wordcloud(reviews_top_positive_videogames)    