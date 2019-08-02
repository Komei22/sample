import MeCab
import codecs
import os

def wakati(doc):
	tagger = MeCab.Tagger('-Owakati')

	doc_nodes = tagger.parseToNode(doc)

	keywords = []
	while doc_nodes:
		if doc_nodes.feature.split(",")[0] == "名詞":
			keywords.append(doc_nodes.surface)
		doc_nodes = doc_nodes.next

	return keywords


def read(file):
	with codecs.open("txt/" + file, "r", "utf-8") as reader:
		lines = reader.read().splitlines()
		doc = "".join(lines)
	return doc


def write(keywords, file):
	if not os.path.exists('wakati'):
		os.mkdir('wakati')

	with open('wakati/' + file, 'wt') as writer:
		writer.write(" ".join(keywords))


# main
for file in os.listdir('txt'):
	doc = read(file)
	keywords = wakati(doc)
	write(keywords, file)



