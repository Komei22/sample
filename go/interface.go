package main

type Statement interface {
	iStatement()
}

func (*Select) iStatement() {}
func (*Insert) iStatement() {}

type Select struct {
	str string
}

type Insert struct {
	str string
}

func main() {
	var stmt Statement
	stmt.iStatement()
}
