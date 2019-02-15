/**
 * Copyright 2018 Alin-Andrei Georgescu (alinandrei2007@yahoo.com)
 * Grupa: 325 CA
 * Tema AA - Identificarea Numerelor Prime
 */

#include <iostream>
#include <cmath>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

int main() {
    int n, x;
    vector<int> primes;

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x;

        if (x < 2) {
            continue;
        }

        if (x == 2) {
            primes.push_back(x);
            continue;
        }

        if (!(x % 2)) {
            continue;
        }

        bool prime = true;
        for (int j = 3; j <= sqrt(x); j += 2) {
            if (!(x % j)) {
                prime = false;
                break;
            }
        }

        if (prime) {
            primes.push_back(x);
        }
    }

    cout << primes.size() << '\n';
    if (!primes.size()) {
        cout << "NICIUN NUMAR PRIM\n";
    } else {
        for (int i : primes) {
            cout << i << " ";
        }

        cout << '\n';
    }

    return 0;
}