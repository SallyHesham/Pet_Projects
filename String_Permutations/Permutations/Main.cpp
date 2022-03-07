#include<iostream>
#include<string>
#include"permutation.h"
using namespace std;

int main()
{
	while (true)
	{
		string word = "";
		cin >> word;
		permutation::permutate(word, cout);
		system("pause");
	}
	return 0;
}