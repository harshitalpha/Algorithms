#include<bits/stdc++.h>
#include<stdio.h>

using namespace std;

bool odd_even_ones(unsigned int n) 
{ 
    unsigned int count = 0; 
    while (n) { 
        count += n & 1; 
        n >>= 1; 
    } 
    if(count%2 == 0)
        return 1;
    else
        return 0;    
}



int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,q;
        scanf("%d %d ",&n,&q);

        unsigned int arr[n];

        int odd_count = 0;
        int eve_count = 0;

        for(int i = 0;i<n;i++)
        {
            scanf("%u ",&arr[i]);
            if(odd_even_ones(arr[i]))
            {
                eve_count++;
            }
            else
            {
                odd_count++;
            }
        }

        while(q--)
        {
            unsigned int p;
            scanf("%u ",&p);
            bool px = odd_even_ones(p);

            if(!px)
            {
                printf("%d %d\n",odd_count,eve_count);               
            }
            else
            {
                printf("%d %d\n",eve_count,odd_count);                
            }
            
        }
    }
}