#include <iostream>
#include <stdint.h>
#include "mytimer.h"
using namespace std;

int main () {
  uint64_t begin = GetRDTSC();
  uint64_t end = GetRDTSC();

  cout <<end-begin<<endl;
  return 0;
}
