// Implementation here
#include "Stack.h"
#include "CardTypes.h"
#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

template <class T>
Stack<T>::Stack(vector<T> s){
  this->s = s;
}

template <class T>
Stack<T> Stack<T>::push(T){
    return Stack(s.push_back(T)) ;
}

template <class T>
Stack<T> Stack<T>::push(T){
    return Stack(s.pop_back()) ;
}

template <class T>
T Stack<T>::top(){
    return s[s.size() - 1];
}


template <class T>
unsigned int Stack<T>::size(){
    return s.size();
}

template <class T>
std::vector<T> Stack<T>::toSeq(){
    return s.size();
}
// Keep this at bottom
template class Stack<CardT>;

