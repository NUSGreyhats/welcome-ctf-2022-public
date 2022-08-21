package src

import (
	"fmt"
	"log"
	"strconv"
)

func Main() {
	var flag string
	fmt.Scanln(&flag)

	if check(flag) {
		log.Println("You won! That's the flag!")
	} else {
		log.Println("That's not it :(")
	}
}

func check(flag string) bool {
	// greyhats{st4t1c_s1nGl3_4ss1Gnm3nt}
	for _, i := range [...]int{9, 16, 24, 25} {
		if flag[i] != 's' {
			return false
		}
	}

	for _, i := range []int{13, 17, 26} {
		if num, err := strconv.Atoi(string(flag[i])); err != nil || num != 1 {
			return false
		}
	}

	return len(flag) == 34 &&
		flag[:9] == "greyhats{" &&
		flag[len(flag)-1] == '}' &&
		flag[15] == flag[22] &&
		flag[22] == '_' &&
		flag[29] == 'm' &&
		flag[10] == flag[12] &&
		flag[12] == flag[32] &&
		flag[32] == 't' &&
		flag[13] == flag[17] &&
		flag[17] == flag[26] &&
		flag[26] == '1' &&
		flag[14] == 'c' &&
		flag[18] == flag[28] &&
		flag[28] == flag[31] &&
		flag[31] == 'n' &&
		flag[19] == flag[27] &&
		flag[27] == 'G' &&
		flag[20] == 'l' &&
		flag[11] == flag[23] &&
		flag[23] == '4' &&
		flag[21] == flag[30] &&
		flag[30] == '3'
}
