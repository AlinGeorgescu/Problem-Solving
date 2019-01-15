// Problem        : Tracing Vile Angus
// Break a cipher - swap two letters in part of the text from a random position to the end.
// Language       : C++11
// Compiled Using : g++
// Version        : GCC 4.9.1

#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::string;

typedef struct {
    int pos;
    char first, second;
} myStruct;

void decipher(string message, int N) {
    myStruct arr[N];
    
    for (int k = 0; k < N; ++k) {
        cin >> arr[k].pos
            >> arr[k].first
            >> arr[k].second;
    }
    
    for (int k = N - 1; k >= 0; --k) {
        for (int i = arr[k].pos; i < message.length(); ++i) {
            if (message[i] == arr[k].first) {
                message[i] = arr[k].second;
            } else if (message[i] == arr[k].second) {
                message[i] = arr[k].first;
            } else if (('A' <= message[i] && message[i] <= 'Z') && ((message[i] + 'a' - 'A') == arr[k].first)) {
                message[i] = arr[k].second + 'A' - 'a';
            } else if (('A' <= message[i] && message[i] <= 'Z') && ((message[i] + 'a' - 'A') == arr[k].second)) {
                message[i] = arr[k].first + 'A' - 'a';
            }
        }
    }
    
    cout << message << "\n";
}

int main() {
    int N;
    string message;
    
    getline(cin, message);
    if (!message.length()) {
        cout << "\n";
    } else {
        cin >> N;

        if (!N) {
            cout << message << "\n";
        } else {
            decipher(message, N);
        }
    }

    return 0;
}
