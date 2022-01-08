package main

func main () {
	var number int = 600851475143
	workingNumber := number
	var largestPrimeFactor int

	for factor := 2; factor^2 < workingNumber; {
		if (workingNumber % factor == 0) {
			workingNumber = workingNumber / factor
			largestPrimeFactor = factor
		} else {
			factor++
		}
	}
	if workingNumber > largestPrimeFactor {
		largestPrimeFactor = workingNumber
	}

	print(largestPrimeFactor)
}