
tictactoe = Dict(
    "a1"=> "1",
	"a2"=> "2",
	"a3"=> "3",
	"b1"=> "4",
	"b2"=> "5",
	"b3"=> "6",
	"c1"=> "7",
	"c2"=>"8",
	"c3"=> "9",
)
stringArray = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
#printlnln(tictacetoe)
#printlnln(stringArray)

function validateWin()
    if tictactoe["a1"] == tictactoe["a2"] == tictactoe["a3"]
		println("c1")
		return true
	elseif tictactoe["b1"] == tictactoe["b2"] == tictactoe["b3"]
		println("c2")
		return true
	elseif tictactoe["c1"] == tictactoe["c2"] == tictactoe["c3"]
		println("c3")
		return true
	elseif tictactoe["a1"] == tictactoe["b1"] == tictactoe["c1"]
		println("c4")
		return true
	elseif tictactoe["a2"] == tictactoe["b2"] == tictactoe["c2"]
		println("c5")
		return true
	elseif tictactoe["a3"] == tictactoe["b3"] == tictactoe["c3"]
		println("c7")
		return true
	elseif tictactoe["a1"] == tictactoe["b2"] == tictactoe["c3"]
		println("c8")
		return true
	elseif tictactoe["a3"] == tictactoe["b2"] == tictactoe["c1"]
		println("c9")
		return true
	else
		println("f1")
		return false
    end
end

#validateWin()

function posCheck(position::String)
    found = false
    for i in stringArray
        if position == i
            found = true
        end
    end
    if found
        return true
    else
        return false
    end
end

println("The game will not have a graphic display and the tic-tac-toe board has to be simulated in the mind")
println("The board representation is same as the chess board. The horizontal rows are represented by 1,2,3")
println("The vertical columns are represented by alphabets A,B,C")
println("""
			3 _ | _ | _
			2 _ | _ | _
			1   |   | 
			  A   B   C
     """)
println("The move is played by mentioning the position on the board ex:A1")
println("The first player starts with cross \'X\' and the next player is \'O\' ")
println("Let's begin the game")

println("Enter the username of the player1")
user1 = readline()
println("Enter the username of the player2")
user2 = readline()

for i in 1:9
    posFlag = false
    user1Move = ""
    user2Move = ""
    while !posFlag
        println("Enter the User 1 position")
        user1Move = readline()
        if posCheck(lowercase(user1Move))
            posFlag = true
            break
        else
            println("Invalid position")
        end
    end
    tictactoe[lowercase(user1Move)] = "X"
    println(tictactoe)
    if validateWin()
        println("Player 1 Wins")
        break
    end
    posFlag = false
    while !posFlag
        println("Enter the User 2 position")
        user2Move = readline()
        if posCheck(lowercase(user2Move))
            posFlag = true
        else
            println("Invalid position")
        end
    end
    tictactoe[lowercase(user2Move)] = "O"
    println(tictactoe)
    if validateWin()
        println("Player 2 Wins")
        break
    end
end
