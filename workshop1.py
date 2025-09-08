#include <iostream>
#include <ctime>
using namespace std;

int main() {
    int year, month, day, hour, addHour;
    cout << "현재 연, 월, 일, 시 입력 (예: 2024 4 19 15): ";
    cin >> year >> month >> day >> hour;

    cout << "추가할 시간 입력: ";
    cin >> addHour;

    // tm 구조체 생성
    tm t = {};
    t.tm_year = year - 1900; // tm_year는 1900년 기준
    t.tm_mon = month - 1;    // 0부터 시작
    t.tm_mday = day;
    t.tm_hour = hour;

    // time_t 변환 후 시간 추가
    time_t now = mktime(&t);
    now += addHour * 3600;   // 입력한 시간(초 단위)

    // 다시 구조체로 변환
    tm *newTime = localtime(&now);

    cout << "결과: " 
         << newTime->tm_year + 1900 << "년 "
         << newTime->tm_mon + 1 << "월 "
         << newTime->tm_mday << "일 "
         << newTime->tm_hour << "시" << endl;

    return 0;
}
