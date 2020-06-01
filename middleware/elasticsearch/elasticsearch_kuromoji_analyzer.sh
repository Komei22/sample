# kuromoji用のanalyzerを作成する
curl -X PUT "localhost:9200/my_ja_map?pretty" -H 'Content-Type: application/json' -d'
{
    "settings": {
        "analysis": {
            "analyzer": {
                "my_ja_analyzer": {
                    "type": "custom",
                    "tokenizer": "kuromoji_tokenizer",
                    "mode": "normal",
                    "char_filter": [
                        "kuromoji_iteration_mark"
                    ],
                    "filter": [
                        "kuromoji_baseform",
                        "kuromoji_part_of_speech",
                        "ja_stop",
                        "kuromoji_number",
                        "kuromoji_stemmer",
                        "my_posfilter"
                    ]
                }
            },
            "filter": {
                "my_posfilter": {
                    "type": "kuromoji_part_of_speech",
                    "stoptags": [
                        "助詞-格助詞-一般",
                        "助詞-終助詞"
                    ]
                }
            }
        }
    }
}
'
