from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from google.cloud import language

def token_words(text):
    client = language.Client()
    document = client.document_from_text(text)
    annotations = document.annotate_text()
    words = []
    for token in annotations.tokens:
        words.append(token.text_content)
    return words

def fetch_docs(posts):
	return [TaggedDocument(words=token_words(post.title), tags=['d{}'.format(i)]) for (i, post) in enumerate(posts)]

def order_docs(posts):
	docs = fetch_docs(posts)

	model = Doc2Vec(documents=docs, min_count=1, dm=0)	


print(model.docvecs['d1'])

print(model.docvecs.most_similar('d1'))
print(model.docvecs.most_similar('d2'))
print(model.docvecs.most_similar('d3'))
print(model.docvecs.most_similar('d4'))
