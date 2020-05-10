#include <stdio.h>
#include <stdlib.h>

#define MAXVEX 100

typedef char VertexType;
typedef int EdgeType;

typedef struct EdgeNode {
    int adjvex;
    EdgeType weight;
    struct EdgeNode *next;
} EdgeNode;

typedef struct VertexNode {
    VertexType data;
    struct EdgeNode *firstEdge;
} VertexNode, AdjList[MAXVEX];

typedef struct {
    AdjList adjList;
    int numVertexes, numEdges;
} GraphAdjList;

void CreateGraph(GraphAdjList *G)
{
    int i, j, k;
    EdgeNode *e;
    printf("输入定点数和边数:\n");
    scanf("%d %d", &G->numVertexes, &G->numEdges);
    for (i = 0; i < G->numVertexes; i++) {
        scanf(&G->adjList[i].data);
        G->adjList[i].firstEdge = NULL;
    }

    for (k = 0; k < G->numEdges; k++) {
        printf("输入边上的顶点号\n");
        scanf("%d %d", &i, &j);
        e = (EdgeNode *)malloc(sizeof(EdgeNode));
        e->adjvex = j;
        e->next = G->adjList[i].firstEdge;
        G->adjList[i].firstEdge = e;

        e = (EdgeNode *)malloc(sizeof(EdgeNode));
        e->adjvex = i;
        e->next = G->adjList[j].firstEdge;;
        G->adjList[j].firstEdge = e;
    }
}

typedef int Boolean;
Boolean visited[MAXVEX];

/* 递归方法实现深度优先遍历 */
void DFS(GraphAdjList *GL, int i)
{
    EdgeNode *p;
    visited[i] = true;
    printf("%c", GL->adjList[i].data);
    p = GL->adjList[i].firstEdge;
    while (p) {
        if (!visited[p->adjvex]) {
            DFS(GL, p->adjvex);
        }
        p = p->next
    }
}

void DFSTraverse(GraphAdjList *GL)
{
    int i;
    for (i = 0; i < GL->numVertexes; i++) {
        visited[i] = FALSE;
    }

    for (i = 0; i < GL->numVertexes; i++) {
        if (!visited[i]) {
            DFS(GL, i);
        }
    }
}


/* 非递归用栈实现深度优先遍历 */
void DFS(GraphAdjList *GL, int i)
{
    stack s;
    EdgeNode *p;
    printf("%c", GL->adjList[i].data);
    visited[i] = 1;
    Push(&s, i)
    while (!StackEmpty(s)) {
        p = GL->adjList[s.top()].firstEdge;
        while (p) {
            if (!visited[p->adjvex]) {
                visited[p->adjvex] = 1;
                printf("%c", GL->adjList[p->adjvex].data);
                Push(&s, p->adjvex);
                p = GL->adjList[p->adjvex].firstEdge;
            } else {
                p = p->next;
            }
        }
        if (p == NULL) {
            Pop(&s);
        }
    }
}

void DFSTraverse(GraphAdjList *GL)
{
    int i;
    for (i = 0; i < GL->numVertexes; i++) {
        visited[i] = 0;
    }
    for (i = 0; i < GL->numVertexes; i++) {
        if (!visited[i]) {
            DFS(GL, i);
        }
    }
}

/* 用队列实现广度优先遍历 */
void BFSTraverse(GraphAdjList *GL)
{
    int i;
    EdgeNode *p;
    Queue Q;
    for (i = 0; i < GL->numVertexes; i++) {
        visited[i] = FALSE;
    }
    InitQueue(&Q);
    for (i = 0; i < GL->numVertexes; i++) {
        if (!visited[i]) {
            visited[i] = true;
            printf("%c", GL->adjList[i].data);
            EnQueue(&G, i);
            while (!QueueEmpty(&G)) {
                DEQueue(&G, i);
                p = GL->adjList[i].firstEdge;
                while (p) {
                    if (!visited[p->adjvex]) {
                        visited[p->adjvex] = true;
                        printf("%c", GL->adjList[p->adjvex].data);
                        EnQueue(&G, p->adjvex);
                    }
                    p = p->next;
                }
            }
        }
    }
}
