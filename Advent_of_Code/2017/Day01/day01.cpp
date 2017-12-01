#include <iostream>
#include <fstream>

/*
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
*/

int main(int argc, char ** argv) {
	std::ifstream kod("captcha");
	int sum = 0;
	char current, next, first;
	kod>>first;
	current=first;

	while(kod>>next){		
		//std::cout<<"Current: "<<current<<" | Next: "<<next<<" | Sum: "<<sum<<std::endl;
		if(current == next) 
			sum += (current - '0');
		current = next;		
		//std::cout<<"Current: "<<current<<" | Next: "<<next<<" | Sum: "<<sum<<std::endl<<std::endl;
	}
	//std::cout<<"Firs: "<<first<<" | Current: "<<current;
	if(first == current)
		sum += (first -'0');
	//std::cout<<"\n\t\t\t"<<sum<<"\n";

	return 0;
}