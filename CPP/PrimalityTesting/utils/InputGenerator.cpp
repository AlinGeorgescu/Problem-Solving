/**
 * Copyright 2018 Alin-Andrei Georgescu (alinandrei2007@yahoo.com)
 * Grupa: 325 CA
 * Tema AA - Identificarea Numerelor Prime
 */

#include <iostream>
#include <set>
#include <random>
#include <limits>

#define NUM 1000000			// Numarul de numere de generat.

using std::set;
using std::random_device;
using std::mt19937;
using std::uniform_int_distribution;
using std::numeric_limits;
using std::cout;

// Genereaza NUM numere prime distincte si intregi (reprezentare pe 32 biti).
int main() {
	random_device rd;
	mt19937 mt(rd());
	uniform_int_distribution<int>
				dist(1, numeric_limits<int>::max());

	set<int> numbers;
	while(numbers.size() < NUM) {
		numbers.insert(dist(mt));
	}

	cout << NUM << "\n";
	for (int i : numbers)
		cout << i << " ";

	return 0;
}
