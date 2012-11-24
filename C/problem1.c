#include <stdlib.h>
#include <stdio.h>

int mod_three_or_five(int num)
{
    if (num % 3 || num % 5) return num;
    return 0;
}

int main() 
{
    int total = 0;
    int start = 0;
    while(start < 1000) {
        total += mod_three_or_five(start);
        start++;
    }
    printf("%d\n", total);

}
