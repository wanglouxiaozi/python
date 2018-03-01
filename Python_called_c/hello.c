#include<stdio.h>
#include<string.h>

int main(int argc, char **argv)
{
	char str[20];
	strcpy(str, argv[1]);
	printf("This is c program entrance!\n");
	printf("**********************************\n");
	printf("your name:");
	printf("%s\n", str);
	return 0;
}
