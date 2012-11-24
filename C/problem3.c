#include <stdlib.h>
#include <stdio.h>

int main() 
{
    long n = 600851475143;
    long i;
    for (i = 2; i < n; i+=1) {
        while ((n % i) == 0) {
            n = n / i;
        }
    }
    printf("%lu\n", n);
}
