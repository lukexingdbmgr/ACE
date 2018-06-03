##http://www.cnblogs.com/grandyang/p/8519566.html

'''
basic graph:
    BFS
    DFS
similar to

the new knowdege is colored;
color is status of each node
https://leetcode.com/problems/number-of-islands/description/

class Solution {
    void DFS(int i, int j, vector<vector<char>>& grid){
        grid[i][j] = 'X';
        if(i-1>=0 && grid[i-1][j] == '1'){
            DFS(i-1, j, grid);
        }
        if (j-1 >= 0 && grid[i][j-1] == '1'){
            DFS(i, j-1, grid);
        }
        if(i + 1 < grid.size() && grid[i+1][j] == '1'){
            DFS( i+ 1, j, grid);
        }
        if (j + 1 < grid[0].size() && grid[i][j+1] == '1'){
            DFS(i, j+ 1, grid);
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        for(int i = 0; i < grid.size(); ++i){
            for(int j = 0; j < grid[0].size(); ++j){
                if(grid[i][j] == '1'){
                    DFS(i, j, grid);
                    res ++;
                }
            }
        }
        return res;
    }
};
'''


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        colors = [0] * len(graph)
        for i in range(len(graph)):
            if colors[i] != 0:
                continue
            colors[i] = 1
            q = []
            q.append(i)
            while (len(q)):
                head = q.pop(0)
                for nxt in graph[head]:
                    if colors[nxt] == 0:  ##
                        colors[nxt] = -1 * colors[head]
                        q.append(nxt)
                    else:
                        if colors[nxt] == colors[head]:
                            return False
        return True
