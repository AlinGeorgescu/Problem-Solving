/**
 * Copyright 2018 Alin-Andrei Georgescu (alinandrei2007@yahoo.com)
 * Grupa: 325 CA
 * Tema AA - Identificarea Numerelor Prime
 */

#ifndef ALGO_H
#define ALGO_H

#include <vector>
#include <cmath>
#include <random>

using std::vector;
using std::random_device;
using std::mt19937;
using std::uniform_int_distribution;

/**
 * Calculez (base ^ exponent) % mod
 * 
 * Parametrii de tip long long deoarece inmultirea poate da overflow.
 * 
 * @param base baza operatiei
 * @param exponent puterea
 * @param mod numarul cu care se realizeaza modulo
 */
int modular_exponentiation(long long base, long long exponent, long long mod);

/**
 * Spune daca a este martor al proprietatii de numar compus al lui n.
 * 
 * Calculeaza (a ^ (n - 1)) % n si cauta radacini patrate ale unitatii modulo
 * n.
 * 
 * @param a baza testarii primalitatii
 * @param n numarul de cercetat
 * @return true daca numarul este probabil prim
 *         false daca este compus
 */
bool witness(int a, int n);

/**
 * Testarea primalitatii unui numar cu algoritmul Miller-Rabin.
 * 
 * @param n numarul a carui primalitate o testam
 * @param s numarul de posibile iteratii
 * @return true daca numarul este prim
 *         false altfel
 */
bool miller_rabin(const int n, const int s);

/**
 * Pentru o secventa de numere, elimina din ea numerele compuse.
 *
 * @param sequence   secventa de numere citita
 * @return vectorul cu numerele prime din secventa initiala, asezate in
 * ordinea din secventa
 */
vector<int> filter_non_prime(const vector<int>& sequence);

#endif
