#ifndef FILE_H
#define FILE_H
#include <vector>

using namespace std;

class File {
	private:
		string filename;
		vector<string> split(string str, char delimiter);
	public:
		File(string filename);
		vector<vector<int>> read();
		void write(vector<vector<int>> total);
};
#endif
