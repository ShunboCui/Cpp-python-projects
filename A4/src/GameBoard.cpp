#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <stdexcept>
#include "GameBoard.h"
#include "File.h"
using namespace std;

Board::Board(vector<vector<int>> total)
{
	for (int i = 0; i < total.size(); i++) {
		if (total.size() < 3 || total[i].size() < 3)
			throw std::invalid_argument("Sequence too small");
	}

	this->total = total;
}


int Board::get(int row, int col) {
	if (row < 0 || row >= total.size())
		throw std::invalid_argument("Out of bound");
	if (col < 0 || col >= total[row].size())
		throw std::invalid_argument("Out of bound");
	return total[row][col];
}

int Board::count(int row, int col) {
	int a, b, c,
		d, e,
		f, g, h;
	int sum;

	if (row == 0 || col == 0) a = 0;
	else a = total[row - 1][col - 1];

	if (row == 0) b = 0;
	else b = total[row - 1][col];

	if (row == 0 || col == total[row].size() - 1) c = 0;
	else c = total[row - 1][col + 1];

	if (col == 0) d = 0;
	else d = total[row][col - 1];

	if (col == total[row].size() - 1) e = 0;
	else e = total[row][col + 1];

	if (row == total.size() - 1 || col == 0) f = 0;
	else f = total[row + 1][col - 1];

	if (row == total.size() - 1) g = 0;
	else g = total[row + 1][col];

	if (row == total.size() - 1 || col == total[row].size() - 1) h = 0;
	else h = total[row + 1][col + 1];

	sum = a + b + c + d + e + f + g + h;
	return sum;
}

void Board::next() {
	vector<vector<int>> temp(total.size());
	for (int i = 0; i < total.size(); i++) {
		vector<int> temp2(total[i].size());
		temp[i] = temp2;
		for (int j = 0; j < total[i].size(); j++) {
			if (total[i][j] == 1) {
				if (count(i, j) < 2) {
					temp[i][j] = 0;
				}
				else if (count(i, j) > 3) {
					temp[i][j] = 0;
				}
				else temp[i][j] = 1;
			}
			if (total[i][j] == 0) {
				if (count(i, j) == 3) {
					temp[i][j] = 1;
				}
				else temp[i][j] = 0;
			}
			//cout << count(i, j);
		}

	}
	total = temp;
}
/*
void Board::show() {
	for (int i = 0; i < total.size(); i++) {
		for (int j = 0; j < total[i].size(); j++) {
			if (total[i][j]) cout << (char)254;
			else cout << (char)9633;

		}
		cout << endl;

	}
	cin.get();
}
*/
vector<vector<int>> Board::toSeq() {
	vector<vector<int>> newSeq;
	newSeq = total;
	return newSeq;
}

