#include "Stack.h"
#include "catch.h"
#include "GameBoard.h"
#include "CardStack.h"
#include "CardTypes.h"

#include <algorithm>
#include <iostream>
#include <vector>
#include <stdexcept>

using std::vector;


TEST_CASE("General tests for GameBoard", "[GameBoard]") {
	std::vector<CardT> d;
	for (RankT rank = ACE; rank <= KING; rank++) {
		for (unsigned int suit = 0; suit < 4; suit++) {
			CardT n = { static_cast<SuitT>(suit), rank };
			d.push_back(n);
			d.push_back(n);
		}
	}

	BoardT board(d);

	SECTION("Test for is_valid_tab_mv") {
		//std::cout << board.get_tab(0).top().r << std::endl;
		//std::cout << board.get_tab(0).top().s << std::endl;
		REQUIRE(board.is_valid_tab_mv(Foundation, 0, 0) == true);
	}
	
	SECTION("Test for is_valid_waste_mv") {

		REQUIRE_THROWS_AS(board.is_valid_waste_mv(Foundation, 0), std::invalid_argument);
	}

	SECTION("Second test for is_valid_waste_mv") {
		board.deck_mv();
		REQUIRE(board.is_valid_waste_mv(Foundation, 0) == false);
	}

	SECTION("Test for is_valid_deck_mv") {
		REQUIRE(board.is_valid_deck_mv() == true);
	}
	

}