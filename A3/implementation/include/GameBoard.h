/**
 * \file Gameboard.h
 * \author Shunbo Cui
 * \brief Defines variables and methods in GameBoard.
 */
#ifndef A3_GAME_BOARD_H_
#define A3_GAME_BOARD_H_

#include "CardStack.h"
#include "Stack.h"
#include "CardTypes.h"

#include <vector>

using std::vector;

/**
 * \brief The class of a GameBoard.
 */
class BoardT
{
	private:
		typedef vector<CardStackT> SeqCrdStckT;
		SeqCrdStckT T;
		SeqCrdStckT F;
		CardStackT D;
		CardStackT W;
		SeqCrdStckT tab_deck(vector<CardT> deck);
		SeqCrdStckT init_seq(int n);
		bool valid_tab_tab(unsigned int n0, unsigned int n1);
		bool valid_tab_foundation(unsigned int n0, unsigned int n1);
		bool valid_waste_tab(unsigned int n);
		bool valid_waste_foundation(unsigned int n);
		bool tab_placeable(CardT c, CardT d);
		bool foundation_placeable(CardT c, CardT d);
		bool is_valid_pos(CategoryT c, unsigned int n);
		bool two_decks(vector<CardT> deck);

	public:
		/**
		* @brief Construct the GameBoard.
		* @param deck The input deck of cards.
		*/
		BoardT(vector<CardT> deck);

		/**
		* @brief Checks if the move from tab is valid.
		* @param c The destination of movement.
		* @param n0 The number of Stack from tab.
		* @param n1 The number of Stack in destination.
		* @return The result of check.
		*/
		bool is_valid_tab_mv(CategoryT c, unsigned int n0, unsigned int n1);

		/**
		* @brief Checks if the move from waste is valid.
		* @param c The destination of movement.
		* @param n The number of Stack from waste.
		* @return The result of check.
		*/
		bool is_valid_waste_mv(CategoryT c, unsigned int n);

		/**
		* @brief Checks if the move from deck to waste is valid.
		* @return The result of check.
		*/
		bool is_valid_deck_mv();

		/**
		* @brief Move from tab to other stack.
		* @param c The destination of movement.
		* @param n0 The number of Stack from tab.
		* @param n1 The number of Stack in destination.
		*/
		void tab_mv(CategoryT c, unsigned int n0, unsigned int n1);

		/**
		* @brief Move from waste to other stack.
		* @param c The destination of movement.
		* @param n The number of stack in destination.
		*/
		void waste_mv(CategoryT c, unsigned int n);

		/**
		* @brief Move the card from deck to waste.
		*/
		void deck_mv();

		/**
		* @brief Get the ith tab from the GameBoard.
		* @param i The index of tab wanted.
		* @return The tab stack wanted.
		*/
		CardStackT get_tab(unsigned int i);

		/**
		* @brief Get the ith foundation from the GameBoard.
		* @param i The index of foundation wanted.
		* @return The foundation stack wanted.
		*/
		CardStackT get_foundation(unsigned int i);

		/**
		* @brief Get the deck from the GameBoard.
		* @return The deck stack wanted.
		*/
		CardStackT get_deck();

		/**
		* @brief Get the waste from the GameBoard.
		* @return The waste stack wanted.
		*/
		CardStackT get_waste();

		/**
		* @brief Checks if the valid move exists in current state.
		* @return The result of checking.
		*/
		bool valid_mv_exists();

		/**
		* @brief Checks if the GameBoard is in win state in current state.
		* @return The result of checking.
		*/
		bool is_win_state();
};
#endif

