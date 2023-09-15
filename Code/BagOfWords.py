import numpy as np
import pandas as pd

responses = [
    "people watch Tanmay",
    "Tanmay watch Tanmay",
    "People write comment",
    "Tanmay write comment"
]

df = pd.DataFrame({'text':responses, 'output':[1,1,0,0]})

print(df)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()

bow = cv.fit_transform(df['text'])

print(cv.vocabulary_)

print(bow[0].toarray())
print(bow[1].toarray())

print(cv.transform(["Tanmay watch Tanmay and write comment"]).toarray())

