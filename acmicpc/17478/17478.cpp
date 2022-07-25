#include <iostream>

using namespace std;

const string script[] = {
    "\"재귀함수가 뭔가요?\"", 
    "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.", 
    "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",
    "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
};

void printSpace(int space) {
    for (int i = 0; i < space; i++) cout << "____";
}

void print(int count, int space) {
    if (count == 0) {
        printSpace(space);
        cout << "\"재귀함수가 뭔가요?\"" << endl;
        printSpace(space);
        cout << "\"재귀함수는 자기 자신을 호출하는 함수라네\"" << endl;
        printSpace(space);
        cout << "라고 답변하였지." << endl;

        return;
    }
    for (int i = 0; i < 4; i++) {
        printSpace(space);
        cout << script[i] << endl;
    }

    print(count - 1, space + 1);
    printSpace(space);
    cout << "라고 답변하였지." << endl;
}

int main(void) {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);

    int count;
    cin >> count;
    cout << "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다. " << endl;
    print(count, 0);
}
