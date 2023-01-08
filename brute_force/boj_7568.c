#include<stdio.h>
int main()
{
    int arr[50][2] = { 0 };
    int n, a, b;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &a, &b);
        arr[i][0] = a;
        arr[i][1] = b;
    }
    for (int j = 0; j < n; j++)
    {
        int k = 1;
        for (int p = 0; p < n; p++)
        {
            if ((arr[j][0] < arr[p][0]) && (arr[j][1] < arr[p][1])) {
                k++;
            }
        }
        printf("%d ", k);
    }
    return 0;

}