Steps to follow to build an end NLP software

1) Data Acquisition
2) Text Preparation
3) Feature Engineering
4) Modelling
5) Deployment


#DataAcquisition :

i) data available 
-> on the table - start working
-> database - data Engineering
-> less data - data augmentation(bigram flip, synonyms, back translate, additional noise) //generate synthetic data

ii) others have the data 
-> web scraping, public dataset, api (Rapid Api), pdf, image, audio
= convert to textual data

iii) nobody has the data 


#TextPreprocessing

i) Cleaning

-html tag cleaning (RegEx)
```
import re

def striphtml(data):
  p = re.compile(r'<.?>')
  return p.sub('', data)
```

-emoji-unicode normalization 
```
emoji_text.encode('utf-8')
```

-spelling check

```
from textblob import TextBlob

textBlb = TextBlob(incorrect_text)
textBlb.correct()
```

ii) Basic preprocessing

-tokenization
-stop word removal
-stemming
-removing digits, punctuations
-lowercasing
-language detection

iii) Advanced preprocessing

-parts of speech tagging
-parsing
-coreference resolution

#FeatureEngineering

-bag of words, tfidf, ohe, wordsvec

if model is an ML model, features have to be created by us and domain knowledge is important, however we can backtrack our results.

if model is a DL model, feature extraction is automatically done by itself, however backtracking is not possible.

#modelling 

modelling - heuristic, ml, dl, composite, cloud api
evaluation - intrinsic, extrinsic
__perplexity__

#deployment

deploy -> monitor -> update









