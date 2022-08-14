// solved
#include <iostream>

#define endl "\n"
#define mod 15746

using namespace std;

size_t dp[10000000] = {0, 1, 1, };

size_t fibo(int n) {
    if (dp[n] == 0) dp[n] = (fibo(n - 1) + fibo(n - 2)) % mod;
    return dp[n];
}

size_t solution(int N) {
    if (N <= 3) return N;
    return fibo(N + 1);
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    cout << solution(N) << endl;

    return 0;
}
