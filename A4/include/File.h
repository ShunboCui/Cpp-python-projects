#ifndef FILE_H
#define FILE_H
#include <vector>

using namespace std;

class File {
	private:
		vector<vector<int>> total;
		vector<string> split(string str, char delimiter);
		int count(int row, int col);
	public:
		File(string filename);

		void write();
		int get(int row, int col);
};
#endif
