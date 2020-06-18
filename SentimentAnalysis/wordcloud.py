
import pandas as pd
import itertools
import matplotlib.pyplot as plt

from collections import Counter
from wordcloud import WordCloud


#Import datasets
reviews_top_negative_books = pd.read_csv('./Documents/università/DataAnalytics/amazon_review/data/reviews_top_negative_books.csv')



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


    
    sentences2 = (list(itertools.chain(reviews_top_negative_books["tokens_stemming"])))
    flat_list2 = [item for sublist2 in sentences2 for item in sublist2]
    c2 = Counter(flat_list2)

    fig2 = plt.figure(figsize=(20,14))
    wordcloud2 = WordCloud(background_color="white").generate(" ".join(flat_list2))
    plt.imshow(wordcloud2,interpolation='bilinear')
    plt.axis("off")
    
    
wordcloud(reviews_top_negative_books)
    