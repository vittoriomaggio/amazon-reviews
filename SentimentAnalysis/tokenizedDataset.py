import pandas as pd

products = pd.read_csv(r'./products_clean.csv')
reviews = pd.read_csv(r'./reviews_clean.csv')

cat_idProd = pd.DataFrame()
cat_idProd["category"] = list(products.category)
cat_idProd["product"] = list(products._id)

result = pd.DataFrame()
result = pd.merge(cat_idProd,reviews)

to_drop = []

i=0
while i < 1478315:
    cat = result['category'][i]
    if not(cat == 'videogames' or cat == 'books'  or cat == 'music' or cat == 'dvd' ):
        to_drop.append(i)       
    i = i+1
      
dataset = result.drop(to_drop)

sentiment = []
for r in dataset_ent['rating']:
    if r < 3:
        sentiment.append('negative')
    if r == 3:
        sentiment.append('neutral')
    if r > 3:
        sentiment.append('positive')

dataset_ent['sentiment'] = sentiment

dataset_ent_sent =  pd.read_csv('./reviews_sentiment.csv')


tokenized = pd.read_csv('./tokenizedDataset.csv')
tokenized['category'] = dataset_ent_sent['category']
tokenized['product'] = dataset_ent_sent['product']
tokenized['sentiment'] = dataset_ent_sent['sentiment']

product_title = pd.DataFrame ()
product_title['product'] = products['_id']
product_title['title'] = products['title']

result = pd.merge(product_title, tokenized)

result.set_index('Index', inplace=True)
result= result.loc[:, ~result.columns.str.contains('^Unnamed')]

result.to_csv('./tokenizedDataset.csv')