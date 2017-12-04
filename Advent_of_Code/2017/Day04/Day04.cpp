#include <iostream> 	//std::cout
#include <fstream> 		//std::ifstream
#include <sstream> 		//std::stringstream
#include <vector>		//std::vector
#include <map>		    //std::map

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

		std::unordered_map<int, int> count;  // holds count of each encountered number 
		for (int i = 0; i < words_vector.size(); i++)        
    		count[ words_vector[i] ]++; 
		
		// for (auto &e:count)
    	// 	std::cout << e.first <<" : "<<e.second<<std::endl; 
	}

	std::cout<<"\n\n\n\t\t\t"<<counter<<"\n\n\n";

	return 0;
}