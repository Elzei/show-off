#include <iostream> 	//std::cout
#include <fstream> 		//std::ifstream
#include <sstream> 		//std::stringstream
#include <vector>		//std::vector
#include <map>		    //std::map

int main(int argc, char ** argv) {
	
	std::ifstream puzzle;
	puzzle.open("puzzle_input");

	int counter = 0;
	int counter_bad = 0;

	std::string row;
	std::string word;

	while(getline( puzzle, row )) {
		std::stringstream row_stream ( row );
		std::vector<std::string> words_vector;		
		counter++;

		//Building vector of words
		row_stream >> word;
		words_vector.push_back(word);

		while( row_stream >> word) {
			for( int i = 0; i < words_vector.size(); ++i) {
				if(words_vector[i] == word) {
					counter_bad++;
					std::cout<<"Word: "<<word<<" | ";
					for(int j = 0; j < words_vector.size(); j++) {
						std::cout<<" "<<words_vector[j]; 
					}
					std::cout<<std::endl;
					break;
				}					
			}
			words_vector.push_back(word);
		}
	}

	std::cout<<"\n\n\n\t\t\t"<<"All: "<<counter<<" | Bad: "<<counter_bad<<" | Correct: "<<counter-counter_bad<<"\n\n\n";

	return 0;
}

// #include <iostream>
// #include <algorithm>
// #include <sstream>
// #include <set>

// int main()
// {
//     std::string line;
//     int valid = 0;
//     while(getline(std::cin, line))
//     {
//         std::set<std::string> unique;
//         std::stringstream ss(line);
//         std::string word;
//         size_t count = 0;
//         while(ss >> word)
//         {
//             std::sort(word.begin(), word.end());
//             unique.insert(word);
//             count++;
//         }
//         valid += count == unique.size();
//     }
//     std::cout << valid << std::endl;
// }