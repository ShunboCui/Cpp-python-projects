/**
 * \file Gameboard.h
 * \author Shunbo Cui
 * \brief Defines variables and methods in GameBoard.
 */
#ifndef GAMEBOARD_H
#define GAMEBOARD_H
#include <vector>

using namespace std;

/**
 * \brief The class of a GameBoard.
 */
class Board {
	private:
		vector<vector<int>> total;
		int count(int row, int col);
	public:
		/**
		* @brief Construct the GameBoard.
		* @param total The input sequence of integers representing the cell.
		*/
		Board(vector<vector<int>> total);

		/**
		* @brief Goes to the next game state.
		*/
		void next();

		/**
		* @brief Get the wanted cell in the sequence.
		* @param row The horizontal coordinate.
		* @param col The vertical coordinate.
		* @return The value in the coordinate.
		*/
		int get(int row, int col);
		vector<vector<int>> toSeq();
};
#endif
