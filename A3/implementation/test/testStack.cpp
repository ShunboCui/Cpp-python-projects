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



TEST_CASE("General tests for Stack", "[StackT]") {
	std::vector<CardT> d;
	for (RankT rank = ACE; rank <= KING; rank++) {
		for (unsigned int suit = 0; suit < 4; suit++) {
			CardT n = { static_cast<SuitT>(suit), rank };
			d.push_back(n);
			d.push_back(n);
		}
	}

	CardStackT stack(d);

	SECTION("Tests for top") {


		REQUIRE
		((stack.top().s == 3
			&& stack.top().r == 13));

	}

	SECTION("Tests for push") {
		CardT newcard = { static_cast<SuitT>(1), 1 };
		stack.push(newcard);
		REQUIRE
		((stack.top().s == 1
			&& stack.top().r == 1));
	}

	SECTION("Tests for pop") {
		CardT newcard = { static_cast<SuitT>(1), 1 };
		stack.push(newcard);
		stack.pop();
		REQUIRE
		((stack.top().s == 3
			&& stack.top().r == 13));
	}

	SECTION("Tests for size") {
		REQUIRE
		((stack.size() == 104));
	}

	SECTION("Tests for toSeq") {
		vector<CardT> seq2 = stack.toSeq();
		CardStackT stack2(seq2);
		REQUIRE
		((stack2.top().s == 3
			&& stack2.top().r == 13));
	}
}