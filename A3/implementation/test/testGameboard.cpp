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

	SECTION("Test for tab_mv") {
		REQUIRE_THROWS_AS(board.tab_mv(Tableau, 0, 1), std::invalid_argument);
	}

	SECTION("Test for waste_mv") {
		board.deck_mv();
		CardStackT waste = board.get_waste();
		REQUIRE_THROWS_AS(board.waste_mv(Tableau, 0), std::invalid_argument);
	}

	SECTION("Test for deck_mv") {
		board.deck_mv();
		CardStackT waste = board.get_waste();
		board.deck_mv();
		CardStackT waste2 = board.get_waste();
		board.deck_mv();
		CardStackT waste3 = board.get_waste();

		REQUIRE(((waste3.top().r == 13) && (waste3.top().s == 2)));
	}

	SECTION("Test for get_tab") {
		CardStackT tab = board.get_tab(0);

		REQUIRE(tab.size() == 4);
	}

	SECTION("Test for get_foundation") {
		CardStackT foundation = board.get_foundation(0);

		REQUIRE(foundation.size() == 0);
	}

	SECTION("Test for get_deck") {
		CardStackT deck = board.get_deck();

		REQUIRE(deck.size() == 64);
	}

	SECTION("Test for get_waste") {
		CardStackT waste = board.get_waste();

		REQUIRE(waste.size() == 0);
	}

	SECTION("Test for valid_mv_exists") {
		REQUIRE(board.valid_mv_exists());
	}

	SECTION("Test for is_win_state") {
		REQUIRE(board.is_win_state() == false);
	}

}