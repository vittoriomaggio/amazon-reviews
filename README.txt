README

#Matricole:
Martina Ceccon 
Chantal Costantino 860621
Vittorio Maggio			


#Fasi del progetto
	1)tokenized_stemming = facciamo tokenizzazione e stemming
	2)category_sentiment  = calcoliamo il sentiment e lo salviamo in una nuova colonna
	3)sentiment_distribution = calcoliamo la distribuzione in percentuale del sentiment
	4)reduce_dataset = era top_popular, dividiamo per il sentiment
	5)wordcloud_print = stampa parole più usate per le positive, le negative e le neutre per ogni categoria eccetto music
	6)priceVSrating = valutazioni legate al prezzo e alle recensioni
	7)sentiment_supervised = modelli supervisionato


#Ordine creazione dei dataset
	1)reviews_clean = dataset ridotto di righe
	2)reviews_sentiment = dataset ridotto solo con le categorie interessate
	3)tokenizedDataset = dataset con lo stemming
	4)top = cartella contenente i dataset dei produtti top
	4)sentiment_distribution = dataset in cui è salvata la distribuzione in percentuale