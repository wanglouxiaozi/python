#include <iostream>

using namespace std;

class T
{
	public:
		int num = 10;
};

int main()
{
	T t1;
	t1.num = 1;
	cout << "t1.num = " << t1.num << endl;
	T t2;
	cout << "t2.num = " << t2.num << endl;
}
