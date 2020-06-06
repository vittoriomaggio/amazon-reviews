import pandas as pd

reviews = pd.read_json(r'C:\Users\marti\Dropbox\Magistrale_Informatica\Data_Analytics\PROGETTO\Amazon_Dataset\Data\reviews.json', lines=True)

reviews.to_csv(r'C:\Users\marti\Dropbox\Magistrale_Informatica\Data_Analytics\PROGETTO\Amazon_Dataset\Data\reviews_clean.csv')