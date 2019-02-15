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
 * Spune daca a este martor al proprietatii de numar prim sau de numar compus a
 * lui n.
 * 
 * Calculeaza (a ^ (n - 1)) % n si cauta radacini patrate ale unitatii modulo
 * n.
 * 
 * @param a baza testarii primalitatii
 * @param n numarul de cercetat
 * @return true daca numarul este probabil prim
 *         false daca este compus
 */
bool witness(int a, int n) {
    int u = n - 1;
    int t = 0;

    // Determina t >= 1 si u impar astfel incat n - 1 = (2 ^ t) * u.
    while (!(u & 1)) {
        u >>= 1;
        ++t;
    }

    long long last_x = modular_exponentiation(a, u, n);

    for (int i = 0; i < t; ++i) {
        long long current_x = (last_x * last_x) % n;

        if (current_x == 1 && last_x != 1 && last_x != n - 1) {
            return false;
        }

        last_x = current_x;
    }

    if (last_x != 1) {
        return false;
    }

    return true;
}

/**
 * Testarea primalitatii unui numar cu algoritmul Miller-Rabin.
 * 
 * @param n numarul a carui primalitate o testam
 * @param s numarul de posibile iteratii
 * @return true daca numarul este prim
 *         false altfel
 */
bool miller_rabin(const int n, const int s) {
    // Caz testare 2 sau 3
    if (n == 2 || n == 3) {
        return true;
    }

    // Caz testare 1, 4 sau numere pare
    if (n <= 4 || !(n % 2)) {
        return false;
    }

    // Initializare dispozitiv creare numere aleatoare.
    random_device rd;
    mt19937 mt(rd());
    uniform_int_distribution<int> dist(2, n - 1);

    for (int i = 0; i < s; ++i) {
        int a = dist(mt);
        if (witness(a, n) == false) {
            return false;       // este compus
        }
    }

    return true;                // este cel mai probabil prim
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

    for (int i : sequence) {
        if (miller_rabin(i, S)) {
            primes.push_back(i);
        }
    }

    return primes;
}
