#ifndef FILE_H
#define FILE_H
#include <vector>

using namespace std;

class File {
	private:
		vector<vector<int>> total;
		vector<string> split(string str, char delimiter);
		int count(int row, int col);
		void write();
	public:
		File(string filename);
		void next();
		void show();

		int get(int row, int col);
};
#endif
