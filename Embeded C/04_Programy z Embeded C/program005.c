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
		//8.4.7 Manual (BSRR - sluzy do zerowania i resetowania calego rejestru)
		GPIOG->BSRR |= (3<<13);			
		Sleep(900000);
		GPIOG->BSRR &= ~(3<<29);
		Sleep(900000);
	};
}
