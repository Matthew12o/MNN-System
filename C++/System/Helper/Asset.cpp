#include <iostream>
#include <time.h>
#include <string>

using namespace std;

class Price {
    static const string ID;
    static const time_t time;
    static const float Ask, Bid, Last, Mid;   
    
    public:
        Price(string ID, time_t time, float Ask=NULL, float Bid=NULL, float Last=NULL, float Mid=NULL);
        Price(string ID, float Ask=NULL, float Bid=NULL, float Last=NULL, float Mid=NULL) : Price(string ID, time(0),float Ask=NULL, float Bid=NULL, float Last=NULL, float Mid=NULL);
};

class Position {
    const *
};

class Trade {
    static const string ID;
    static const string Side;
    static const bool isLong;
    static const
};
class Security {
    static const string ID;
    Price Prices [] = {};
    Trade Trades [] = {};
};