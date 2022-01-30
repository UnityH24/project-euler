#include <stdio.h>

int num_factors(int n) {
	int factors = 0;
	for (int i = 1; i <= n; ++i) {
		if (n % i == 0) {
			factors++;
		}
	}
	return factors;
}

int main() {
	int curr = 12000;	
	int curr_triangle = 72006000;
	while (num_factors(curr_triangle) <= 500) {
		printf("%d %d\n", curr, curr_triangle);
		curr_triangle += ++curr;
	}
	printf("result: %d\n", curr_triangle);

	return 0;
}
