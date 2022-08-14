// solved
#include <iostream>
#include <vector>

#define SWAP(X, Y) { int tmp = X; X = Y; Y = tmp; }

using namespace std;

vector<int> sort(vector<int> v) {
    int n = v.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                SWAP(v[i], v[j]);
            }
        }
    }

    return v;
}

int main(void) {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    int arr[3];
    cin >> arr[0] >> arr[1] >> arr[2];

    vector<int> v(arr, arr + sizeof(int));
    v = sort(v);

    if (v[0] == v[2]) { // all of them are the same
        cout << 10000 + v[0] * 1000 << endl;
    } else if (v[0] == v[1] || v[1] == v[2]) { // two of them are the same
        int same = v[0] == v[1] ? v[1] : v[2];
        cout << 1000 + same * 100 << endl;
    } else { // none of them are the same
        cout << v[2] * 100;
    }
}
