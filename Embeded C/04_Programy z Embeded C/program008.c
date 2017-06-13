// Adam Orcholski, 2017, Global Logic
#include <stm32f4xx.h>
#include <core_cm4.h>

void Sleep(int ticks)
{
    int i;
    
    for (i = 0; i < ticks; i++);
}

#define CORE_CLOCK_SPEED        16000000
#define USART_BAUD_RATE9600     9700

void send_char(char nic)
{
    while (0 == (USART1->SR & USART_SR_TXE));
    USART1->DR = nic & 0x1ff;
}

void send_string(char * string)
{
    while('\0' != *string)
    {
        send_char(*string);
        string++;
    }
}

int main(void)
{
    // enable clocks
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOGEN | RCC_AHB1ENR_GPIOAEN | RCC_AHB1ENR_GPIOBEN;
    RCC->APB2ENR |= RCC_APB2ENR_USART1EN;
    RCC->APB1ENR |= RCC_APB1ENR_TIM6EN;  //enable timer clock
    
    // output LEDs: PG13, PG14
    GPIOG->MODER &= ~((3<<26) | (3<<28)); // clear bitfields
    GPIOG->MODER |=   (1<<26) | (1<<28);    // set mode for pins 13 and 14
    
    // input PA0
    GPIOA->MODER &= ~(3<<0);

    // usart config: pb6 - tx (white), pb7 - rx (green)
    GPIOB->MODER &= ~((3 << 12) | (3 << 14)); // clear bitfields
    GPIOB->MODER |=   (2 << 12) | (2 << 14);  // set alternate function mode for pins 6 and 7
    GPIOB->AFR[0] |=  (7 << 24) | (7 << 28); 
    
    // config usart 1
    USART1->BRR = CORE_CLOCK_SPEED/USART_BAUD_RATE9600;
    USART1->CR1 |= USART_CR1_TE; // transmit enable
    
    // enable usart 1
    USART1->CR1 |= USART_CR1_UE;
    
    //init basic timer 6
    TIM6->CNT = 0; //counter = 0
    TIM6->PSC = 16000 -1; //prescaler/drive - 16 000 000 Hz / 16 000 Hz = 1000 Hz
    //T[s] = 1 / F[z] ; T[s] = 1/1000 = 0,001 [s], 1[ms]
    TIM6->ARR = 1000 - 1;
    
    TIM6->CCR1 |= TIM_CR1_CEN;  //enable timer
    
    
    while(1)
    {
        
    }
}