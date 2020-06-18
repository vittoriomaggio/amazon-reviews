import pandas as pd
dataset = pd.read_csv('./Documents/università/DataAnalytics/amazon_review/data/sentiment_distribution.csv')
products = pd.read_csv('./Documents/università/DataAnalytics/amazon_review/data/tokenizedDataset.csv')
products = products.drop_duplicates(subset='product')

category=pd.DataFrame()
category['product'] = products['product']
category['category'] = products['category']


dataset = pd.merge(dataset, category)
dataset = dataset.sort_values(by = ['reviews_number'], ascending=False)



top_popular  = dataset[:200]

top_books = top_popular[top_popular['category'] == 'books']
top_videogames = top_popular[top_popular['category'] == 'videogames']
top_dvd = top_popular[top_popular['category'] == 'dvd']
top_music = top_popular[top_popular['category'] == 'music']

books_number = len(top_books)
videogames_number = len(top_videogames)
dvd_number = len(top_dvd)
music_number = len(top_music)

books_percent = books_number/200
videogames_percent = videogames_number/200
dvd_percent = dvd_number/200
music_percent = music_number/200



import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go


langs = ['Books', 'Videogames', 'DVD', 'Music']
val = [books_percent, videogames_percent, dvd_percent, music_percent]
pie_category = go.Pie(labels = langs, values = val)
data = [pie_category]
fig = go.Figure(data = data)
plot(fig)
fig.write_image("./pie_category.jpeg")


top_positive_books = top_books.sort_values(by = ['positive_percent'], ascending=False)[:5]
top_negative_books = top_books.sort_values(by = ['negative_percent'], ascending=False)[:5]
top_positive_videogames = top_videogames.sort_values(by = ['positive_percent'], ascending=False)[:5]
top_negative_videogames = top_videogames.sort_values(by = ['negative_percent'], ascending=False)[:5]
top_positive_dvd = top_dvd.sort_values(by = ['positive_percent'], ascending=False)[:5]
top_negative_dvd = top_dvd.sort_values(by = ['negative_percent'], ascending=False)[:5]


reviews = pd.read_csv('./Documents/università/DataAnalytics/amazon_review/data/tokenizedDataset.csv')
reviews_top_positive_books = pd.merge(top_positive_books, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'title', 'tokens', 'tokens_stemming', 'sentiment']]
reviews_top_negative_books = pd.merge(top_negative_books, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_positive_books = reviews_top_positive_books[reviews_top_positive_books['sentiment'] == 'positive']
reviews_top_negative_books = reviews_top_negative_books[reviews_top_negative_books['sentiment']=='negative']

reviews_top_positive_videogames = pd.merge(top_positive_videogames, reviews[['product','tokens_stemming','tokens','sentiment']], on='product')[['product', 'category', 'title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_negative_videogames = pd.merge(top_negative_videogames, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_positive_videogames = reviews_top_positive_videogames[reviews_top_positive_videogames['sentiment'] == 'positive']
reviews_top_negative_videogames = reviews_top_negative_videogames[reviews_top_negative_videogames['sentiment']=='negative']

reviews_top_positive_dvd = pd.merge(top_positive_dvd, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_negative_dvd = pd.merge(top_negative_dvd, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'title', 'tokens', 'tokens_stemming', 'sentiment']]
reviews_top_positive_dvd = reviews_top_positive_dvd[reviews_top_positive_dvd['sentiment'] == 'positive']
reviews_top_negative_dvd = reviews_top_negative_dvd[reviews_top_negative_dvd['sentiment']=='negative']


'''Save to csv '''
reviews_top_positive_books.to_csv('./Documents/università/DataAnalytics/amazon_review/data/reviews_top_positive_books.csv')
reviews_top_negative_books.to_csv('./Documents/università/DataAnalytics/amazon_review/data/reviews_top_negative_books.csv')

reviews_top_positive_videogames.to_csv('./Documents/università/DataAnalytics/amazon_review/data/reviews_top_positive_videogames.csv')
reviews_top_negative_videogames.to_csv('./Documents/università/DataAnalytics/amazon_review/data/reviews_top_negative_videogames.csv')

reviews_top_positive_dvd.to_csv('./Documents/università/DataAnalytics/amazon_review/data/reviews_top_positive_dvd.csv')
reviews_top_negative_dvd.to_csv('./Documents/università/DataAnalytics/amazon_review/data/reviews_top_negative_dvd.csv')


