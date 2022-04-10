#pragma once
#include<vector>
using namespace std;

template<typename T>
class Random_Chooser
{
private:
	vector<T> list;
	int end;
	static Random_Chooser R;
	Random_Chooser();
public:
	static Random_Chooser get_chooser();
	void set_list(vector<T> l);
	T choose_next();

};