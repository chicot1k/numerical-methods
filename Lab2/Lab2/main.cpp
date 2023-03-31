//
//  main.cpp
//  Lab2
//
//  Created by Alex on 04.06.2021.
//


#include <iostream>
#include <cmath>
using namespace std;
const double epsilon = 0.0001;

 double f(double x)
{
     
    return tan(x) - 1/x;
};

int main()
{
    double intstart, intend,x1,x2,delta;
    delta = 0.000001;
    cin >> intstart;
    cin >> intend;
    
    while (intend - intstart > epsilon)
    {
        x1 = (intstart + intend) / 2 -  delta;
        x2 = (intstart + intend) / 2 + delta;
        if (f(x1) > f(x2))
            intstart = x1;
        else
            intend =x2;
        cout << "(" << (intstart + intend) / 2 << ";" << f((intstart + intend) / 2) << ")";
    };
    cout <<"("<<(intstart + intend) / 2 << ";" << f((intstart + intend) / 2) << ")";
    
}
 
