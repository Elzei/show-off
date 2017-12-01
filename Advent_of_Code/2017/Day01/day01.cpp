#include <iostream>
#include <fstream>

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