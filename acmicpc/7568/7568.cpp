#include <iostream>
#include <vector>
#include <string>

#define SWAP(X, Y) { auto tmp = X; X = Y; Y = tmp; }

using namespace std;

typedef struct __PERSON__ {
    int idx = 0, weight = 0, height = 0, order = 1;
} Person;

void printOrder(vector<Person> v) {
    for (auto p : v) cout << p.order << " ";
    cout << endl;
}

string toString(Person person) {
    return to_string(person.weight) + " " + to_string(person.height);
}

void printVector(vector<Person> v) {
    cout << "===============" << endl;
    for (auto item : v) cout << toString(item) << endl;
    cout << "===============" << endl;
}

vector<Person> sortByWeight(vector<Person> v) {
    int n = v.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (v[i].weight < v[j].weight) {
                SWAP(v[i], v[j]);
            }
        }
    }
    return v;
}

vector<Person> sortByIndex(vector<Person> v) {
    int n = v.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (v[i].idx > v[j].idx) {
                SWAP(v[i], v[j]);
            }
        }
    }
    return v;
}

// reutrn true in the case only when the order has to be updated. 
bool check(Person prev, Person cur) { // suppose that the prev preson is heavier than the current person
    return (prev.weight > cur.weight) && (prev.height > cur.height);
}

int main(void) {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<Person> v;
    for (int i = 0; i < N; i++) {
        Person p;
        cin >> p.weight >> p.height;
        p.idx = i;
        v.push_back(p);
    }

    v = sortByWeight(v);
    // printVector(v);
    
    int curOrder = 1;
    for (int i = 1; i < N; i++) {
        auto cur = v[i], prev = v[i - 1];
        curOrder++;
        if (check(prev, cur)) v[i].order = curOrder;
        else v[i].order = prev.order;
    }

    v = sortByIndex(v);
    printOrder(v);

    return 0;
}
