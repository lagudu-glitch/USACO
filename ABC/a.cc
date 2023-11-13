#include <iostream>
#include <algorithm>

int main ()
{
  int ABC[7];
  
  // get the file inputs
  for (int i=0; i<7; i++)
  {
    std::cin >> ABC[i];
  }

  // sort the inputs
  std::sort(ABC, ABC+7);

  std::cout << ABC[0] << " " << ABC[1] << " " << ABC[6]-(ABC[0]+ABC[1]) << std::endl;
}

