
import nltk
import re

# Download required NLTK datasets
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def process_review(review):

    # convert lowercase form
    review_lower = review.lower()

    # remove punctuations and numbers
    review_pun_num = re.sub(r"[^a-z\s]", "", review_lower)

    # tokenize
    review_tokens = word_tokenize(review_pun_num)

    # remove stop words
    stop_words = stopwords.words('english')
    review_tokens_stopwords = [
        token for token in review_tokens
        if token not in stop_words
    ]

    # lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_token = [
        lemmatizer.lemmatize(token, pos='n')
        for token in review_tokens_stopwords
    ]

    # join tokens
    return " ".join(lemmatized_token)


if __name__ == "__main__":
    review = "The product was really nice!!"
    print(process_review(review))
