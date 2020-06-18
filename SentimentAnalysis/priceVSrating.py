import pandas as pd
from plotly.offline import plot

#Import datasets
products_clean = pd.read_csv(r'./Documents/università/DataAnalytics/amazon_review/Data/products_clean.csv') 


to_drop = []

i=0
while i < 20459:
    cat = products_clean['category'][i]
    if not(cat == 'videogames' or cat == 'books'  or cat == 'music' or cat == 'dvd' ):
        to_drop.append(i)       
    i = i+1

products_clean = products_clean.drop(to_drop)

sentiment = []

for r in products_clean['avg_rating']:
    if r < 3:
        sentiment.append('negative')
    else:
        if r == 3:
            sentiment.append('neutral')
        else:
            if r > 3:
                sentiment.append('positive')
            else:
                sentiment.append('no value')

products_clean['sentiment'] = sentiment
    
## BOOKS ##
products_books = products_clean
products_books = products_books[products_books['category'] == 'books']
products_books_pos = products_books[products_books['sentiment'] == 'positive']
products_books_neg = products_books[products_books['sentiment'] == 'negative']

## DVD ##
products_dvd = products_clean
products_dvd = products_dvd[products_dvd['category'] == 'dvd']
products_dvd_pos = products_dvd[products_dvd['sentiment'] == 'positive']
products_dvd_neg = products_dvd[products_dvd['sentiment'] == 'negative']

## VIDEOGAMES ##
products_videogames = products_clean
products_videogames = products_videogames[products_videogames['category'] == 'videogames']
products_videogames_pos = products_videogames[products_videogames['sentiment'] == 'positive']
products_videogames_neg = products_videogames[products_videogames['sentiment'] == 'negative']

## MUSIC ##
products_music = products_clean
products_music = products_music[products_music['category'] == 'music']
products_music_pos = products_music[products_music['sentiment'] == 'positive']
products_music_neg = products_music[products_music['sentiment'] == 'negative']

## INTERVALLI ##

def int_df1(df, df_list):
    df_list.append(df['price'][df['price'] < 15].count())
    df_list.append(df['price'][(df['price'] >= 15) & (df['price'] < 30)].count())
    df_list.append(df['price'][(df['price'] >=30) & (df['price'] < 45)].count())
    df_list.append(df['price'][(df['price'] >= 45) & (df['price'] < 100)].count())
    df_list.append(df['price'][(df['price'] >= 100) & (df['price'] < 150)].count())


def int_df2(df, df_list):
    df_list.append(df['price'][df['price'] < 30].count())
    df_list.append(df['price'][(df['price'] >= 30) & (df['price'] < 50)].count())
    df_list.append(df['price'][(df['price'] >= 50) & (df['price'] < 100)].count())
    df_list.append(df['price'][(df['price'] >= 100) & (df['price'] < 300)].count())
    df_list.append(df['price'][(df['price'] >= 300) & (df['price'] < 500)].count())

# Books #  
books_list_pos = []
int_df1(products_books_pos, books_list_pos)
books_list_pos = [(x/sum(books_list_pos)).round(3) for x in books_list_pos]

books_list_neg = []
int_df1(products_books_neg, books_list_neg)
books_list_neg = [(x/sum(books_list_neg)).round(3) for x in books_list_neg]

# Dvd #
dvd_list_pos = []
int_df1(products_dvd_pos, dvd_list_pos)
dvd_list_pos = [(x/sum(dvd_list_pos)).round(3) for x in dvd_list_pos]

dvd_list_neg = []
int_df1(products_dvd_neg, dvd_list_neg)
dvd_list_neg = [(x/sum(dvd_list_neg)).round(3) for x in dvd_list_neg]

# Videogames #
videogames_list_pos = []
int_df2(products_videogames_pos, videogames_list_pos)
videogames_list_pos = [(x/sum(videogames_list_pos)).round(3) for x in videogames_list_pos]

videogames_list_neg = []
int_df2(products_videogames_neg, videogames_list_neg)
videogames_list_neg = [(x/sum(videogames_list_neg)).round(3) for x in videogames_list_neg]

# Music #
music_list_pos = []
int_df2(products_music_pos, music_list_pos)
music_list_pos = [(x/sum(music_list_pos)).round(3) for x in music_list_pos]

music_list_neg = []
int_df2(products_music_neg, music_list_neg)
music_list_neg = [(x/sum(music_list_neg)).round(3) for x in music_list_neg]


## BOOKS ##
import plotly.graph_objects as go
intervals=['[0-15]', '[15-30]', '[30-45]', '[45-100]', '[100-150]']

fig = go.Figure(data=[
    go.Bar(name='Positive', x=intervals, y=books_list_pos, marker_color = 'goldenrod'),
    go.Bar(name='Negative', x=intervals, y=books_list_neg, marker_color = 'darkblue')
])


fig.update_layout(
    title='Price vs Rating - Book',
    xaxis=dict(
        title='Rating',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='Price',
        titlefont_size=16,
        tickfont_size=14,
    ),
    barmode='group'
)

plot(fig)

## DVD ##
import plotly.graph_objects as go
intervals=['[0-15]', '[15-30]', '[30-45]', '[45-100]', '[100-150]']

fig2 = go.Figure(data=[
    go.Bar(name='Positive', x=intervals, y=dvd_list_pos, marker_color = 'goldenrod'),
    go.Bar(name='Negative', x=intervals, y=dvd_list_neg, marker_color = 'darkblue')
])

fig2.update_layout(
    title='Price vs Rating - DVD',
    xaxis=dict(
        title='Rating',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='Price',
        titlefont_size=16,
        tickfont_size=14,
    ),
    barmode='group'
)

plot(fig2)

## VIDEOGAMES ##
import plotly.graph_objects as go
intervals=['[0-30]', '[30-50]', '[50-100]', '[100-300]', '[300-500]']

fig3 = go.Figure(data=[
    go.Bar(name='Positive', x=intervals, y=videogames_list_pos, marker_color = 'goldenrod'),
    go.Bar(name='Negative', x=intervals, y=videogames_list_neg, marker_color = 'darkblue')
])

fig3.update_layout(
    title='Price vs Rating - Videogames',
    xaxis=dict(
        title='Rating',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='Price',
        titlefont_size=16,
        tickfont_size=14,
    ),
    barmode='group'
)

plot(fig3)

## MUSIC ##
import plotly.graph_objects as go
intervals=['[0-30]', '[30-50]', '[50-100]', '[100-300]', '[300-500]']

fig4 = go.Figure(data=[
    go.Bar(name='Positive', x=intervals, y=music_list_pos, marker_color = 'goldenrod'),
    go.Bar(name='Negative', x=intervals, y=music_list_neg, marker_color = 'darkblue')
])

fig4.update_layout(
    title='Price vs Rating - Music',
    xaxis=dict(
        title='Rating',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='Price',
        titlefont_size=16,
        tickfont_size=14,
    ),
    barmode='group'
)

plot(fig4)


fig.write_image("./fig.jpeg")
fig2.write_image("./fig2.jpeg")
fig3.write_image("./fig3.jpeg")
fig4.write_image("./fig4.jpeg")








           