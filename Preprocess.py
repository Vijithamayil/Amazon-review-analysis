import re
import nltk

nltk.download('stopwords')  # Stop Words in English
nltk.download('wordnet')    # Vocabulary for lemmatization
nltk.download('vader_lexicon') # Lexicon for Vader Model 
nltk.download('punkt') # Tokenizer Rules
nltk.download('punkt_tab')

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer

from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
lemmatizer= WordNetLemmatizer()


def preprocess(review):
    # Convert review into lowercase
    review_lower = review.lower()

    # Remove punctuations , numbers and other characters 
    reviews = re.sub (r'[^a-z\s]','',review_lower)

    # Split review into tokens
    tokens = word_tokenize(reviews)

    # Renove stop words
    tokens_without_stopwords = [token for token in tokens if token not in stop_words]
                                   
    # Lemmatize tobens
    lemmatize_tokens =[lemmatizer.lemmatize(token, pos='a') for token in tokens_without_stopwords]
 
    return " ".join(lemmatize_tokens)

if __name__ == "__main__":
    print(preprocess("Nice product and very USEFUL!!"))