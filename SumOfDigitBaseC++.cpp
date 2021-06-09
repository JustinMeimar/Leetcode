#include <stdio.h>
#include <cmath>
#include <iostream>

using namespace std;

class Solution{
 public:
        int n;
        int k;

        int sumBase(int n, int k){
            int i = 0;

            if (n == 0){
                return 0;
            }
            while (pow(k,i) <= n/k){
                i += 1;
            }

            return 1 + sumBase(n-pow(k,i),k);
        }
};

int main(void){
  
    int fillArr[10] = {34,6,68,2,10,10,128,2,78,3};
    int incr = 2;

    for (int i = 0; i < 10; i+=incr){
        Solution temp;
        printf("sum of digits in n %d as base k: %d\n",
            fillArr[i], 
            temp.sumBase(fillArr[i], fillArr[i+1])
            );
    }

}