#include "permutation.h"

void permutation::permutate(string word, ostream& stream)
{
	int n = word.length();
	queue<char> lettersQ;
	stack<char> takenStk;
	for (int i = 0; i < n; i++)
	{
		lettersQ.push(word[i]);
	}
	word = "";
	sub_per(lettersQ, takenStk, word, n, stream);
	return;
}

void permutation::sub_per(queue<char>& lettersQ, stack<char>& takenStk, string& word, int n, ostream& stream)
{
	for (int i = 0; i < n; i++)
	{
		word += lettersQ.front();
		takenStk.push(lettersQ.front());
		lettersQ.pop();

		if (n > 1) { sub_per(lettersQ, takenStk, word, n - 1, stream); }
		else { stream << word << endl; }

		word = word.substr(0,word.size()-1);
		lettersQ.push(takenStk.top());
		takenStk.pop();
	}
	return;
}
