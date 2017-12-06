#include <iostream>		//std::cout
#include <fstream> 		//std::ifstream
#include <sstream>		//std::istringstream
#include <vector>		//std::vector

int main() {
	std::string line;
	int number = 0; 
	int result = 0;
	std::vector< int > vector;

	//Loading the file
	std::ifstream puzzle;
	puzzle.open("puzzle_input");

	//Building vector
	while(getline( puzzle, line )){		
		std::stringstream line_stream ( line );
		while( line_stream >> number)
			vector.push_back( number );
	}
	
	std::cout<<"\n\n\n\t\t\t"<<result<<"\n\n\n";

	puzzle.close();

	return 0;
}