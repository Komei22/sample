package main

import (
	"fmt"
	"github.com/knocknote/vitess-sqlparser/sqlparser"
)

func main() {
	stmt, err := sqlparser.Parse("select * from user_items where user_id=1 order by created_at limit 3 offset 10")
	if err != nil {
		panic(err)
	}

	fmt.Println(stmt.(*sqlparser.Select).From[0].(*sqlparser.AliasedTableExpr).Expr.(sqlparser.TableName).Name.String())
	fmt.Println(sqlparser.String(stmt.(*sqlparser.Select).From))

	// インターフェースを経由し過ぎていて，テーブル名を取り出すだけでかなり長い呼び出しを行わないといけない
	// 厳しいなという感想
	// 別のやつも探してみよう

}
