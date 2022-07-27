#include <iostream>

#define endl "\n"

using namespace std;

size_t dp[1000005] = {1, 1, 2, 6, 24, 120}; // dp[n] = n!

/**
 * @param n at which factorial number to get
 * @return nth factorial number. That is, this function returns n!
 */
size_t factorial(int n) {
    if (dp[n] == 0) dp[n] = n * factorial(n - 1);
    return dp[n];
}

size_t solution(int N) {
    if (N <= 3) return N;
    size_t ans = 0;
    int maxN = (int) N / 2;
    for (int i = 0; i <= maxN; i++) {
        ans += factorial(N - i) / (factorial(N - i * 2) * factorial(i));
    }
    return ans;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // int N;
    // cin >> N;
    // cout << solution(N) % 15746 << endl;

    for (int i = 1; i <= 100; i++) {
        cout << i << " : " << solution(i) << endl;
    }

    return 0;
}
