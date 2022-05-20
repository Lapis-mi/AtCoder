#include<iostream>
using namespace std;
int main()
{
    // 文字列の入力
    string s;
    cin >> s;
    int count = 0;
    // 1文字ずつ操作
    for(int i = 0; i < (int)s.size(); ++i){
      char ch = s[i];
      if (ch == '1'){
        count++;
      }
    }
    // 出力
    cout << count << endl;
    return 0;
}
// g++ -o out abc081_a.cpp
// コンパイルされてoutというファイルが作られる
// ./out