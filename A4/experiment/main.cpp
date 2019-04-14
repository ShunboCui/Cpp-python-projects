#include <iostream>
#include <vector>
#include "GameBoard.h"
#include "File.h"
#include "Display.h"

int main() {
	File newfile("com.txt");
	vector<vector<int>> total = newfile.read();
	Board board(total);
	display(board.toSeq());
	//cout << board.get(0, 0) << endl;
	board.next();
	display(board.toSeq());
	//newfile.write(board.toSeq());
	return 0;

}