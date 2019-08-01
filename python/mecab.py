import MeCab

mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = '今日はとんこつラーメンが食べたい気分だな。でも味噌ラーメンもいいなあ'
mecab.parse('')
node = mecab.parseToNode(text)
while node:
	word = node.surface
	pos = node.feature.split(",")[1]
	print('{0} , {1}'.format(word, pos))
	node = node.next
