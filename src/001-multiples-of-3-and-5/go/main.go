package main

import "fmt"

func main() {
	fmt.Print(solution())
}

func solution() int {
	sum := 0
	for n := 3; n < 1001; n++ {
		if (n%3 == 0) || (n%5 == 0) {
			sum += n
		}
	}
	return sum
}
