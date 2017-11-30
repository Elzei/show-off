#include "PerlinNoise.h"
#include <iostream>
#include <cmath>
#include <random>
#include <algorithm>

//Initialize with the reference values for permuation vector
PerlinNoise::PerlinNoise()
{
	//Initialize the permutation vector with the reference values
	p = {
		151, 160, 137, 91 
}
