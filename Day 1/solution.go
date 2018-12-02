package main

import "fmt"
import "bufio"
import "strconv"
import "os"

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func find_duplicate(f *os.File, frequencies map[int]bool, result int) (int, bool) {
	f.Seek(0, 0)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		number, err := strconv.Atoi(scanner.Text())
		check(err)
		result = result + number
		_, ok := frequencies[result]
		if ok {
			return result, true
		} else {
			frequencies[result] = true
		}
	}
	return result, false
}

func part1() int {
  result := 0
  f, err := os.Open("input.txt")
	check(err)
  scanner := bufio.NewScanner(f)
  for scanner.Scan() {
    number, err := strconv.Atoi(scanner.Text())
    check(err)
    result = result + number
  }
  return result
}

func part2() int {
  frequencies := map[int]bool{}
	result := 0
	frequencies[result] = true
	solution_found := false
	f, err := os.Open("input.txt")
	check(err)
	for !solution_found {
		result, solution_found = find_duplicate(f, frequencies, result)
	}
	return result
}


func main() {
  fmt.Println(part1())
  fmt.Println(part2())
}
