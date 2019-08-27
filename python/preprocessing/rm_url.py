# coding: UTF-8
import re

# text = "これは僕のサイトのurlです。https://komei22.github.io/"
text = '手のひらサイズのシンプルな財布です。片手で開閉できる、便利ながま口タイプ。お札は二つ折りで、カードは縦でも横でも入ります。小物を入れるポーチとしても、お使い頂けます。約W125×H125×T25mm＜カラー＞○ブルー＜革＞○タンニン鞣しの豚革・がま口財布商品一覧（他のイラスト刻印の商品が、ご覧頂けます）https://minne.com/@atelier-roca?q=%E3%81%8C%E3%81%BE%E5%8F%A3%E8%B2%A1%E5%B8%83&input_method=typing&category_id=&commit=%E6%A4%9C%E7%B4%A2・トラ猫の刻印の商品は、こちらからご覧頂けます。https://minne.com/@atelier-roca?q=%E3%83%88%E3%83%A9%E7%8C%AB&input_method=typing&category_id=&commit=%E6%A4%9C%E7%B4%A2《《カスタムメイドオーダーご希望の方へ》》刻印違い、色違いのみ、オーダー承ります。（サイズ、形の変更は承っておりません。）オーダーで、お取り扱い出来ない革もございますので、必ず「×カートに入れる×」ではなく、「◎質問する◎」ボタンから、メールにてご相談ください。（現在、１～２ヶ月程度の製作時間を頂戴しています。）・刻印一覧ページ　https://minne.com/items/18411591・革の色見本ページ　https://minne.com/items/18409488'

pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-@]+"
result = re.sub(pattern, "", text)

print('元のテキスト:\n', text)
print('URLを削除したテキスト:\n', result)
