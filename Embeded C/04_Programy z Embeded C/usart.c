#include "stm32f4xx.h" 
#include "usart.h"

void Usart_SendChar(char ch)
{
    while (0 == (USART1->SR & USART_SR_TXE));
    USART1->DR = ch & 0x1ff;
}
