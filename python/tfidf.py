import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

vectorizer = CountVectorizer(input='filename', token_pattern=u'(?u)\\b\\w+\\b')

files = ['wakati/' + path for path in os.listdir('wakati')]

# 単語ごとの出現数をカウントする。(sklearnにおいてはこの値がtf)
tf_vec = vectorizer.fit_transform(files).toarray()

features = vectorizer.get_feature_names()
print("features:\n{}".format(features))
print("tf_vec:\n{}".format(tf_vec))

# word_count = []
# for word, count in zip(vectorizer.get_feature_names()[:], tf_vec.sum(axis=0)[:]):
# 	print(word, count)
# 	word_count.append((word, count))

# 単語と使用回数の表示(降順)
# print(sorted(word_count, key=lambda k: k[1], reverse=True))

# tfidfを計算するオブジェクト（ベクトルの正規化はしない、tf_vecをtfの値はそのまま使う）
tfidf_transformer = TfidfTransformer(norm=None, sublinear_tf=False)

idf = tfidf_transformer.fit(tf_vec)

print("idf:\n{}".format(idf.idf_))

# tfidfの計算を実行。``tf=単語の出現回数``、``idf=log((1+全文書数)/(1+単語が出現する文書数))+1``
tfidf = tfidf_transformer.fit_transform(tf_vec)

print("tfidf:\n{}".format(tfidf.toarray()))
# print(tfidf.shape)

# max_feature_idx = tfidf.toarray().argmax()

# print(features[max_feature_idx])

# print(tfidf.toarray()[:, features.index('ラーメン')])
