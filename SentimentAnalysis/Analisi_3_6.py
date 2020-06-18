import pandas as pd


df = pd.read_csv('./tokenizedDataset.csv')
       
import datetime as dt

year = []
month = []
for d in df['date']:
    date_time_obj = dt.datetime.strptime(d, '%Y-%m-%d')
    year.append(date_time_obj.year)
    month.append(date_time_obj.month)

df['year'] = year
df['month']  = month


videogames = df[df['category'] == 'videogames']
books = df[df['category'] == 'books']
music = df[df['category'] == 'music']
dvd = df[df['category'] == 'dvd']



import plotly.express as px
from plotly.offline import plot

'''
Distribuzione percentuale del sentiment
'''
#Videogiochi
fig = px.histogram(videogames, x="sentiment" , histnorm='percent')
fig.update_layout(
    title="Videogiochi",
    yaxis_title="Percentuale"
    )
plot(fig)
fig.write_image("./sent_dist_videoogiochi.jpeg")


#Libri
fig = px.histogram(books, x="sentiment" , histnorm='percent')
fig.update_layout(
    title="Libri",
    yaxis_title="Percentuale"
    )
plot(fig)
fig.write_image("./sent_dist_libri.jpeg")

#DVD
fig = px.histogram(dvd, x="sentiment" , histnorm='percent')
fig.update_layout(
    title="DVD",
    yaxis_title="Percentuale"
    )
plot(fig)
fig.write_image("./sent_dist_dvd.jpeg")

#Music
fig = px.histogram(music, x="sentiment" , histnorm='percent')
fig.update_layout(
    title="Music",
    yaxis_title="Percentuale"
    )
plot(fig)
fig.write_image("./sent_dist_music.jpeg")

def sentiment_year(df):
    dist_df = pd.DataFrame()
    years = set(df['year'])
    for y in years:
        ydf = df[df['year'] == y]
        dist_df[y] = ydf.groupby("sentiment")['sentiment'].count()/len(ydf)
    df_years = list(dist_df)
    df_years.sort()
    dist_df = dist_df.reindex(columns=df_years)    
    
    result = pd.DataFrame()
    result['year'] = list(dist_df)
    result['positive'] = list(dist_df.loc['positive'])
    result['neutral'] = list(dist_df.loc['neutral'])
    result['negative'] = list(dist_df.loc['negative'])
    
    return result.fillna(0)
        
videogames_year = sentiment_year(videogames)
fig = px.line(videogames_year, x='year', y = ['positive','neutral','negative'], title='Videogames Sentiment Distribution')
plot(fig)
fig.write_image("./videogiochi_year_sentiment.jpeg")

books_year = sentiment_year(books)
fig = px.line(books_year, x='year', y = ['positive','neutral','negative'], title='Books Sentiment Distribution')
plot(fig)
fig.write_image("./books_year_sentiment.jpeg")

dvd_year = sentiment_year(dvd)
fig = px.line(dvd_year, x='year', y = ['positive','neutral','negative'], title='DVD Sentiment Distribution')
plot(fig)
fig.write_image("./dvd_year_sentiment.jpeg")

music_year = sentiment_year(music)
fig = px.line(music_year, x='year', y = ['positive','neutral','negative'], title='Music Sentiment Distribution')
plot(fig)
fig.write_image("./music_year_sentiment.jpeg")


total = sentiment_year(df)
fig = px.line(total, x='year', y = ['positive','neutral','negative'], title='Sentiment Distribution')
plot(fig)
fig.write_image("./total_year_sentiment.jpeg")