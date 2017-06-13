#include "stm32f4xx.h" 
#include "gpio.h"

// ustawia tryb pinu, dla dowolnego portu GPIO
void GPIO_config(GPIO_TypeDef * p_gpio, gpio_mode_t mode, gpio_pin_number_t pin)
{
    if(p_gpio) //sprawdzamy czy wskaznik p_gpio nie jest null pointerem
    {
        int offset = pin * 2; //przemnazamy przez 2 ponieważ PIN dla GPIO zajmuje 2 bity
        p_gpio->MODER &= ~(3 << offset); //clean bitfields
        p_gpio->MODER |= (mode << offset);  //set mode for pin
    }
}

// ustawia pin w stan '1', dla dowolnego portu GPIO
void GPIO_set_output(GPIO_TypeDef * p_gpio, gpio_pin_number_t pin)
{
    if(p_gpio) //sprawdzamy czy wskaznik p_gpio nie jest null pointerem
    {
        int offset = pin * 2; //przemnazamy przez 2 ponieważ PIN dla GPIO zajmuje 2 bity
        p_gpio->MODER |= (1 << offset);  //set mode for pin
    }
}

// ustawia pin w stan '0', dla dowolnego portu GPIO
void GPIO_clear_output(GPIO_TypeDef * p_gpio, gpio_pin_number_t pin)
{
    if(p_gpio) //sprawdzamy czy wskaznik p_gpio nie jest null pointerem
    {
        int offset = pin * 2; //przemnazamy przez 2 ponieważ PIN dla GPIO zajmuje 2 bity
        p_gpio->MODER |= (0 << offset);  //set mode for pin   
    }
}

// odczytnie stanu wyjscia na pin dowolnego GPIO
// zwraca'0' lub '1'
pin_state_t GPIO_get_output(GPIO_TypeDef * p_gpio, gpio_pin_number_t pin)
{
    pin_state_t pin_state = PIN_STATE_RESET;
    if(p_gpio) //sprawdzamy czy wskaznik p_gpio nie jest null pointerem
    {        
        if(( p_gpio->ODR >> pin ) & 0x1)
        {
            pin_state = PIN_STATE_SET;
        }
    }
    return pin_state;
}

// odczytnie stanu wejscia na pin dowolnego GPIO
// zwraca'0' lub '1'
pin_state_t GPIO_get_input(GPIO_TypeDef * p_gpio, gpio_pin_number_t pin)
{
    pin_state_t pin_state = PIN_STATE_RESET;
    if(p_gpio) //sprawdzamy czy wskaznik p_gpio nie jest null pointerem
    {        
        if(( p_gpio->IDR >> pin ) & 0x1)
        {
            pin_state = PIN_STATE_SET;
        }
    }
    return pin_state;
}

//Alternate function to funkcja gdzie PIN przejmuje kontrolę na urządzeniu wewnętrznym (peryferiały)
void GPIO_set_alternate_function(GPIO_TypeDef * p_gpio, gpio_alternate_function_t new_af, gpio_pin_number_t pin)
{
	if(p_gpio) //sprawdzamy czy wskaznik p_gpio nie jest null pointerem
	{
		if(new_af <= GPIO_AF_7)
        {
            p_gpio->AFR[0] |= (pin<<new_af*4); //przemnazamy przez 4 ponieważ PIN dla USART zajmuje 4 bity
        }
        else
        {
            p_gpio->AFR[1] |= ((pin<<new_af*4)-8); //przemnazamy przez 4 ponieważ PIN dla USART zajmuje 4 bity, odejmujemy 8 bitów by "trafić" na odpowiedni bit
        }
	}
}
