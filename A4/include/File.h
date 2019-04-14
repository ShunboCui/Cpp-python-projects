/**
 * \file File.h
 * \author Shunbo Cui
 * \brief Defines methods to read and write input file.
 */
#ifndef FILE_H
#define FILE_H
#include <vector>

using namespace std;
/**
 * \brief The class of File.
 */
class File {
	private:
		string filename;
		vector<string> split(string str, char delimiter);
	public:
		/**
		* @brief Construct the File.
		* @param filename The name of the file.
		*/
		File(string filename);

		/**
		* @brief Read the input file and output as a 2-dimentional sequence.
		* @return The output sequence.
		*/
		vector<vector<int>> read();

		/**
		* @brief Write the 2-dimentional sequence into the file.
		* @param total The sequence to be written.
		*/
		void write(vector<vector<int>> total);
};
#endif
