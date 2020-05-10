#include <stdio.h>
#include <stdlib.h>

typedef char VertexType;
typedef int EdgeType;

#define MAXVEX 100
#define INFINITY 65535

typedef struct {
    VertexType vexs[MAXVEX];
    EdgeType arc[MAXVEX][MAXVEX];
    int numVertexes, numEdges;
} MGraph;

void CreateGraph(MGraph *G)
{
    int i, j, k, w;
    printf("输入顶点数和边数:\n");
    scanf("%d %d", &G->numVertexes, &G->numEdges);
    for (i = 0; i < G->numVertexes; i++) {
        scanf(&G->vexs[i]);
    }
    for (i = 0; i < G->numVertexes; i++) {
        for (j = 0; j < G->numVertexes; j++) {
            G->arc[i][j] = INFINITY;
        }
    }
    for (k = 0; k < G->numEdges; k++) {
        printf("输入边的上下标\n");
        scanf("%d %d %d", &i, &j, &w);
        G->arc[i][j] = w;
        G->arc[j][i] = G->arc[i][j];
    }
}

typedef int Boolean;
Boolean visited[MAXVEX];


/* 递归方法实现深度优先遍历 */
void DFS(MGraph G, int i)
{
    int j;
    visited[i] = true;
    printf("%d", G.vexs[i]);
    for (j = 0; j < G.numVertexes; j++) {
        if (G.arc[i][j] == 1 && !visited[j]) {
            DFS(G, j);
        }
    }
}

void DFSTraverse(MGraph G)
{
    int i, j;
    memset(visited, 0, sizeof(visited[0])*MAXVEX);
    for (i = 0; i < G.numVertexes; i++) {
        if (!visited[i]) {
            DFS(G, i);
        }
    }
}

/* 非递归用栈实现深度优先遍历 */
void DFS(MGraph G, int i)
{
    int j;
    stack s;
    visited[i] = 1;
    printf("%c", G.vexs[i]);
    Push(&s, i);
    while (!StackEmpty(s)) {
        i = s.top()
        for (j = 0; j < G.numVertexes; j++) {
            if (G.arc[i][j] == 1 && !visited[j]) {
                visited[j] = 1;
                printf("%c", G.vexs[j]);
                Push(&s, j);
                break;
            }
        }
        if (j == G.numVertexes) {
            Pop(&s);
        }
    }
}

void DFSTraverse(MGraph G)
{
    int i;
    for (i = 0; i < G.numVertexes; i++) {
        visited[i] = 0;
    }
    for (i = 0; i < G.numVertexes; i++) {
        if (!visited[i]) {
            DFS(G, i);
        }
    }
}

/* 用队列实现广度优先遍历 */
void BFSTraverse(MGraph G)
{
    int i, j;
    Queue Q;
    for (i = 0; i < G.numVertexes; i++) {
        visited[i] = FALSE;
    }
    InitQueue(&Q);
    for (i = 0; i < G.numVertexes; i++) {
        if (!visited[i]) {
            visited[i] = true;
            printf("%c", G.vexs[i]);
            EnQueue(&G, i);
            while (!QueueEmpty(&G)) {
                DEQueue(&G, &i);
                for (j = 0; j < G.numVertexes; j++) {
                    if (!visited[j] && G.arc[i][j] == 1) {
                        visited[j] = true;
                        printf("%c", G.vexs[j]);
                        EnQueue(&G, j);
                    }
                }
            }
        }
    }
}
