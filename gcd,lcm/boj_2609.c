// 재귀함수를 사용하지 않은 코드
#include<stdio.h>
int gcd(int a, int b)
{
	int temp;
	while (b > 0)
	{
		temp = a;
		a = b;
		b = temp%b;
	}
	return a;
}

int main()
{
	int a , b;
	scanf("%d %d", &a, &b);

	printf("%d\n%d",gcd(a,b),(a*b)/gcd(a,b));
	return 0;
}

/*
유클리드 알고리즘에 의해 gcd(A,B)를 하기 위해서 A가 B보다 커야 하지만, 위의 while문에서 A가 B보다 작다면 A,B의 위치가 while문의 코드에 의해 변동 되기에 사전에 A,B의 대소비교
를 통해 위치를 바꿔줄 필요는 없다. 
*/