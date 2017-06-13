// Adam Orcholski, 2017, Global Logic
#include <stm32f4xx.h>
#include <core_cm4.h>

void Sleep(int ticks)
{
    int i;
    
    for (i = 0; i < ticks; i++);
}

#define CORE_CLOCK_SPEED        16000000
#define USART_BAUD_RATE9600     9600

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
    
    // output LEDs: PG13, PG14
    GPIOG->MODER &= ~((3<<26) | (3<<28)); // clear bitfields
    GPIOG->MODER |=   (1<<26) | (1<<28);    // set mode for pins 13 and 14
    
    // input PA0
    GPIOA->MODER &= ~(3<<0);

    // usart config: pb6 - tx (white), pb7 - rx (green)
    GPIOB->MODER &= ~((3 << 12) | (3 << 14)); // clear bitfields
    GPIOB->MODER |=   (2 << 12) | (2 << 14);  // set alternate function mode for pins 6 and 7
    GPIOB->AFR[0] |=  (7 << 28) | (7 << 24); 
    
    // config usart 1
    USART1->BRR = CORE_CLOCK_SPEED/USART_BAUD_RATE9600;
    USART1->CR1 |= USART_CR1_TE; // transmit enable
    
    // enable usart 1
    USART1->CR1 |= USART_CR1_UE;
    
    while(1)
    {
        send_string("dupa666\r\n");
        Sleep(1000000);
    }
}