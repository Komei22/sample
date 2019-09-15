package main

import "fmt"

// fibonacci()はクロージャ、func()で関数が呼ばれたときの処理を書く
func fibonacci() func() int {
	// クロージャ内で保持される変数
	f, g := 0, 1
	// クロージャが呼ばれたときに実行される処理（変数f, gの値は呼ばれるたびに初期化されず、値は保持される）
	return func() int {
		f, g = g, f+g
		return f
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(i, f())
	}
}
