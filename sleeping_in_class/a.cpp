#include <iostream>
#include <vector>

using namespace std;

int solve()
{
  int N; cin >> N;
  vector<int> arr;
  for (int i = 0; i < N; i++) 
  {
    int num; cin >> num; arr.push_back(num); 
  }
  int key = 0;
  int _min = N-1; 
  for (int i = 0; i < N; i++) 
  {
    key += arr[i];
    int num_c_op = 0;
    bool ok = true;
    int r_sum = 0; 
    for (int j = i+1; j < N; j++) 
    {
      r_sum += arr[j];
      if (key < r_sum)
      {
        ok = false;
        break;
      }
      else if (key > r_sum)
      {
        num_c_op += 1;
      }
      else if (key == r_sum)
      {
        r_sum = 0;
      }
    }
    if (ok)
    {
      if (num_c_op + i < _min)
      {
        _min = num_c_op + i;
      }
    }
  }
  return _min; 
}

int main() 
{
  int T; cin >> T;
  for (int i = 0; i < T; i++)
  {
    cout << solve() << endl; 
  }
}
