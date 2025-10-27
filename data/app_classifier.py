from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
sentence = ['Gucci and Lui Vuitton sucks', 'Nike, puma and adidas are kings']
embedings = model.encode(sentence)
print(embedings)