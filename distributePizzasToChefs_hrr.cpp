#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;


int getMinTime(int r[], int start, int nc, int np, int dp[][1005])  {
    if(np == 0)
        return 0;
    if(start == nc) {
        return np == 0 ? 0 : INT_MAX;
    }
    if(dp[start][np] != -1)
        return dp[start][np];
    int minTime = INT_MAX;
    for(int i=np / (nc - start +1); i<=np; i++)    {
        int curChefTime = r[start] * (i * i - i + 1);
        int curTime = max(curChefTime, getMinTime(r, start + 1, nc, np - i, dp));
        minTime = min(minTime, curTime);
    }
    dp[start][np] = minTime;
    return minTime;
}

int main() {
    int t;
    cin>>t;
    while(t-- > 0)  {
        int np, nc;
        cin>>np>>nc;
        int r[nc];
        for(int i=0; i<nc; i++)
            cin>>r[i];
        int dp[1005][1005];
        for(int i=0; i<=nc; i++)
            for(int j=0; j<=np; j++)
                dp[i][j] = -1;
        sort(r, r+nc);
        cout << getMinTime(r, 0, nc, np, dp) << endl;
    }
    return 0;
}