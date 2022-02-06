#pragma once
#include<iostream>
#include<stack>
#include<queue>
#include<string>
using namespace std;

class permutation
{
public:
	static void permutate(string word, ostream& stream);
private:
	static void sub_per(queue<char>& lettersQ, stack<char>& takenStk, string& word, int n, ostream& stream);
};

