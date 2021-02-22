#include <iostream>
using namespace std;
int sum() {
	int allNumbers = 0;
	int result;
	int positiveNumbers = 0;
	int negativeNumbers = 0;
	int devisionPositiveNumbers;
	int remainderNegativeNumbers;

	for (int i = -1000; i < 1000; i++) {

		allNumbers = allNumbers + i;

	}
	for (int j = -1000; j < 0; j++) {

		negativeNumbers = negativeNumbers + j;

	}
	for (int k = 1000; k >= 0; k--) {

	positiveNumbers = positiveNumbers + k;

	}
	devisionPositiveNumbers = positiveNumbers / 7;
cout << devisionPositiveNumbers << ", ";

remainderNegativeNumbers = negativeNumbers % 15;
cout << remainderNegativeNumbers << ", ";

	result = negativeNumbers + positiveNumbers;
	cout << result;

	return result;
}
int main()
{
	sum();
}
