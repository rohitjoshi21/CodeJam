'''
Question 2
Synchronous Shopping
Link: https://www.hackerrank.com/contests/w20/challenges/synchronous-shopping
'''

#include <bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define mp make_pair

const int MAX_MASK = 1024, MAXN = 1010, INF = 1E9;
int n, m, k;
int d[MAXN][MAX_MASK], msk[MAXN];
vector< pair<int, int> > go[MAXN];
set< pair<int, pair<int, int> > > s;

int main() {
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 1; i <= n; i++) {
        int t;
        scanf("%d", &t);
        for (int j = 0; j < t; j++) {
            int x;
            scanf("%d", &x);
            x--;
            msk[i] |= (1<<x);
        }
    }
    for (int i = 0; i < m; i++) {
        int aa, bb, cc;
        scanf("%d%d%d", &aa, &bb, &cc);
        assert(1 <= aa && aa <= n);
        assert(1 <= bb && bb <= n);
        assert(aa != bb);
        go[aa].push_back( mp(bb, cc) );
        go[bb].push_back( mp(aa, cc) );
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < MAX_MASK; j++) {
            d[i][j] = INF;
        }
    }
    d[1][ msk[1] ] = 0;
    s.insert( mp(0, mp(1, msk[1]) ) );
    while (!s.empty() ) {
        pair<int, pair<int, int> > cur = *s.begin();
        s.erase(s.begin() );
        int v = cur.Y.X, curmsk = cur.Y.Y, curd = cur.X;
        for (int j = 0; j < go[v].size(); j++) {
            int to = go[v][j].X;
            int cost = go[v][j].Y;
            int tomsk = curmsk | msk[to];
            if (d[to][tomsk] > curd + cost) {
                s.erase( mp(d[to][tomsk], mp(to, tomsk) ) );
                d[to][tomsk] = curd + cost;
                s.insert( mp(d[to][tomsk], mp(to, tomsk) ) );
            }
        }
    }
    int ans = INF;
    for (int i = 0; i < (1<<k); i++) {
        for (int j = 0; j < (1<<k); j++) {
            if ( (i | j) == ( (1<<k) - 1 ) ) {
                ans = min(ans, max(d[n][i], d[n][j]) );
            }
        }
    }
    if (ans == INF) {
        assert(false);
    }
    cout<<ans<<endl;
    return 0;
}