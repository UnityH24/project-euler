
#include <stdio.h>
#include <stdlib.h>

static int len = 0;

int *sieve(int limit) {
	int *result = malloc((limit - 2) * sizeof(int));
	char A[limit - 2];
	for (int k = 0; k < limit - 2; ++k) {
		A[k] = 1;
	}
	for (int i = 2; i * i <= limit; ++i) {
		if (A[i - 2]) {
			for (int j = i*i; j <= limit; j += i) {
				A[j-2] = 0;
			}
		}
	}
	int *tmp = result;
	for (int k = 0; k < limit - 2; ++k) {
		if (A[k]) {
			*tmp++ = k + 2;
			len++;
		}
	}
	return result;
}

int main() {
	int *primes = sieve(1000000);
	if (len >= 10001) {
		printf("%i\n", *(primes + 10000));
	}
	return 0;
}
