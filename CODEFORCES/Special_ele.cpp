#include<bits/stdc++.h>

using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin >> n;
		int arr[n];
		for(int i = 0;i<n;i++)
		{
			//cout<<"Enter "<<i<<" element:\n";
			cin >> arr[i];
		}
		//cout<<"Hello";
		int mat[n][n];
		
		int exist[n+1];
		
		int i = 0;
		while(i < n+1)
		{
			//cout<<"Hello\n";
			exist[i] = 0;
			i = i + 1;	
		}
		for (int i = 0;i<n+1;i++)
		{
			cout<<exist[i]<<endl;
		}
		for(int i = 0; i < n-1; i++)
			for (int j = i+1 ;j < n ;j++)
			{
				mat[i][j] = mat[i][j-1] + arr[j];
				if (mat[i][j] < n+1)
					exist[mat[i][j]] = 1;
			}	
		
		int count = 0;
		
		for (int i = 0;i<n+1;i++)
		{
			cout<<exist[i]<<endl;
		}
		for(int i = 0;i< n;i++)
		{
			if(exist[arr[i]] == 1)
				count = count + 1;
		}
		cout<<count<<endl;
	}
}
