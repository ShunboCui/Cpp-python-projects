/**
 * \file Stack.h
 * \author Shunbo Cui
 * \brief Defines method needed for Stack type.
 */
#ifndef A3_STACK_H_
#define A3_STACK_H_

#include <vector>

template <class T>

/**
 * \brief The class templete of Stack.
 */
class Stack
{
    private:
		/**
		* \brief The input sequence of type T.
		*/
        std::vector<T> s;
    public:
		/**
		* @brief Construct the stack.
		* @param s The input sequence of type T.
		*/
        Stack(std::vector<T> s);

		/**
		* @brief Pushing new element to the stack.
		* @param t The new element to be pushed.
		* @return The new stack after pushing.
		*/
        Stack<T> push(T t);

		/**
		* @brief Pop the last element off from the stack.
		* @return The new stack after popping.
		*/
        Stack<T> pop();

		/**
		* @brief The top element in the stack.
		* @return The top element in the stack.
		*/
        T top();

		/**
		* @brief Getting the size of the stack.
		* @return The size of the stack.
		*/
        unsigned int size();

		/**
		* @brief Putting everything in a stack into a sequence.
		* @return The output sequence.
		*/
        std::vector<T> toSeq();
};
#endif
