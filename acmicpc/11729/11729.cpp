// solved
#include <iostream>

using namespace std;

int printed;

int pow(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

void hanoi(int n, int start, int end) {
    if (n == 1) {
        cout << start << " " << end << "\n";
        return;
    }

    hanoi(n - 1, start, 6 - (start + end));
    hanoi(1, start, end);
    hanoi(n - 1, 6 - (start + end), end);
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    cout << pow(2, N) - 1 << endl;
    hanoi(N, 1, 3);

    return 0;
}
