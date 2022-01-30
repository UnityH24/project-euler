#include <stdio.h>
#define ulli unsigned long long int

ulli fact(int n) {
	ulli  result = 1;
	for (int i = n; i > 1; result *= i--);
	return result;
}

ulli count_paths(size_t size) {
	ulli top = fact(size + size);
	printf("top: %llu\n", top);
	ulli btm = fact(size) * fact(size);
	printf("btm: %llu\n", btm);
	return top / btm;
}

int main(int argc, char **argv) {
	ulli ans = count_paths(20);
	printf("%llu\n", ans);
	return 0;
}
