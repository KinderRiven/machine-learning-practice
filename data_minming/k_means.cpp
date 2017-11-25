#include <bits/stdc++.h>
using namespace std;
double log2(double x) {
    return log(x) / log(2);
}
struct point {
    double x, y, z;
    point(double x, double y, double z):
        x(x), y(y), z(z){};
};
vector<point> points, center;
vector<point> group[10];
double dist(point a, point b) {
    return 1.0 * sqrt((a.x - b.x) * (a.x - b.x) + \
                      (a.y - b.y) * (a.y - b.y) + \
                      (a.z - b.z) * (a.z - b.z));
}
void k_means() {
    for(int t = 0; t < 10; t++) {
        for(int i = 0; i < center.size(); i++) {
            //printf("[%d]:(%lf, %lf, %lf)\n", i, center[i]);
            group[i].clear();
        }
        for(int i = 0; i < points.size(); i++) {
            double min_dist = dist(center[0], points[i]);
            int index = 0;
            for(int j = 1; j < center.size(); j++) {
                double tmp_dist = dist(center[j], points[i]);
                if(tmp_dist < min_dist) {
                    min_dist = tmp_dist;
                    index = j;
                }
            }
            group[index].push_back(points[i]);
            //printf("[%d]->%d:%lf\n", i, index, min_dist);
        }
        for(int i = 0; i < center.size(); i++) {
            double x = 0, y = 0, z = 0;
            int num = 0;
            for(int j = 0; j < group[i].size(); j++) {
                x += group[i][j].x;
                y += group[i][j].y;
                z += group[i][j].z;
                num ++;
            }
            center[i] = point(x/num, y/num, z/num);
            //printf("%d:%lf %lf %lf\n", i, x/num, y/num, z/num);
        }
    }
    for(int i = 0; i < center.size(); i++) {
        printf("[%d](%lf, %lf, %lf):\n", i, center[i].x, center[i].y, center[i].z);
        for(int j = 0; j < group[i].size(); j++) {
            printf("(%lf, %lf, %lf) ", \
                   group[i][j].x, group[i][j].y, group[i][j].z);
        }
        printf("\n");
    }
}
int main() {
    double x, y, z;
    while(scanf("%lf %lf %lf", &x, &y, &z) != EOF) {
        points.push_back(point(x, y, z));
    }
    while(scanf("%lf %lf %lf", &x, &y, &z) != EOF) {
        center.push_back(point(x, y, z));
    }
    k_means();
    return 0;
}
/*
4 2 5
10 5 2
5 8 7
1 1 1
2 3 2
3 6 9
11 9 2
1 4 6
9 1 7
5 6 7
*/
