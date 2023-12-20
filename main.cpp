#include <iostream>
#include <stdlib.h>
#include <string>

signed int find_location(char* location, char* desert_map)
{
    std::cout << "location is " << location << std::endl;
    return 1;
}

int main(int argc, char const *argv[])
{
    find_location((char*)'A',(char*)'2');
    return EXIT_SUCCESS;
}