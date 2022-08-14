// solved
#include <iostream>

#define endl "\n"

using namespace std;

size_t fibo(int n) {
    size_t fibo[100] = {0, 1, 1, 0, }; // fibo[n] = nth fibonacci sequence
    for (int i = 3; i <= n; i++)
        fibo[i] = fibo[i - 2] + fibo[i - 1];
    return fibo[n];
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    cout << fibo(N) << " " << N - 2 << endl;

    return 0;
}
