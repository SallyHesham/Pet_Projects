#include "Random_Chooser.h"
#include <stdlib.h>
#include <time.h>

template<typename T>
Random_Chooser<T> Random_Chooser<T>::get_chooser()
{
	if (!R) R = new Random_Chooser();
	return R;
}

template<typename T>
void Random_Chooser<T>::set_list(vector<T> l)
{
	list = l;
	end = l.size();
	return;
}

template<typename T>
T Random_Chooser<T>::choose_next()
{
	if (end == 0) {
		end--; return list[0];
	}
	else if (end < 0) return nullptr;
	T chosen;
	srand(time(NULL));
	int n = rand() % end;
	chosen = list[n];
	list[n] = list[end];
	end--;
	return chosen;
}