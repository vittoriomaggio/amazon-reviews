import pandas as pd
dataset = pd.read_csv(r'./data/sentiment_distribution.csv')
products = pd.read_csv(r'./data/tokenizedDataset.csv')
products = products.drop_duplicates(subset='product')

category=pd.DataFrame()
category['product'] = products['product']
category['category'] = products['category']

#Add category 
dataset = pd.merge(dataset, category)
dataset = dataset.sort_values(by = ['reviews_number'], ascending=False)

top_popular  = dataset[:200]

#Save tokenized dataset of most popular
tokenizedDataset = pd.read_csv('./data/tokenizedDataset.csv')
tokenizedDataset_top = pd.merge(top_popular['product'], tokenizedDataset )
tokenizedDataset_top.to_csv('./data/tokenizedDataset_top.csv')

#Dataset by category 
top_books = top_popular[top_popular['category'] == 'books']
top_videogames = top_popular[top_popular['category'] == 'videogames']
top_dvd = top_popular[top_popular['category'] == 'dvd']
top_music = top_popular[top_popular['category'] == 'music']

#category percentage
books_number = len(top_books)
videogames_number = len(top_videogames)
dvd_number = len(top_dvd)
music_number = len(top_music)

books_percent = books_number/1000
videogames_percent = videogames_number/1000
dvd_percent = dvd_number/1000
music_percent = music_number/1000


import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go


langs = ['Books', 'Videogames', 'DVD', 'Music']
val = [books_percent, videogames_percent, dvd_percent, music_percent]
pie_category = go.Pie(labels = langs, values = val)
data = [pie_category]
fig = go.Figure(data = data)
plot(fig)
fig.write_image("./grafici/pie_category.jpeg")

#Dataset by category and sentiment
top_positive_books = top_books.sort_values(by = ['positive_percent'], ascending=False)[:5]
top_negative_books = top_books.sort_values(by = ['negative_percent'], ascending=False)[:5]
top_positive_videogames = top_videogames.sort_values(by = ['positive_percent'], ascending=False)[:5]
top_negative_videogames = top_videogames.sort_values(by = ['negative_percent'], ascending=False)[:5]
top_positive_dvd = top_dvd.sort_values(by = ['positive_percent'], ascending=False)[:5]
top_negative_dvd = top_dvd.sort_values(by = ['negative_percent'], ascending=False)[:5]
top_positive_music = top_music.sort_values(by = ['positive_percent'], ascending=False)[:5]
top_negative_music = top_music.sort_values(by = ['negative_percent'], ascending=False)[:5]



reviews = pd.read_csv('./data/tokenizedDataset.csv')
reviews_top_positive_books = pd.merge(top_positive_books, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'product_title', 'tokens', 'tokens_stemming', 'sentiment']]
reviews_top_negative_books = pd.merge(top_negative_books, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'product_title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_positive_books = reviews_top_positive_books[reviews_top_positive_books['sentiment'] == 'positive']
reviews_top_negative_books = reviews_top_negative_books[reviews_top_negative_books['sentiment']=='negative']

reviews_top_positive_videogames = pd.merge(top_positive_videogames, reviews[['product','tokens_stemming','tokens','sentiment']], on='product')[['product', 'category', 'product_title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_negative_videogames = pd.merge(top_negative_videogames, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'product_title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_positive_videogames = reviews_top_positive_videogames[reviews_top_positive_videogames['sentiment'] == 'positive']
reviews_top_negative_videogames = reviews_top_negative_videogames[reviews_top_negative_videogames['sentiment']=='negative']

reviews_top_positive_dvd = pd.merge(top_positive_dvd, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'product_title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_negative_dvd = pd.merge(top_negative_dvd, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'product_title', 'tokens', 'tokens_stemming', 'sentiment']]
reviews_top_positive_dvd = reviews_top_positive_dvd[reviews_top_positive_dvd['sentiment'] == 'positive']
reviews_top_negative_dvd = reviews_top_negative_dvd[reviews_top_negative_dvd['sentiment']=='negative']


reviews_top_positive_music = pd.merge(top_positive_music, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'product_title', 'tokens', 'tokens_stemming', 'sentiment' ]]
reviews_top_negative_music = pd.merge(top_negative_music, reviews[['product','tokens_stemming','tokens', 'sentiment']], on='product')[['product', 'category', 'product_title', 'tokens', 'tokens_stemming', 'sentiment']]
reviews_top_positive_music = reviews_top_positive_music[reviews_top_positive_music['sentiment'] == 'positive']
reviews_top_negative_music = reviews_top_negative_music[reviews_top_negative_music['sentiment']=='negative']


'''Save to csv '''
reviews_top_positive_books.to_csv('./data/top/reviews_top_positive_books.csv')
reviews_top_negative_books.to_csv('./data/top/reviews_top_negative_books.csv')

reviews_top_positive_videogames.to_csv('./data/top/reviews_top_positive_videogames.csv')
reviews_top_negative_videogames.to_csv('./data/top/reviews_top_negative_videogames.csv')

reviews_top_positive_dvd.to_csv('./data/top/reviews_top_positive_dvd.csv')
reviews_top_negative_dvd.to_csv('./data/top/reviews_top_negative_dvd.csv')

reviews_top_positive_music.to_csv('./data/top/reviews_top_positive_music.csv')
reviews_top_negative_music.to_csv('./data/top/reviews_top_negative_music.csv')


