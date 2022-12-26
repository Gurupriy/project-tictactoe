package main

import (
	"fmt"
	"strings"
)

var tictactoe = map[string]string{
	"a1": "1",
	"a2": "2",
	"a3": "3",
	"b1": "4",
	"b2": "5",
	"b3": "6",
	"c1": "7",
	"c2": "8",
	"c3": "9",
}
var stringArray = [9]string{"a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"}

func validateWin() bool {
	if (tictactoe["a1"] == tictactoe["a2"]) && (tictactoe["a1"] == tictactoe["a3"]) && (tictactoe["a2"] == tictactoe["a3"]) {
		fmt.Println("C1")
		return true
	} else if (tictactoe["b1"] == tictactoe["b2"]) && (tictactoe["b1"] == tictactoe["b3"]) && (tictactoe["b2"] == tictactoe["b3"]) {
		fmt.Println("C2")
		return true
	} else if (tictactoe["c1"] == tictactoe["c2"]) && (tictactoe["c1"] == tictactoe["c3"]) && (tictactoe["c2"] == tictactoe["c3"]) {
		fmt.Println("C3")
		return true
	} else if (tictactoe["a1"] == tictactoe["b1"]) && (tictactoe["a1"] == tictactoe["c1"]) && (tictactoe["b1"] == tictactoe["c1"]) {
		fmt.Println("C4")
		return true
	} else if (tictactoe["a2"] == tictactoe["b2"]) && (tictactoe["a2"] == tictactoe["c2"]) && (tictactoe["b2"] == tictactoe["c2"]) {
		fmt.Println("C5")
		return true
	} else if (tictactoe["a3"] == tictactoe["b3"]) && (tictactoe["a3"] == tictactoe["c3"]) && (tictactoe["b3"] == tictactoe["a3"]) {
		fmt.Println("C6")
		return true
	} else if (tictactoe["a1"] == tictactoe["b2"]) && (tictactoe["a1"] == tictactoe["c3"]) && (tictactoe["b2"] == tictactoe["c3"]) {
		fmt.Println("C7")
		return true
	} else if (tictactoe["a3"] == tictactoe["b2"]) && (tictactoe["a3"] == tictactoe["c1"]) && (tictactoe["b2"] == tictactoe["c1"]) {
		fmt.Println("C8")
		return true
	} else {
		fmt.Println("Not yet there")
		return false
	}
}

func posCheck(pos string) bool {
	found := false
	for _, c := range stringArray {
		if c == pos {
			found = true
		}
	}
	if found {
		return true
	} else {
		return false
	}
}

func main() {

	//var noOfMoves int = 9

	fmt.Println("Welcome to the Tic Tac Toe Game")
	fmt.Println("There are two players in the game. One of the players chooses the 'X' character.The other chooses the 'O' character")
	var user1 string
	var user2 string

	fmt.Print("Enter the username for player one: ")
	fmt.Scan(&user1)
	fmt.Print("Enter the username for player two: ")
	fmt.Scan(&user2)
	fmt.Printf("%v selected 'X' and %v selected 'O'", user1, user2)
	fmt.Println(" The game is based on the blindfold mode. The players point the position on which they want to place the character. The board is 3X3 board displayed below")
	fmt.Print(` 
				A1 | A2 | A3 
				B1 | B2 | B3				
				C1 | C2 | C3	
	`)
	fmt.Println("")
	fmt.Println("Lets start the game")

	for i := 0; i < 9; i++ {
		var posFlag bool = false
		user1Move := ""
		user2Move := ""

		fmt.Printf("%v to play", user1)

		for !posFlag {
			fmt.Scan(&user1Move)
			if posCheck(user1Move) {
				posFlag = true
			} else {
				fmt.Println("Invalid position. Enter the correct position")
			}
		}
		tictactoe[strings.ToLower(user1Move)] = "X"
		if validateWin() {
			fmt.Println("Player 1 wins")
			break
		}
		fmt.Printf("%v to play", user2)
		fmt.Scan(&user2Move)
		tictactoe[strings.ToLower(user2Move)] = "O"
		if validateWin() {
			fmt.Println("Player 2 wins")
			break
		}
		fmt.Println(tictactoe)
		if i == 8 {
			fmt.Println("Board full ")
		}
	}

}
