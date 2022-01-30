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
	int *primes = sieve(2000000);
	unsigned long s = 0;
	for (int i = 0; i < len; ++i) {
		s += *(primes + i);
	}
	printf("sum: %lu\n", s);

	return 0;
}
