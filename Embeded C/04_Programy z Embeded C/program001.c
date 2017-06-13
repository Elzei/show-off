//GPIO 0x4002 1800

#define GPIO_G_ADDR 0x40021800

typedef struct gipi_register
{
	unsigned MODDER; //znajduje sie na offsecie 0
	unsigned TYPER;  //znajduje sie na offsecie 4 (bo unsigned jest 4 bajtowy)
	unsigned OSPEED; //znajduje sie na offsecie 8 (bo unsigned jest 4 bajtowy)
} gpio_reg_t;

//example of address
int main(void)
{
	unsigned address = 0x40021800;
	
	gpio_reg_t * GPIO_G = (gpio_reg_t*)0x40021800;
	gpio_reg_t * GPIO_A = (gpio_reg_t*)0x40020000;
	
	GPIO_G->OSPEED = 123;
	GPIO_G->MODDER = 1;
	
	GPIO_A->OSPEED = 123;
	GPIO_A->MODDER = 1;
	
	while(1);
}