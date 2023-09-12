1)lowercasing 

```
bad_str.lower()
```

2) remove html tags

```
import re

def striphtml(data):
  p = re.compile(r'<.?>')
  return p.sub('', data)
```

3) remove urls
- similar regex

4) remove punctuation
```
import string

exclude=string.punctuation

for char in exclude: 
  text=text.replace(char, '')

return text
```

or

```
return text.translate(str.maketrans('', '', exclude))
```

5)chat word treatment

github.com/rishabhverma17/sms_slang_translator

6) spelling correction

```
from textblob import TextBlob

textBlb = TextBlob(incorrect_text)
textBlb.correct()
```

7) removing stop words

```
from nltk.corpus import stopwords

exclude = stopwords.words('english')
```

8) remove emoji - use regex

```
import emoji

print(emoji.demojize('python is 💋'))
```

9) tokenization

```
from nltk.tokenize import word_tokenize, sent_tokenize

word_tokenize(sentence)
sent_tokenize(sentence)
```

```
import spacy

nlp = spacy.load('en_core_web_sm')

doc1=nlp(sentence)
```

10) stemming

```
from nltk.stem.porter import PorterStemmer

ps= PorterStemmer()

def stem_words(text):
   return " ".join([ps.stem(word) for word in text.split()])
```

lemmatization - root word is always a valid word

```
import nltk
from nltk.stem import WordNetLemmatizer

lemma = WordNetLemmatizer()

def lemmatize(text):
  exclude = string.punctuation
  words= nltk.word_tokenize(text)

  for token in text: 
    if token in exclude:
       text.remove(token)
  
  for word in words:
    print("{0:20}{1:20}".format(word, lemma.lemmatize(word, pos='v)))
```