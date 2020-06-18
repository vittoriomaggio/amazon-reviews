import pandas as pd

df = pd.read_csv('./tokenizedDataset.csv')

positive_count = pd.DataFrame()
positive_count = df[df['sentiment']=='positive']
positive_count= positive_count.groupby('product').count()['reviews_number'].rename("positive").to_frame()
positive_count.reset_index(level=0, inplace=True)

negative_count = pd.DataFrame()
negative_count = df[df['sentiment']=='negative']
negative_count= negative_count.groupby('product').count()['reviews_number'].rename("negative").to_frame()
negative_count.reset_index(level=0, inplace=True)

neutral_count = pd.DataFrame()
neutral_count = df[df['sentiment']=='neutral']
neutral_count= neutral_count.groupby('product').count()['reviews_number'].rename("neutral").to_frame()
neutral_count.reset_index(level=0, inplace=True)

prod_sent = df.groupby('product').count()['reviews_number'].to_frame()
prod_sent.reset_index(level=0, inplace=True)

df = df.drop_duplicates(subset="product")
title_df = pd.DataFrame()
title_df['product'] = df['product']
title_df['title'] = df['title']

prod_sent = prod_sent.merge(title_df, how='left' , on='product')
prod_sent = prod_sent.merge(positive_count, how='left' , on='product')
prod_sent = prod_sent.merge(negative_count, how='left' , on='product')
prod_sent = prod_sent.merge(neutral_count, how='left' , on='product')

i = 0
positive_percent = []
while i<len(prod_sent):
    percent = prod_sent['positive'][i] / prod_sent['reviews_number'][i]
    positive_percent.append(percent)
    i=i+1

i = 0
negative_percent = []
while i<len(prod_sent):
    percent = prod_sent['negative'][i] / prod_sent['reviews_number'][i]
    negative_percent.append(percent)
    i=i+1
   
i = 0
neutral_percent = []
while i<len(prod_sent):
    percent = prod_sent['neutral'][i] / prod_sent['reviews_number'][i]
    neutral_percent.append(percent)
    i=i+1
    
prod_sent['positive_percent'] = positive_percent
prod_sent['negative_percent'] = negative_percent
prod_sent['neutral_percent'] = neutral_percent
prod_sent = prod_sent.fillna(0)

prod_sent.to_csv('./sentiment_distribution.csv')