from appJar import gui
import gensim
from langdetect import detect

#Carrega ambos os modelos para a memoria
#model = gensim.models.KeyedVectors.load_word2vec_format('model_trained_en.bin', binary = 1)
#model_pt = gensim.models.KeyedVectors.load_word2vec_format('model_trained_pt.txt')

model_pt = gensim.models.Word2Vec.load('mymodel_pt')
model = gensim.models.Word2Vec.load('mymodel')


text = []
result = []
related = []
similaritytuple = ()


#Processo chamado a cada segundo durante execucao
def testEvent():

	similarity = []

	#Pre-processamento do texto
	text = app.getTextArea("t1").split()

	

	if len(text) == 0:

		#Se nao houver texto, deixar caixas vazias
		app.updateListBox("list", [])
		app.updateListBox("relatedwords", [])
		app.updateListBox("similarityranking", [])
		app.updateListBox("worstfit", [])

	if len(text) == 1:
		#Detetar linguagem
		lang = detect(app.getTextArea("t1"))
	
	if len(text) > 1:
		lang = detect(app.getTextArea("t1"))

		try:
			if lang == "pt":
				print("PT")
				#Preencher variaveis com os valores adequados
				result = model_pt.predict_output_word(text, topn = 5)

				related = model_pt.most_similar(positive = text[:-1], topn=5)

				if len(text) > 2:
					tempstring1 = text[-2]
					tempstring2 = text[-3]
					similarity = [model_pt.similarity(tempstring1, tempstring2)]

				worst = [model_pt.doesnt_match(text)]
			else:
				print("EN")
				result = model.predict_output_word(text, topn = 5)

				related = model.most_similar(positive = text[:-1], topn=5)

				if len(text) > 2:
					tempstring1 = text[-2]
					tempstring2 = text[-3]
					similarity = [model.similarity(tempstring1, tempstring2)]

				worst = [model.doesnt_match(text)]

			#Pos-processamento
			divide = []

			if result is not None:
				for r in result:
					divide.append(r[0])

			divide2 = []

			if related is not None:
				for rel in related:
					divide2.append(rel[0])

			#Colocar variaveis nas caixas
			app.updateListBox("list", divide)
			app.updateListBox("relatedwords", divide2)
			app.updateListBox("similarityranking", similarity)
			app.updateListBox("worstfit", worst)
		except KeyError:
			#Caso o modelo nao reconheca a palavra.
			print("Word Not Found.")


app = gui()

#Labels e caixas de texto
app.addLabel("Word Predictor", "Word Predictor")

app.addLabel("Text", "Text",0, 0)

app.addTextArea("t1",1,0)

app.addLabel("Suggestions", "Suggestions",0,1)

app.addListBox("list",[],1,1)

app.addLabel("Related Words", "Related Words",0,2)

app.addListBox("relatedwords",[],1,2)

app.addLabel("Similarity Ranking", "Similarity Ranking",0,3)

app.addListBox("similarityranking",[],1,3)

app.addLabel("Worst Fit", "Worst Fitting Word",0,4)

app.addListBox("worstfit",[],1,4)

#Inicializar processo
app.registerEvent(testEvent)

#Inicializar GUI
app.go()