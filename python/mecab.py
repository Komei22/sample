import MeCab
import sys

mecab = MeCab.Tagger('-d/usr/local/lib/mecab/dic/mecab-ipadic-neologd -u/usr/local/lib/mecab/dic/userdic/user.dic')
# mecab = MeCab.Tagger('-Owakati -u/Users/komei.nomura/mecab-dic/user.dic')

args = sys.argv
text = args[1]

node = mecab.parseToNode(text)
while node:
    word = node.surface
    pos = node.feature.split(",")[1]
    print(word, node.feature)
    node = node.next
