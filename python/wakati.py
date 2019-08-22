import MeCab
import os
import argparse

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
	with open(file, 'r') as reader:
		lines = reader.read().splitlines()
		doc = "".join(lines)
	return doc


def write(keywords, file):
	if not os.path.exists('wakati'):
		os.mkdir('wakati')
	with open('wakati/' + file, 'wt') as writer:
		writer.write(" ".join(keywords))

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--data_dir', required=True)
	return parser.parse_args()

if __name__ == '__main__':
	args = parse_args()
	dir = args.data_dir
	for file in os.listdir(dir):
		doc = read(dir + '/' + file)
		keywords = wakati(doc)
		write(keywords, file)



