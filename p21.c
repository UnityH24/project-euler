#include <stdio.h>

int d(int n) {
	int s = 1;
	for (int i = 2; i < n; ++i) {
		if (n % i == 0) {
			s += i;
		}
	}
	return s;
}

int main() {
	int ans = 0;
	int b;
	for (int a = 1; a < 10000; ++a) {
		b = d(a);
		if (d(b) == a && a != b) {
			ans += a;
		}
	}
	printf("%d\n", ans);
}
