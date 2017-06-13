def showNumber(num):
    zero = [
        "  ****  ",
        " *   ** ",
        " *  * * ",
        " * *  * ",
        " **   * ",
        " *    * ",
        "  ****  ",
        "        " ]
    one = [
        "    **  ",
        "   * *  ",
        "  *  *  ",
        "     *  ",
        "     *  ",
        "     *  ",
        "    *** ",
        "        " ]
    two = [
        "  ****  ",
        " *    * ",
        "     *  ",
        "    *   ",
        "   *    ",
        "  *   * ",
        " ****** ",
        "        " ]
    three = [
        "  ****  ",
        " *    * ",
        "      * ",
        "   ***  ",
        "      * ",
        " *    * ",
        "  **** ",
        "        " ]
    four = [
        "    **  ",
        "   * *  ",
        "  *  *  ",
        " ****** ",
        "     *  ",
        "     *  ",
        "    *** ",
        "        " ]
    five = [
        " ****** ",
        " *      ",
        " *      ",
        "  ****  ",
        "      * ",
        " *    * ",
        "  ****  ",
        "        " ]
    six = [
        "   **** ",
        "  *     ",
        " *      ",
        " *****  ",
        " *    * ",
        " *    * ",
        "  ****  ",
        "        " ]
    seven = [
        " ****** ",
        " *    * ",
        "     *  ",
        "    *   ",
        "   *    ",
        "  *     ",
        "  *     ",
        "        " ]
    eigth = [
        "  ****  ",
        " *    * ",
        " *    * ",
        "  ****  ",
        " *    * ",
        " *    * ",
        "  ****  ",
        "        " ]
    nine = [
        "  ****  ",
        " *    * ",
        " *    * ",
        "  ***** ",
        "      * ",
        "     *  ",
        "   **   ",
        "        " ]

    numbers = [ zero, one, two, three, four, five, six, seven, eigth, nine ]

    myNum = str(num)
    for i in range(8):
        for j in range(len(myNum)):
            print numbers[int(myNum[j])][i],
        print

import sys

showNumber(sys.argv[1])
