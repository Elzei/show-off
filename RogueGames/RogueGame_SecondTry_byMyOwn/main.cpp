#include <ncurses.h>
 
void init();
void erase( int y, int x );
void game_loop( char main_char, int row, int col, int ch );

// Entry function for game
int main() 
{
 	//Define main character symbol and initial position
	 int row = 10;
	 int col = 10;
	 char main_char = '@';

	 //Start ncurses
	 init();

	 //Print a welcome message on screen
	 printw("\t\tWelcome to the Rogue game.\n\t\tPress any key to start.\n\t\tIf you want to quit press \"q\"");

	 //Wait until the user press a key
	 int ch = getch();

	 //Clear the screen
	 clear();

	 //Start the game loop
	 game_loop(main_char, row, col, ch);

	 //Clear ncurses data structures
	 endwin();

	 return 0;
}

// Initialize the ncurses library
void init() 
{
	initscr();
	clear();
	noecho();
	cbreak();
	keypad(stdscr, TRUE);
	curs_set(0);
}

// Define the "erase" character, use an empty character for cleaning a cell or a
// visible character for showing the trace of a game character
void erase( int y, int x )
{
	mvaddch(y, x, '#');
}

// Main loop of the game
void game_loop( char main_char, int row, int col, int ch )
{
	//Check if user wishes to play the game
	if( ch == 'q' || ch == 'Q' )
		return;
	
	//Show the main character on screen
	mvaddch(row, col, main_char);
	refresh();

	while(1)
	{
		ch = getch();

		if( ch == KEY_LEFT)
		{
			erase(row, col);
			col = col - 1;
			mvaddch(row, col, main_char);
			refresh();
		}
		else if( ch == KEY_RIGHT)
		{
			erase(row, col);
			col = col + 1;
			mvaddch(row, col, main_char);
			refresh();
		}
		else if( ch == KEY_UP)
		{
			erase(row, col);
			col = row - 1;
			mvaddch(row, col, main_char);
			refresh();
		}
		else if( ch == KEY_DOWN)
		{
			erase(row, col);
			col = col + 1;
			mvaddch(row, col, main_char);
			refresh();
		}
	}
}

