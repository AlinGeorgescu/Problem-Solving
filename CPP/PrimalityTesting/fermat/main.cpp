/**
 * Copyright 2018 Alin-Andrei Georgescu (alinandrei2007@yahoo.com)
 * Grupa: 325 CA
 * Tema AA - Identificarea Numerelor Prime
 */

#include <iostream>
#include <vector>
#include <time.h>
#include "algo.h"

using std::cin;
using std::cout;

/**
 * Functia main cu care am testat codul.
 */
int main() {
    clock_t start, end;
    double cpu_time_used;
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }

    start = clock();
    v = filter_non_prime(v);
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    
    cout << "Numar numere prime: "<< v.size()      << "\n";
    cout << "Timp rulare: "       << cpu_time_used << "\n";
    if (!v.size()) {
        cout << "NICIUN NUMAR PRIM";
    }

    for (int i : v)
        cout << i << " ";

    cout << "\n";

    return 0;
}
