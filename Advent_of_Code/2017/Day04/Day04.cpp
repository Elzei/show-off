#include <iostream> //std::cout
#include <fstream> 	//std::ifstream
#include <sstream> 	//std::stringstream
#include <vector>	//std::vector

int main(int argc, char ** argv) {
	
	std::ifstream puzzle;
	puzzle.open("puzzle_input");

	int counter = 0;

	std::string row;
	std::string word;

	while(getline( puzzle, row )) {
		std::stringstream row_stream ( row );
		std::vector<std::string> words_vector;

		//Building vector of words
		while( row_stream >> word) 
			words_vector.push_back(word);

		

		// for(auto x:words_vector)
		// 	std::cout<<x<<"\n";
	}

	std::cout<<"\n\n\n\t\t\t"<<counter<<"\n\n\n";

	return 0;
}