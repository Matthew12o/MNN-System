#include <Primitives.h>
#include <string>

using namespace std;

class Neuron
{
private:
    /* data */
public:
    Neuron(string id, Environment environment, double threshold=1.0);
    ~Neuron();
    string getID();
};

Neuron::Neuron(string id, Environment environment, double threshold=1.0)
{
    string getID() {
        return id;
    };
    
}

Neuron::~Neuron()
{
}
