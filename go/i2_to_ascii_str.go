package main

import (
	"fmt"
	"strconv"
)

func main() {
	binary_str := []string{
		"01001101", "01100001", "01110010", "01100011", "01101000", "00100000", "00110101", "00100000", "00110010", "00110000", "00110001", "00111000",
	}

	for _, bs := range binary_str {
		b, _ := strconv.ParseInt(bs, 2, 0)
		fmt.Printf("%s", string(b))
	}
}
