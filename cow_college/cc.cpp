#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

int main ()
{
  int n; cin >> n;
  long long max_T[n];

  for (int i = 0; i < n; i++)
  {
    cin >> max_T[i];
  }

  sort(max_T, max_T+n);

  int n_attend = n;
  long long m_profit = 0, m_tuition = 0;
  for (int i = 0; i < n; i++)
  {
    long long p_i_cow = max_T[i]*n_attend;
    if (m_profit < p_i_cow)
    {
      m_profit = p_i_cow;
      m_tuition = max_T[i];
    }
    n_attend--;
  }
  cout << m_profit << " " << m_tuition << "\n";
  return 0;
}
