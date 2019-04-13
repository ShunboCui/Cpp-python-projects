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
		if (intvec.size() != 0) {
			total.push_back(intvec);
		}


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
	int a, b, c,
		d,    e,
		f, g, h;
	int count;

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

	if (row == total.size() - 1||col == 0) f = 0;
	else f = total[row + 1][col - 1];

	if (row == total.size() - 1) g = 0;
	else g = total[row + 1][col];

	if (row == total.size() - 1 || col == total[row].size() - 1) h = 0;
	else h = total[row + 1][col + 1];

	count = a + b + c + d + e + f + g + h;
	return count;
}

void File::next() {
	vector<vector<int>> temp(total.size());
	for (int i = 0; i < total.size(); i++) {
		vector<int> temp2(total[i].size());
		temp[i] = temp2;
		for (int j = 0; j < total[i].size(); j++) {
			if (total[i][j] == 1){
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
void File::show() {
	for (int i = 0; i < total.size(); i++) {
		for (int j = 0; j < total[i].size(); j++) {
			cout << total[i][j];



		}
		cout << endl;

	}
}

void main() {

	File board("com.txt");
	board.show();
	//cout << board.get(0, 0) << endl;
	board.next();
	board.show();
	cin.get();

}