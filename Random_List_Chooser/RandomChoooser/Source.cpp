#include <iostream>
#include "Random_Chooser.h"

using namespace std;

int main() {
	Random_Chooser<string> chooser = Random_Chooser<string>::get_chooser();
	bool in = true;
	string temp;
	vector<string> v;
	while (in)
	{
		while (true)
		{
			cout << "Input list item / write 'done' when finished:\n";
			try
			{
				cin >> temp;
				if (temp == "done") break;
				v.push_back(temp);
			}
			catch (const std::exception&)
			{
				cout << "Try again.\n";
				continue;
			}

		}
		chooser.set_list(v);
		while (true)
		{
			try
			{
				cout << chooser.choose_next();
			}
			catch (const std::exception&)
			{
				cout << "List finished.";
				break;
			}
		}
	}
}