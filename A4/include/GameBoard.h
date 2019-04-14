#ifndef GAMEBOARD_H
#define GAMEBOARD_H
#include <vector>

using namespace std;
class Board {
	private:
		vector<vector<int>> total;
		int count(int row, int col);
	public:
		Board(vector<vector<int>> total);
		void next();
		//void show();
		int get(int row, int col);
		vector<vector<int>> toSeq();
};
#endif
