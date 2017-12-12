TO TEST:
https://pl.wikipedia.org/wiki/Drzewo_sufiksowe
http://namiekko.pl/2015/06/17/elegancki-algorytm-miesiaca-kadane/
https://codility.com/media/train/15-DynamicProgramming.pdf
*/


#include <iostream>	//std::cout
#include <time.h>	//clock()
#include <string>	//std::string
#include <map>		//std::map

int solution(std::string);
int UNI(std::string);

int main(int argc, char **argv) {
	clock_t tStart = clock();
	std::cout << "Solution: " << solution(argv[1]) << "\n";
	std::cout << "Time: " << (double)(clock() - tStart)/CLOCKS_PER_SEC;
}

int solution(std::string s) {
	int result = 0;
	std::string subs;

	for(int i = 0; i < s.size(); i++)
		for(int j = 1; j <= s.size() - i; j++) 
			if((subs = s.substr(i, j)).size() > 1 )
				result += UNI(subs);

	return result+s.size();
}

int UNI(std::string s) {
	int count = 0;
	std::map <char, int> counter;

	//Feeling map
	for(int i = 0; i < s.size(); i++)
		counter[ s[i] ]++;
	
	//Counting unique
	for(int i = 0; i < counter.size(); i++)
		if(counter[ i ] == 1)
			count++;

	return count;
}