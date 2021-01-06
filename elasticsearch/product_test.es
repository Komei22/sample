// 登録されてるインデックスの確認
GET /_cat/indices?v

// product_developmentの情報を確認
GET /products_development

GET /products_development/synonym/1?pretty

// products_developmentに対して検索のクエリを投げる。クエリの内容を書かないと、SELECT * FROM products_developmentされる。
GET /products_development/_search

GET /products_development/_search
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "product_name": "ヘアピン"
                    }
                }
            ]
        }
    }
}

// 検索のクエリ例
GET /products_development/_search
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "product_name": "ヘアピン"
                    }
                }
            ]
        }
    }
}

// 条件を色々指定したクエリ
GET /products_development/_search
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "product_name": "ヘアピン"
                    }
                }
            ],
            "should": [
                {
                    "match": {
                        "description": "シルバー"
                    }
                }
            ],
            "filter": {
                "range": {
                    "stock_num": {
                        "gte": 0
                    }
                }
            }
        }
    }
}

GET /products_development/_search
{
    "query": {
        "function_score": {
            "query": {
                "bool": {
                    "should": [
                        {
                            "match": {
                                "description": {
                                    "query": "シルバー",
                                    "boost": 2
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
}

GET /products_development/_search
{
    "query": {
        "function_score": {
            "query": {
                "bool": {
                    "should": [
                        {
                            "match": {
                                "description": {
                                    "query": "シルバー",
                                    "boost": 2
                                }
                            }
                        },
                        {
                            "match": {
                                "product_name":{
                                    "query": "ヘアピン",
                                    "boost": 1
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
}

GET /products_development/_search
{
    "query": {
        "function_score": {
            "query": {
                "bool": {
                    "should": [
                        {
                            "match": {
                                "description": "シルバー"
                            }
                        },
                        {
                            "match": {
                                "product_name": "ヘアピン"
                            }
                        }
                    ]
                }
            },
            "functions": [
                {
                    "field_value_factor": {  // 指定したfieldをscoreに反映する
                        "field": "price"
                    }
                },
                {
                    "linear": {  // Decay functions：目的の値との近さをscoreに反映する
                        "displayed_at": {  // displayed_atをscoreに反映する
                            "origin": "2019-11-27",  // 基準となる日時
                            "scale": "7d",  // 7dかけて減衰率"decay"分scoreを減衰させる
                            "offset": "0d"  // 基準値と同じとみなす値の範囲
                        }
                    }
                }
            ],
            "score_mode": "multiply",  // functionsで定義した関数のscore（function score）を計算する方法。sum, avgなどもある
            "boost_mode": "multiply",  // クエリで計算されたスコア（query score）とfunction scoreを合算計算する方法
            "max_boost": 10  // functionsで定義した関数のscoreの最大値。最終的なscoreの最大値ではない。
        }
    }
}
