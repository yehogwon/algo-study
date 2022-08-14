// solved
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

#define endl "\n"

using namespace std;

vector<int> v; // If I put v as a parameter, not as a global variable, it'll be duplicated over again, which is gonna cause a loss of both time and space. So, I decided to declare as a global variable.

int find(int target, int s, int e) {
    if (s > e) return 0;

    int mid = (s + e) / 2;
    int val = v[mid];

    if (val == target) return 1;
    else if (target < val) return find(target, s, mid - 1);
    else return find(target, mid + 1, e);
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) {
        int tmp;
        scanf("%d", &tmp);
        v.push_back(tmp);
    }

    sort(v.begin(), v.end());
    
    int M;
    scanf("%d", &M);

    vector<int> t;
    for (int i = 0; i < M; i++) {
        int target;
        scanf("%d", &target);
        t.push_back(target);
    }

    for (int item : t) {
        printf("%d \n", find(item, 0, N - 1));
    }

    return 0;
}
