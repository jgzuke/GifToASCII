#include <iostream>
#include <string>
#include <cassert>
using namespace std;

struct NodeChunk{
    string* val;
    NodeChunk* next;
};

struct Stack{
    int chunkSize;
    int topElt;
    NodeChunk* firstChunk;
};


NodeChunk* createNewNodeChunk (int N) {
    NodeChunk* chunk = new NodeChunk;
    string *values = NULL;
    values = new string[N];
    chunk->val = values;
    chunk->next = nullptr;
    return chunk;
}

void initStack (int chunkSize, Stack& s) {
    s.chunkSize = chunkSize;
    s.topElt = 0;
    s.firstChunk = createNewNodeChunk(chunkSize);
}

bool isEmpty (const Stack& s) {
    return s.firstChunk == nullptr;
}

void push (string val, Stack& s) {
    if(s.topElt < s.chunkSize) // add to current chunk
    {
        s.firstChunk->val[s.topElt] = val;
        s.topElt ++;
    } else
    {
        NodeChunk* newChunk = createNewNodeChunk (s.chunkSize);
        newChunk->next = s.firstChunk;
        newChunk->val[0] = val;
        s.firstChunk = newChunk;
        s.topElt = 1;
    }
}

void pop (Stack& s) {
    assert (!isEmpty(s));
    if(s.topElt < 2)
    {
        NodeChunk* temp = s.firstChunk->next;
        delete[] s.firstChunk->val;
        delete s.firstChunk;
        s.firstChunk = temp;
        s.topElt = s.chunkSize;
    } else
    {
        s.firstChunk->val[s.topElt-1] = "";
        s.topElt -= 1;
    }
}

string top (const Stack& s) {
    assert (!isEmpty(s));
    return s.firstChunk->val[s.topElt-1];
}

int size (const Stack& s) {
    if (isEmpty(s)) return 0;
    int myCount = 0;
    NodeChunk* traveler = s.firstChunk;
    while (traveler)
    {
        myCount ++;
        traveler = traveler->next;
    }
    return (myCount-1) * (s.chunkSize) + s.topElt;
}

void swap (Stack& s) {
    assert (size(s) > 1);
    string temp = s.firstChunk->val[s.topElt-1];
    if(s.topElt < 2)
    {
        s.firstChunk->val[s.topElt-1] = s.firstChunk->next->val[s.chunkSize-1];
        s.firstChunk->next->val[s.chunkSize-1] = temp;
    } else
    {
        s.firstChunk->val[s.topElt-1] = s.firstChunk->val[s.topElt-2];
        s.firstChunk->val[s.topElt-2] = temp;
    }
}

void print (Stack& s)
{
    assert (!isEmpty(s));
    int index = s.topElt - 1;
    NodeChunk* traveler = s.firstChunk;
    while(traveler)
    {
        cout << traveler->val[index] + " ";
        index --;
        if(index < 0)
        {
            traveler = traveler->next;
            index = s.chunkSize-1;
        }
    }
    cout << endl;
}







int main (int argc, char* argv[]) {
    Stack s;
    initStack(5, s);
    push("test1", s);
    push("test2", s);
    push("test3", s);
    print(s);
    cout << "size";
    cout << size(s) << endl;
    push("test4", s);
    push("test5", s);
    push("test6", s);
    push("test7", s);
    push("test8", s);
    push("test9", s);
    push("test10", s);
    push("test11", s);
    push("test12", s);
    swap(s);
    print(s);
    cout << "size";
    cout << size(s) << endl;
    swap(s);
    print(s);
    cout << top(s) << endl;
    pop(s);
    print(s);
    pop(s);
    print(s);
    cout << "size";
    cout << size(s) << endl;
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    cout << "size";
    cout << size(s) << endl;
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    cout << "size";
    cout << size(s) << endl;
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
    pop(s);
    print(s);
}