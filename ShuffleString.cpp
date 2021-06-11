#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;


int main(void){
    int arr[8];
    int sample[8] = {4,2,7,5,3,6,1,0};
    char ch;
    string encrypted("ceeotdel");
    for(int i=0; i<8; i++){
        
        ch = encrypted.at(i);
        cout << ch << " ";

    }

    // for(int k =0; k<10;k++){
    //     // printf("Hello World");
    //     printf("%d\n",arr[k]);
    // }
    return 0;
}