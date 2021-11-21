#include <Primitives.h>
#include <string>

using namespace std;

class Dendrite
{
private:
    string getID();
public:
    Dendrite(Neuron neuron);
    string ID;
    ~Dendrite();
};

Dendrite::Dendrite(Neuron neuron)
{
    void assignID() {
        ID = neuron.getID();
    };
    void addSynapse(Synapse synapse) {
        
    };

}

Dendrite::~Dendrite()
{
}
