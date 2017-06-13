#ifndef STM32_GPIO_H
#define STM32_GPIO_H

typedef enum pin_number_e
{
	GPIO_PIN_0 = 0,
	GPIO_PIN_1,
    GPIO_PIN_2,
    GPIO_PIN_3,
    GPIO_PIN_4,
    GPIO_PIN_5,
    GPIO_PIN_6,
    GPIO_PIN_7,
    GPIO_PIN_8,
    GPIO_PIN_9,
    GPIO_PIN_10,
    GPIO_PIN_11,
    GPIO_PIN_12,
    GPIO_PIN_13,
    GPIO_PIN_14,
	GPIO_PIN_15
} gpio_pin_number_t;

typedef enum gpio_alternate_function_e
{
   GPIO_AF_0 = 0,
   GPIO_AF_1,
   GPIO_AF_2,
   GPIO_AF_3,
   GPIO_AF_4,
   GPIO_AF_5,
   GPIO_AF_6,
   GPIO_AF_7,
   GPIO_AF_8,
   GPIO_AF_9,
   GPIO_AF_10,
   GPIO_AF_11,
   GPIO_AF_12,
   GPIO_AF_13,
   GPIO_AF_14,
   GPIO_AF_15
} gpio_alternate_function_t;

typedef enum gpio_mode_e
{
    GPIO_MODE_INPUT = 0,
    GPIO_MODE_OUTPUT,
    GPIO_MODE_ALTERNATE
} gpio_mode_t;

typedef enum pin_state_e
{
    PIN_STATE_RESET = 0,
    PIN_STATE_SET
} pin_state_t;

// ustawia tryb pinu, dla dowolnego portu GPIO
void GPIO_config(GPIO_TypeDef * p_gpio, gpio_mode_t mode, gpio_pin_number_t pin);
// ustawia pin w stan '1', dla dowolnego portu GPIO
void GPIO_set_output(GPIO_TypeDef * p_gpio, gpio_pin_number_t pin);
// ustawia pin w stan '0', dla dowolnego portu GPIO
void GPIO_clear_output(GPIO_TypeDef * p_gpio, gpio_pin_number_t pin);
// odczytnie stanu wyjscia na pin dowolnego GPIO
// zwraca'0' lub '1'
pin_state_t GPIO_get_output(GPIO_TypeDef * p_gpio, gpio_pin_number_t pin);
// odczytnie stanu wejscia na pin dowolnego GPIO
// zwraca'0' lub '1'
pin_state_t GPIO_get_input(GPIO_TypeDef * p_gpio, gpio_pin_number_t pin);
//Alternate function to funkcja gdzie PIN przejmuje kontrolę na urządzeniu wewnętrznym (peryferiały)
void GPIO_set_alternate_function(GPIO_TypeDef * p_gpio, gpio_alternate_function_t new_af, gpio_pin_number_t pin);

#endif //STM32_GPIO_H
