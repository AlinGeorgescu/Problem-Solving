// Problem        : Passport Control
// Queues management
// Language       : C++11
// Compiled Using : g++

#include <iostream>
#include <climits>

using namespace std;

int main() {
    int N, M, size;
    int *numPass;
    int *groupCount;
    int min;
    int freeBooth;
    
    cin >> N >> M;
    numPass = new int[N];
    groupCount = new int[N];

    for (int i = 0; i < N; ++i) {
        groupCount[i] = 0;
    }

    for (int i = 0; i < M; ++i) {
        cin >> size;
        min = INT_MAX;

        for (int j = 0; j < N; ++j) {
            if (numPass[j] < min) {
                min = numPass[j];
                freeBooth = j;
            }
        }

        numPass[freeBooth] += size;
        ++groupCount[freeBooth];

        if (!(groupCount[freeBooth] % 10)) {
            numPass[freeBooth] += 5;
        }
    }
    
    for (int i = 0; i < N; ++i) {
        cout << groupCount[i] << " ";
    }
    
    delete[] numPass;
    delete[] groupCount;
    return 0;
}
