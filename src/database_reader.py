import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('../good_reads_final.csv')

remove_genres = {
 'Language',
 'Animals',
 'Autobiography',
 'Did Not Finish',
 'Parenting',
 'Comics',
 'Anthologies',
 'Shapeshifters',
 'Biography',
 'Amish',
 'Philosophy',
 'Design',
 'Music',
 'Gardening',
 'Sequential Art',
 'Lds',
 'Own',
 'How To',
 'Christianity',
 'Plays',
 'Asian Literature',
 'Mental Health',
 'Feminism',
 'Manga',
 'Lgbt',
 'Travel',
 'Mythology',
 'Glbt',
 'Family',
 'Couture',
 'Marriage',
 'Art',
 'Media Tie In',
 'United States',
 'World War II',
 'Writing',
 'European Literature',
 'Inspirational',
 'Eastern Africa',
 'Poetry',
 'Relationships',
 'Childrens',
 'War',
 'Self Help',
 'Religion',
 'Sexuality',
 'Sociology',
 'Cultural',
 'Literature',
 'Education',
 'Holiday',
 'Nonfiction',
 'Science',
 'Esoterica',
 'Sports and Games',
 'Sports',
 'Psychology',
 'Retellings',
 'Business',
 'Humor',
 'Health',
 'Occult',
 'Polyamorous',
 'Food and Drink',
 'Pulp',
 'Medical',
 'Warfare',
 'Northern Africa',
 'Football',
 'Spirituality',
 'Unfinished',
 'Teaching',
 'Social Science',
 'Leadership',
 'Fairy Tales',
 'Reference',
 'Military History',
 'Dungeons and Dragons',
 'Economics',
 'Politics',
 'Magical Realism'}

for rm in remove_genres:
    data = data[~data.genre_1.str.contains(rm)]
    data = data[~data.genre_2.str.contains(rm)]

data['genre_1'] = data['genre_1'].replace({'Fiction':'Uncategorized',
    'Literary Fiction'  : 'Uncategorized',
    'Fan Fiction'       : 'Uncategorized',
    'Novels'            : 'Uncategorized',
    'Novella'           : 'Uncategorized',
    'Young Adult'       : 'Young',
    'Dark'              : 'Horror',
    'Category Romance'  : 'Romance',
    'Adult Fiction'     : 'Adult',
    'Suspense'          : 'Thriller',
    'Spy Thriller'      : 'Thriller',
    'Mystery'           : 'Thriller',
    'Death'             : 'Horror',
    'New Adult'         : 'Young',
    'Paranormal'        : 'Horror',
    'Speculative Fiction':'Thriller',
    'Womens Fiction'    : 'Romance',
    'Christian Fiction' : 'Religious',
    'Biblical Fiction'  : 'Religious',
    'Christian'         : 'Religious',
    'Realistic Fiction' : 'Realistic',
    'History'           : 'Historical',
    'Dark Fantasy'      : 'Fantasy',
    'Love'              : 'Romance'})

drop_list = ['author_genres',
    'birthplace',
    'author_id',
    'author_page_url',
    'author_rating_count',
    'author_review_count',
    'book_fullurl',
    'book_id',
    'genre_2',
    'num_ratings',
    'num_reviews']

data = data.drop(drop_list, axis = 1)

auxiliary_date = []
for date in data['publish_date']:
    aux = str(date)
    aux = aux.split(" ")
    auxiliary_date.append(aux[-1])

data['publish_date'] = auxiliary_date

data.to_csv('../booksDB.csv')
