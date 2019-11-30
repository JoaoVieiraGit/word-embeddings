Para correr a aplicação de Word Embeddings, deve correr o seguinte comando:

python GUI_pt.py

Eventualmente poderá ser necessário instalar as dependências appJar, gensim e langdetect


Se em vez de correr a aplicação quiser treinar um novo modelo, deverá ir a meta2.py, e substituir as 2 seguintes linhas:
f = open('news_en.txt')
model.save('newmodel')

Com o dataset a utilizar e com o número desejado do modelo a criar. Seguidamente, basta apenas correr meta2.py e esperar (poderá demorar mais de 2 horas)


