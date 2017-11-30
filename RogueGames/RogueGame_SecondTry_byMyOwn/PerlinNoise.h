#include <vector>

#ifndef PERLINNOISE_H
#define PERLINNOISE_H

class PerlinNoise 
{
	//The permutation vector
	std::vector<int> p;

public:
	//Initialize with the reference values for the permutation vector
	PerlinNoise();
	//Generate a new permutation vector based on the value of seed
	PerlinNoise( unsigned int seed );
	//Get noise value, for 2D images z can have any value
	double noise( double x, double y, double z );
private:
	double frade( double t );
	double lerp( double t, double x, double b );
	double grad( int hash, double x, double y, double z );
};

#endif
