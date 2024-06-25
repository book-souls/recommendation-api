import fasttext
import nltk
import nltk.corpus
import string

nltk.download("punkt", raise_on_error=True, quiet=True)
nltk.download("stopwords", raise_on_error=True, quiet=True)

model = fasttext.load_model("model.bin")
detokenizer = nltk.TreebankWordDetokenizer()
stopwords = set(nltk.corpus.stopwords.words("english"))
punctuation_remover = str.maketrans("", "", string.punctuation)

def preprocess(text: str) -> str:
    text = text.lower()
    text = text.translate(punctuation_remover)
    words = nltk.word_tokenize(text)
    words = [word for word in words if word not in stopwords]
    return detokenizer.detokenize(words)

def get_sentence_vector(text: str) -> list:
    text = preprocess(text)
    return model.get_sentence_vector(text).tolist()
