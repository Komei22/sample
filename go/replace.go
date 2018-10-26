package main

import (
	"fmt"
	"regexp"
)

func main() {
	// str := "SELECT\n*\nFROM\nuser\nWHERE\nid = 1"
	str := "SELECT             * FROM user WHERE id = 1"
	// str2 := strings.Replace(str, "  ", " ", -1)
	multiSpaceRegexp := regexp.MustCompile(" {2,}")
	str2 := multiSpaceRegexp.ReplaceAllString(str, " ")
	fmt.Println(str2)
}
