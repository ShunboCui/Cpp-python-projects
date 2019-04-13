#include <iostream>
#include <vector>
#include "GameBoard.h"
#include "File.h"

int main() {
	File newfile("com.txt");
	vector<vector<int>> total = newfile.read();
	Board board(total);
	board.show();
	//cout << board.get(0, 0) << endl;
	board.next();
	board.show();
	newfile.write(board.toSeq());
	return 0;

}
