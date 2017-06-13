#include <stm32f4xx.h>
#include <core_cm4.h>

//Zadanie wartosci do wykonania by "opiznic" wykonanie kolejnych fragmentow kodu
void Sleep(int ticks)
{
	int i;
	
	for(i = 0; i < ticks; i++);
}

int main(void)
{
	//
	RCC->AHB1ENR |= 1<<6;
	
	//PG13, PG14 (z dokumentacji)
	
	//MODER ustawia trybu pracy GPIO
	//wiemy ze MODER musimy ustawic wiemy z dokumentacji
	GPIOG->MODER &= ~((3<<26) | (3<<28));	//000011000000;
	GPIOG->MODER |=   (1<<26) | (1<<28);		
	
	while(1)
	{
		//ODR 
		//to ze ODR musimy ustawic wiemy z dokuemntacji (6.3 RCC register / 8.General purpose I/Os (GPIO))
		GPIOG->ODR |= (3<<13);			
		Sleep(500000);
		GPIOG->ODR &= ~(3<<13);
		Sleep(500000);
	};
}
