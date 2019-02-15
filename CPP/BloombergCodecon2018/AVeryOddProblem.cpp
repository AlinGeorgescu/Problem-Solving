// Problem        : A Very Odd Problem
// Tell if an array can have a non-zero even number of even numbers.
// Language       : C++11
// Compiled Using : g++
// Version        : GCC 4.9.1

#include <iostream>

using std::cin;
using std::cout;

void isSafe(int n, int numOdds) {
    if (n - numOdds >= 2) {
        cout << "YES\n";
        return;
    }
    
    cout << "NO\n";
}

int main() {
    int n, x;
    int numOdds = 0;
    
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (x % 2) {
            ++numOdds;
        }
    }
    
    isSafe(n, numOdds);

    return 0;
}
