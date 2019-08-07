import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

vectorizer = CountVectorizer(input='filename', token_pattern=u'(?u)\\b\\w+\\b')

files = ['wakati/' + path for path in os.listdir('wakati')]

tf_vec = vectorizer.fit_transform(files).toarray()

features = vectorizer.get_feature_names()
# print("words:\n{}".format(vectorizer.get_feature_names()))
# print("tf_vec:\n{}".format(tf_vec))

# word_count = []
# for word, count in zip(vectorizer.get_feature_names()[:], tf_vec.sum(axis=0)[:]):
	# print(word, count)
	# word_count.append((word, count))

# 単語と使用回数の表示(降順)
# print(sorted(word_count, key=lambda k: k[1], reverse=True))

tfidf_transeformer = TfidfTransformer(norm='l2', sublinear_tf=True)

tfidf = tfidf_transeformer.fit_transform(tf_vec)

print(tfidf.shape)

max_feature_idx = tfidf.toarray().argmax()

print(features[max_feature_idx])

print(tfidf.toarray()[:, features.index('ラーメン')])
