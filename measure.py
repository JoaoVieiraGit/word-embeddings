import gensim

model = gensim.models.Word2Vec.load('mymodel')

f = open("news_en.txt")

sentences = f.readlines()

count = 0
accuracy = 1.00

next_words = []
result = []

line_count = 0

for s in sentences:
	line_count = line_count + 1
	if line_count > 10:
		break

	tokens = s.split()

	for t in tokens:
		if (next_words is not None):
			for r in next_words:
				if t == r[0]:
					accuracy*=r[1]
					print(accuracy)
					break

		count+=1

		result.append(t)

		next_words = model.predict_output_word(result, topn = 10)

		

print((1/accuracy) ** (1. / count))