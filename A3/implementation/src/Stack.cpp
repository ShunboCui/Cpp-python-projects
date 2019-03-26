// Implementation here
#include "Stack.h"
#include "CardTypes.h"

#include <algorithm>
#include <iostream>
#include <vector>
#include <stdexcept>

using std::vector;


template <class T>
Stack<T>::Stack(vector<T> s){
	this->s = s;
}

template <class T>
Stack<T> Stack<T>::push(T t){
	s.push_back(t);
	Stack newstack(s);
    return newstack;
}

template <class T>
Stack<T> Stack<T>::pop(){
	if (s.size() == 0) {
		throw std::out_of_range("Stack is empty");
	}
	s.pop_back();
	Stack newstack(s);
    return newstack;
}

template <class T>
T Stack<T>::top(){
	if (s.size() == 0) {
		throw std::out_of_range("Stack is empty");
	}
    return s.back();
}


template <class T>
unsigned int Stack<T>::size(){
    return s.size();
}

template <class T>
vector<T> Stack<T>::toSeq(){
    return s;
}
// Keep this at bottom
template class Stack<CardT>;

