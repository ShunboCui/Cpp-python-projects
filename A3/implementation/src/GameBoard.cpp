#include "GameBoard.h"
#include "CardStack.h"
#include "CardTypes.h"
#include "Stack.h"

#include <vector>

using std::vector;

BoardT::BoardT(vector<CardT> deck){
	vector<CardT> empty;
	vector<CardT> temp;
	for (int i = 0; i < 40; i++) {
		temp.push_back(deck[i]);
	}
	vector<CardT> temp2;
	for (int i = 40; i < 104; i++) {
		temp2.push_back(deck[i]);
	}
	this->T = tab_deck(temp);
	this->F = init_seq(8);
	this->D = CardStackT(temp2);
	this->W = CardStackT(empty);
}

bool BoardT::is_valid_tab_mv(CategoryT c, unsigned int n0, unsigned int n1) {
	if (c == Tableau) {
		return valid_tab_tab(n0, n1);
	}
	if (c == Foundation) {
		return valid_tab_foundation(n0, n1);
	}
	if (c == Deck) {
		return false;
	}
	if (c == Waste) {
		return false;
	}
}

bool BoardT::is_valid_waste_mv(CategoryT c, unsigned int n) {
	if (c == Tableau) {
		return valid_waste_tab(n);
	}
	if (c == Foundation) {
		return valid_waste_foundation(n);
	}
	if (c == Deck) {
		return false;
	}
	if (c == Waste) {
		return false;
	}
}

bool BoardT::is_valid_deck_mv() {
	return D.size() > 0;
}

void BoardT::tab_mv(CategoryT c, unsigned int n0, unsigned int n1) {
	if (c == Tableau) {
		T[n1] = T[n1].push(T[n1].top());
		T[n0] = T[n0].pop();
	}
	if (c == Foundation) {
		F[n1] = F[n1].push(T[n1].top());
		T[n0] = T[n0].pop();
	}
}

void BoardT::waste_mv(CategoryT c, unsigned int n) {
	if (c == Tableau) {
		T[n] = T[n].push(W.top());
		W = W.pop();
	}
	if (c == Foundation) {
		F[n] = F[n].push(W.top());
		W = W.pop();
	}
}

void BoardT::deck_mv() {
	W = W.push(D.top());
	D = D.pop();
}

CardStackT BoardT::get_tab(unsigned int i){
	return T[i];
}

CardStackT BoardT::get_foundation(unsigned int i) {
	return F[i];
}

CardStackT BoardT::get_deck() {
	return D;
}

CardStackT BoardT::get_waste() {
	return W;
}

bool BoardT::valid_mv_exists() {
	bool temp = false;
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 8; j++) {
			if (is_valid_tab_mv(Tableau, i, j)) {
				temp = true;
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 8; j++) {
			if (is_valid_tab_mv(Foundation, i, j)) {
				temp = true;
			}
		}
	}
	return temp;
}

bool BoardT::is_win_state() {
	for (int i = 0; i < 8; i++) {
		if (F[i].top().r != KING) {
			return false;
		}
	}
	return true;
}

//Local
vector<Stack<CardT>> BoardT::tab_deck(vector<CardT> deck) {
	SeqCrdStckT T;
	for (int i = 0; i < 10; i++) {
		vector<CardT> temp;
		for (int j = 4 * i; j < 4 * (i + 1); j++) {

			temp.push_back(deck[j]);
		}
		T.push_back(temp);
	}
	return T;
}

vector<CardStackT> BoardT::init_seq(int n) {
	vector<CardT> empty;
	vector<CardStackT> s;
	for (int i = 0; i < n; i++) {
		s.push_back(CardStackT(empty));
	}
	return s;
}

bool BoardT::valid_tab_tab(unsigned int n0, unsigned int n1) {
	if (T[n0].size() > 0){
		if (T[n1].size() > 0) {
			return tab_placeable(T[n0].top(), T[n1].top());
		}
		if (T[n1].size() == 0) {
			return true;
		}
	}
	if (T[n0].size() == 0) {
		return false;
	}
}

bool BoardT::valid_tab_foundation(unsigned int n0, unsigned int n1) {
	if (T[n0].size() > 0) {
		if (F[n1].size() > 0) {
			return foundation_placeable(T[n0].top(), F[n1].top());
		}
		if (F[n1].size() == 0) {
			return T[n0].top().r == ACE;
		}
	}
	if (T[n0].size() == 0) {
		return false;
	}
}

bool BoardT::valid_waste_tab(unsigned int n) {
	if (T[n].size() > 0) {
		return tab_placeable(W.top(), T[n].top());
	}
	if (T[n].size() == 0) {
		return true;
	}
}

bool BoardT::valid_waste_foundation(unsigned int n) {
	if (F[n].size() > 0) {
		return foundation_placeable(W.top(), F[n].top());
	}
	if (F[n].size() == 0) {
		return W.top().r == ACE;
	}
}

bool BoardT::tab_placeable(CardT c, CardT d) {
	return c.s == d.s && c.r == d.r - 1;
}

bool BoardT::foundation_placeable(CardT c, CardT d) {
	return c.s == d.s && c.r == d.r + 1;
}

bool BoardT::is_valid_pos(CategoryT c, unsigned int n) {
	if (c == Tableau) {
		if (n < 0 || n > 9) {
			return false;
		}
	}
	if (c == Foundation) {
		if (n < 0 || n > 7) {
			return false;
		}
	}
	return true;
}