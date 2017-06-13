//pushing button
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
	//enable clock
    RCC->AHB1ENR |= 1 << 6; //clock
	RCC->AHB1ENR |= RCC_AHB1ENR_GPIOEEN | RCC_AHB1ENR_GPIOAEN;
	
	//output LEDS: PG13, PG14 (z dokumentacji)
	//MODER ustawia trybu pracy GPIO
	GPIOG->MODER &= ~((3 << 26) | (3 << 28)); //clean bitfields
	GPIOG->MODER |=   (1 << 26) | (1 << 28);  //set mode for pins 13 and 14
    
    //input PA0
    GPIOA->MODER &= ~(3<<0);
	
    volatile int buttonPushed;
    
	while(1)
	{
        buttonPushed = GPIOA->IDR & 1;
        if(buttonPushed == 1)
        {
            GPIOG->BSRR = 3 << 13;
        }
        else
        {
            GPIOG->BSRR = 3 << 29;
        }
        Sleep(100000);
	};
}