package main

import (
	"fmt"
	"github.com/Komei22/sql-mask"
)

func main() {
	// query := "SELECT * FROM `user` WHERE `id` = 1"

	// m := &masker.MysqlMasker{}
	// queryDigest, err := masker.Mask(m, query)
	// if err != nil {
	// 	panic(err)
	// }

	// fmt.Println(queryDigest)

	query := `SELECT * FROM "user" WHERE "id" = 1`

	m := &masker.PgMasker{}
	queryDigest, err := masker.Mask(m, query)
	if err != nil {
		panic(err)
	}

	fmt.Println(queryDigest)
}
