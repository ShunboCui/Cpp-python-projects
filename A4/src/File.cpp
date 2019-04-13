#include <iostream>
#include <fstream>

#include <vector>
#include <sstream>  
#include <string.h>
#include "File.h"
using namespace std;

File::File(string filename) {
	this->filename = filename;
}
vector<vector<int>> File::read()
{
	char buffer[256];
	vector<vector<int>> total;
	fstream out;
	out.open(filename, ios::in);
	while (!out.eof())

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
		if (intvec.size() != 0) {
			total.push_back(intvec);
		}


	}
	out.close();

	return total;
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

void File::write(vector<vector<int>> total)
{
	ofstream in;
	in.open(filename, ios::trunc);

	for (int i = 0; i < total.size(); i++) {
		for (int j = 0; j < total[i].size(); j++) {
			in << total[i][j] << " ";
		}
		in << "\n";
	}
	in.close();
}


