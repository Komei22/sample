# coding: utf-8
import re

# ハイフンの種類は3種類j
text = "-----------aaaaaーーーーーーーーーーーーbbbbb-cccc－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－"

pattern = "\-{2,}|ー{2,}|－{2,}"
# pattern = "ー+|\-+"
result = re.sub(pattern, "", text)

print('元のテキスト:\n', text)
print('罫線を削除したテキスト:\n', result)
