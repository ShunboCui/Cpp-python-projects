#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
void display(vector<vector<int>> total) {
	for (int i = 0; i < total.size(); i++) {
		for (int j = 0; j < total[i].size(); j++) {
			if (total[i][j] != 0 && total[i][j] != 1)
				throw std::invalid_argument("Invalid number");
			if (total[i][j]) cout << (char)254;
			else cout << (char)32;

		}
		cout << endl;

	}
//	cin.get();
}
