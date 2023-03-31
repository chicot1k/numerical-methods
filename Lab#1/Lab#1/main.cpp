//
//  main.cpp
//  Lab#1
//
//  Created by Alex on 22.05.2021.
//

#include <iostream>
#include <cmath>
using namespace std;
const double epsilon = 0.0001;

 double f(double x)
{
     return cos(x*x)-10*x;
};

int main()
{
    double intstart, intend,x0,x1,iter;
    
    cin >> intstart;
    cin >> intend;

    x1=(intend+intstart)/2;
    while (abs(x0-x1)>epsilon) {
        cout<<x1<<"\n";
        x0=x1;
        x1=f(x0);
        iter=iter+1;
    }
    cout<<x1;
    cout<<iter;
               
    
    
}

