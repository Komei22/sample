package main

import (
	"fmt"
	"github.com/lfittl/pg_query_go"
	"regexp"
)

func main() {
	query := `select * from "user_items" where user_id=1 order by created_at limit 3 offset 10`
	tree, err := pg_query.Parse(query)
	if err != nil {
		panic(err)
	}

	fmt.Printf("%+v\n", tree)

	normalizedQuery, err := pg_query.Normalize(query)
	if err != nil {
		panic(err)
	}

	rep := regexp.MustCompile(`\$[0-9]*`)
	maskedQuery := rep.ReplaceAllString(normalizedQuery, `?`)

	fmt.Printf("%+v", maskedQuery)
}
