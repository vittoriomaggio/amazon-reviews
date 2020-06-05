import pandas as pd
reviews= reviews_df[:10000]
users_id = reviews['author-id']
users_id_set = set(users_id)

number_of_review = []

for uid in users_id_set:
    rw_number = 0
    for u in users_id:
        if u == uid:
            rw_number = rw_number + 1
    number_of_review.append(rw_number)
            

users_rev = pd.DataFrame()
users_rev['id'] = list(users_id_set)
users_rev['number_of_reviews'] = number_of_review


