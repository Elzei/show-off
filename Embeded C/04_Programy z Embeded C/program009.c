#include <stm32f4xx.h>
#include <core_cm4.h>
#include "gpio.h"
#include "usart.h"

#include <stdio.h>

#define CORE_CLOCK_SPEED        16000000
#define USART_BAUD_RATE9600     9600

void sleep(int ticks)
{
	int i = 0;
	for(i = 0; i < ticks; i++)
	{
		;
	}
}

typedef enum usart_input_e
{
    USART_INPUT_A = (uint32_t)'A',
    USART_INPUT_B = (uint32_t)'B',

} usart_input_t;

typedef enum led_state_e
{
    LED_ON,
    LED_OFF
} led_state_t;

volatile led_state_t ledState = LED_OFF;

void send_char(char nic)
{
    while (0 == (USART1->SR & USART_SR_TXE));
    USART1->DR = nic & 0x1ff;
}

char received_char()
{
    while (0 == (USART1->SR & USART_SR_RXNE));
    return USART1->DR;
}

void send_string(char *string)
{
    while(*string)
    {
        send_char(*string);
        string++;        
    }
    send_char('\r');
    send_char('\n');
}

void toggleLeds(usart_input_t usart_input)
{
    if (USART_INPUT_A == usart_input)
    {
        GPIO_set_output(GPIOG, GPIO_PIN_13);
    }
    else if (USART_INPUT_B == usart_input)
    {
        GPIO_set_output(GPIOG, GPIO_PIN_14);                
    }    
}

void TIM6_DAC_IRQHandler()
{
    if (ledState == LED_OFF)
    {
        GPIO_set_output(GPIOG, GPIO_PIN_13);
        ledState = LED_ON;
    }
    else
    {
        GPIO_clear_output(GPIOG, GPIO_PIN_13);
        ledState = LED_OFF;
    }
    TIM6->SR = 0;
}



int main(void)
{
    // ####enable clock for GIPO A i GPIO G
    RCC->AHB1ENR = RCC_AHB1ENR_GPIOAEN | RCC_AHB1ENR_GPIOGEN | RCC_AHB1ENR_GPIOBEN;
    
    // ####enable clock for USART1
    RCC->APB2ENR |= RCC_APB2ENR_USART1EN;
    
    // #### port config for PG13 and PG14 - leds
    GPIO_config(GPIOG, GPIO_MODE_OUTPUT, GPIO_PIN_13);
    GPIO_config(GPIOG, GPIO_MODE_OUTPUT, GPIO_PIN_14);

    GPIO_set_output(GPIOG, GPIO_PIN_13);
    GPIO_set_output(GPIOG, GPIO_PIN_14);
    
    GPIO_clear_output(GPIOG, GPIO_PIN_13);
    GPIO_clear_output(GPIOG, GPIO_PIN_14);
    
    // usart config for port B - pin6 and pin7
    //pb6 - white cable
    //pb7 - green cable
    GPIO_config(GPIOB, GPIO_MODE_ALTERNATE, GPIO_PIN_6);
    GPIO_config(GPIOB, GPIO_MODE_ALTERNATE, GPIO_PIN_7);
    
    // #### set alternate function, when register is divided to LOW and HIGH register, we use array indexes
    //GPIOB->AFR[0] |= (7 << 28) | (7 << 24);
    //GPIO_set_alternate_function(GPIOB, GPIO_PIN_6, GPIO_AF_7);
    //GPIO_set_alternate_function(GPIOB, GPIO_PIN_7, GPIO_AF_7);
    
    // #### Config for stlink COM
    GPIO_config(GPIOA, GPIO_MODE_ALTERNATE, GPIO_PIN_9);
    GPIO_config(GPIOA, GPIO_MODE_ALTERNATE, GPIO_PIN_10);
    
    GPIO_set_alternate_function(GPIOA, GPIO_PIN_9, GPIO_AF_7);
    GPIO_set_alternate_function(GPIOA, GPIO_PIN_10, GPIO_AF_7);    
    
    USART_config(USART1, CORE_CLOCK_SPEED/USART_BAUD_RATE9600, USART_MODE_BOTH);
    USART_enable(USART1);
    // ####cofig USART1
    //USART1->BRR = CORE_CLOCK_SPEED/USART_BAUD_RATE9600;
    // ####transmitter USART1 enable
    //USART1->CR1 |= USART_CR1_TE;
    //USART1->CR1 |= USART_CR1_RE;
    
    // ####enable USART1
    //USART1->CR1 |= USART_CR1_UE;
    
    /*
        ############# TIMERS
    */
    
    // init basic timer 6
    RCC->APB1ENR |= RCC_APB1ENR_TIM6EN;
    
    // config 
    TIM6->CR1 |= TIM_CR1_CEN; // timer enabled

    // - counting
    TIM6->CNT = 0; // counter = 0;
    TIM6->PSC = 16000 - 1; // prescaler / divider - 16 000 000 Hz / 16 000 Hz = 1000Hz
    // T[s] = 1 / F [Hz]; T[s] = 1/1000 = 0,001 [s] = 1 [ms]
    
    TIM6->ARR = 1000 - 1; // cause counter counts from 0 to auto-reload value
    
    /*
        ############# TIMERS
    */    
    char c = 0;
    char array[50];
    int i = 0;
    usart_input_t usart_input;
	while(1)
	{
        //send_string("dupa66asdasdasd6\r\n");
        //sleep(100000);

        if (0 != (USART1->SR & USART_SR_RXNE))
        {
          c = USART1->DR;
            // sprawdzenie dlugosci tablicy!!!!!!!
          if (c == '\n' || c == '\0')
          {
              array[i] = '\0';
              send_string(array);
              i = 0;
          }
          else
          {
              array[i] = c;
              i++;
              if (49 == i)
              {
                  array[i] = '\0';
                  i = 0;
                  char *command = "Command to long!";
                  send_string(command);
              }
          }
          //usart_input = (uint32_t)c;
          //toggleLeds(usart_input);
          //send_char(c);            
        }
        //c = received_char();     
	}
}