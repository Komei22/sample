import re


text = "これは僕のサイトのurlです。https://komei22.github.io/"

pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
result = re.sub(pattern, "", text)

print('元のテキスト:\n', text)
print('URLを削除したテキスト:\n', result)
