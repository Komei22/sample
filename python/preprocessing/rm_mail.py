# coding: UTF-8
import re

text = "これは僕のメールアドレスです。hogehoge@fuga.com"

pattern = "[\w\-\.]+@[a-zA-Z0-9\-\.]+\.[a-zA-Z]+"
result = re.sub(pattern, "", text)

print('元のテキスト:\n', text)
print('メールアドレスを削除したテキスト:\n', result)
