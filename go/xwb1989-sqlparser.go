package main

import (
	"fmt"
	"github.com/xwb1989/sqlparser"
)

func main() {
	query := "select * from user_items where user_id=1 order by created_at limit 3 offset 10"

	stmt, err := sqlparser.Parse(query)
	if err != nil {
		// エラー処理を書く
	}
	out := sqlparser.String(stmt.(*sqlparser.Select).From)
	fmt.Println(out)

}
