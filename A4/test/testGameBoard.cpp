#include <iostream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <vector>
#include <stdexcept>
#include "GameBoard.h"
#include "File.h"
#include "Display.h"
#include "catch.h"

using std::vector;

TEST_CASE("General tests for GameBoard", "[GameBoard]") {
	File newfile("GameBoardTest1.txt");
	vector<vector<int>> total = newfile.read();
	Board board(total);

	SECTION("Test 1 for get") {
		vector<vector<int>> total = newfile.read();
		REQUIRE((board.get(0,0)==0 && board.get(1, 2)== 1));
	}
	SECTION("Test 2 for get") {
		vector<vector<int>> total = newfile.read();
		REQUIRE_THROWS_AS(board.get(5, 0) == 0 , std::invalid_argument);
	}
	SECTION("Test 1 for next") {
		board.next();
		REQUIRE(((board.get(1, 2) == 1&& board.get(2, 2) == 1 && board.get(0, 2) == 1)));
	}
	SECTION("Test 1 for toSeq") {
		vector<vector<int>> newSeq = board.toSeq();

		REQUIRE(((newSeq[1][2] == 1 && newSeq[2][2] == 0 && newSeq[0][2] == 0)));
	}



}