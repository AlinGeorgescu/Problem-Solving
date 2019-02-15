/**
 * Copyright 2018 Alin-Andrei Georgescu (alinandrei2007@yahoo.com)
 * Grupa: 325 CA
 * Tema AA - Identificarea Numerelor Prime
 */

#include "algo.h"

#define S 3     // Numarul de iteratii

/**
 * Calculez (base ^ exponent) % mod
 * 
 * Parametrii de tip long long deoarece inmultirea poate da overflow.
 * 
 * @param base baza operatiei
 * @param exponent puterea
 * @param mod numarul cu care se realizeaza modulo
 */
int modular_exponentiation(long long base, long long exponent, long long mod) {
    long long res = 1;

    while (exponent > 0) {
        // Daca exponentul este impar, se inmulteste rezultatul cu a.
        if (exponent & 1)
            res = (res * base) % mod;

        // exponentul trebuie sa fie par acum
        exponent = exponent >> 1;
        base = (base * base) % mod;
    }

    return res % mod;
}


/**
 * Pentru o secventa de numere, elimina din ea numerele compuse.
 *
 * @param sequence   secventa de numere citita
 * @return vectorul cu numerele prime din secventa initiala, asezate in
 * ordinea din secventa
 */
vector<int> filter_non_prime(const vector<int>& sequence) {
    vector<int> primes;
    random_device rd;
	mt19937 mt(rd());

    for (int n : sequence) {
        if (n == 2 || n == 3) {
            primes.push_back(n);
        } else if ((n > 3) && !(n & 1)) {
            continue;
        } else if (n > 3) {
            bool composite = false;
            uniform_int_distribution<int> dist(2, n - 1);

            for (int j = 0; j < S; ++j) {
                int random_base = dist(mt);
                int mod = modular_exponentiation(random_base, n - 1, n);

                if (mod != 1) {
                    composite = true;
                    break;
                }
            }

            if (!composite) {
                primes.push_back(n);
            }
        }
    }

    return primes;
}
