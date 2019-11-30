#Este ficheiro treina os modelos de Word Embeddings. Não serve para os testar.


import gensim

sentences = []
text = []
result = []

print("Opening dataset.")

f = open('news_en.txt')
sentences = f.readlines()

print("Initializing reading of dataset.")

for s in sentences:
	result.append(s.split())

print("Initializing model training. This could take over an hour.")
model = gensim.models.Word2Vec(result, min_count=10, workers = 4, sample = 0, max_vocab_size = 40000000)

print("Saving model to disk.")

model.save('newmodel')