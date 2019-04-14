#include <iostream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <vector>
#include <stdexcept>
#include "GameBoard.h"
#include "File.h"
#include "Display.h"
#include "catch.h"

using std::vector;

TEST_CASE("General tests for File", "[File]") {

	SECTION("Test 1 for read") {
		File newfile("FileTest1.txt");
		vector<vector<int>> total = newfile.read();
		REQUIRE((total[0][0] == 1 && total[0][1] == 2));
	}
	SECTION("Test 2 for read") {
		File newfile("FileTest2.txt");
		vector<vector<int>> total = newfile.read();
		REQUIRE((total[0][0] == 0 && total[1][0] == 3));
	}
	SECTION("Test 1 for write") {
		File file("FileTest2.txt");
		vector<vector<int>> total;
		vector<int> row1 = { 1,2,3 };
		vector<int> row2 = { 4,5,6 };
		total.push_back(row1);
		total.push_back(row2);
		file.write(total);
		File newfile("FileTest2.txt");
		vector<vector<int>> newSeq = newfile.read();
		REQUIRE((total[0][0] == 1 && total[1][0] == 4));
	}


}