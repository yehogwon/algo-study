#include <iomanip>
#include <iostream>

#define PI 3.14159265358979323846

using namespace std;

double squared(int x) {
    return x * x;
}

int main(void) {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    cout << fixed;
    cout << setprecision(10);

    int r;
    cin >> r;

    cout << PI * squared(r) << endl << 2 * squared(r) << endl;
}
