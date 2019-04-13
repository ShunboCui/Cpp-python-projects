#include <iostream>
#include <fstream>

#include <vector>
#include <sstream>  
#include <string.h>
#include "File.h"
using namespace std;

File::File(string filename)
{
	char buffer[256];
	vector<vector<int>> total;
	fstream out;
	out.open(filename, ios::in);
	while (!out.eof())
	//for (int i = 0; i < 2; i++)
	{
		out.getline(buffer, 256, '\n');
		vector<int> intvec;
		vector<string> stringvec = split(buffer, ' ');
		for (int j = 0; j < stringvec.size(); j++) {
			//cout << stringvec[j] << endl;
			//int k = 0;
			int k = stoi(stringvec[j]);
			intvec.push_back(k);
		}
		total.push_back(intvec);

	}
	out.close();

	this->total = total;
}
vector<string> File::split(string str, char delimiter) {
	std::vector<string> internal;
	stringstream ss(str); // Turn the string into a stream.
	string tok;

	while (getline(ss, tok, delimiter)) {
		internal.push_back(tok);
	}

	return internal;
}

void File::write()
{
	ofstream in;
	in.open("com.txt", ios::trunc);
	/*
	int i;
	char a = 'a';
	for (i = 1; i <= 26; i++)
	{
		if (i < 10)
		{
			in << "0" << i << " " << a << "\n";
			a++;
		}
		else
		{
			in << i << " " << a << "\n";
			a++;
		}
	}
	*/
	int i = 0;
	in << i << " " << i << " "<< i << "\n";
	in.close();
}


int File::get(int row, int col) {
	return total[row][col];
}

int File::count(int row, int col) {
	int count;
	count = total[row - 1][col - 1] + total[row - 1][col] + total[row - 1][col + 1]
	      + total[row][col - 1]							  + total[row][col + 1]
		  + total[row + 1][col - 1] + total[row + 1][col] + total[row + 1][col + 1];
}
void main() {

	File board("com.txt");
	board.write();
	cout << board.get(0, 0) << endl;
	cin.get();

}