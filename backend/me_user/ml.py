from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/Users/jinglin/Desktop/fff2-ios-fdb76656592f.json')
client = language.LanguageServiceClient(credentials=credentials)

def token_words(text):
	document = types.Document(
		content=text,
		type=enums.Document.Type.PLAIN_TEXT)

	tokens = client.analyze_syntax(document).tokens
	return [token.text.content for token in tokens]

def fetch_docs(user_description_text, posts):
	return [TaggedDocument(words=token_words(user_description_text), tags=['duser'])] + \
		   [TaggedDocument(words=token_words(post.title), tags=['d{}'.format(i)]) for (i, post) in enumerate(posts)]

def order_docs(user_description_text, posts):
	docs = fetch_docs(user_description_text, posts)

	model = Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
	model.build_vocab(docs)
	model.train(docs, total_examples=len(posts), epochs=10)

	ranked_documents = [
		(model.docvecs.similarity('duser', 'd{}'.format(i)), posts[i].get_json()) for i in range(len(posts))
	]

	ordered_documents = sorted(ranked_documents, key=lambda rank_document: rank_document[0], reverse=True)
	return [ordered_document[1] for ordered_document in ordered_documents]
