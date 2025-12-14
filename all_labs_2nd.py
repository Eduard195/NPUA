import sys
from collections import deque
from functools import cmp_to_key

sys.setrecursionlimit(1_000_000)

INF = 1 << 60


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def dist2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


def sgn(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


def on_seg(a, b, p):
    return (
        min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )


def segments_intersect(a, b, c, d):
    o1 = orient(a, b, c)
    o2 = orient(a, b, d)
    o3 = orient(c, d, a)
    o4 = orient(c, d, b)

    s1, s2, s3, s4 = sgn(o1), sgn(o2), sgn(o3), sgn(o4)

    if s1 == 0 and on_seg(a, b, c):
        return True
    if s2 == 0 and on_seg(a, b, d):
        return True
    if s3 == 0 and on_seg(c, d, a):
        return True
    if s4 == 0 and on_seg(c, d, b):
        return True

    return (s1 * s2 < 0) and (s3 * s4 < 0)


def run_finite_automaton_dfa(it, out):
    n = int(next(it))
    m = int(next(it))

    go = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            go[i][j] = int(next(it))

    start = int(next(it))
    k = int(next(it))
    acc = [0] * n
    for _ in range(k):
        acc[int(next(it))] = 1

    s = next(it).decode()
    st = start
    for ch in s:
        sym = ord(ch) - ord("a")
        if sym < 0 or sym >= m:
            out.append("REJECT\n")
            return
        st = go[st][sym]

    out.append("ACCEPT\n" if acc[st] else "REJECT\n")


def dfs_print(v, g, used, order):
    used[v] = 1
    order.append(v)
    for to in g[v]:
        if not used[to]:
            dfs_print(to, g, used, order)


def run_depth_first_search_dfs(it, out):
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    s = int(next(it))
    used = [0] * n
    order = []
    dfs_print(s, g, used, order)

    out.append(" ".join(map(str, order)) + "\n")


def dfs_comp(v, g, comp, cid):
    comp[v] = cid
    for to in g[v]:
        if comp[to] == -1:
            dfs_comp(to, g, comp, cid)


def run_connected_components(it, out):
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    comp = [-1] * n
    cid = 0
    for i in range(n):
        if comp[i] == -1:
            dfs_comp(i, g, comp, cid)
            cid += 1

    out.append(str(cid) + "\n")
    out.append(" ".join(map(str, comp)) + "\n")


def run_bfs_graph(it, out):
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        g[v].append(u)

    s = int(next(it))
    dist = [-1] * n
    q = deque([s])
    dist[s] = 0

    while q:
        v = q.popleft()
        for to in g[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                q.append(to)

    out.append(" ".join(map(str, dist)) + "\n")


def run_bfs_grid(it, out):
    h = int(next(it))
    w = int(next(it))
    a = [next(it).decode() for _ in range(h)]

    sx = int(next(it))
    sy = int(next(it))
    tx = int(next(it))
    ty = int(next(it))

    if not (0 <= sx < h and 0 <= sy < w and 0 <= tx < h and 0 <= ty < w):
        out.append("-1\n")
        return

    if a[sx][sy] == "#":
        out.append("-1\n")
        return

    dist = [[-1] * w for _ in range(h)]
    q = deque([(sx, sy)])
    dist[sx][sy] = 0

    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and a[nx][ny] != "#" and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    out.append(str(dist[tx][ty]) + "\n")


def run_topological_sort_kahn(it, out):
    n = int(next(it))
    m = int(next(it))
    g = [[] for _ in range(n)]
    indeg = [0] * n

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        g[u].append(v)
        indeg[v] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []

    while q:
        v = q.popleft()
        order.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to] == 0:
                q.append(to)

    out.append("IMPOSSIBLE\n" if len(order) != n else " ".join(map(str, order)) + "\n")


def run_dijkstra_on2(it, out):
    n = int(next(it))
    m = int(next(it))
    w = [[INF] * n for _ in range(n)]

    for i in range(n):
        w[i][i] = 0

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        c = int(next(it))
        w[u][v] = min(w[u][v], c)

    s = int(next(it))
    dist = [INF] * n
    used = [0] * n
    dist[s] = 0

    for _ in range(n):
        v = -1
        for i in range(n):
            if not used[i] and (v == -1 or dist[i] < dist[v]):
                v = i
        if v == -1 or dist[v] >= INF:
            break

        used[v] = 1
        for to in range(n):
            if w[v][to] < INF:
                dist[to] = min(dist[to], dist[v] + w[v][to])

    out.append(" ".join("INF" if d >= INF else str(d) for d in dist) + "\n")


def run_line_segment_intersection(it, out):
    a = (int(next(it)), int(next(it)))
    b = (int(next(it)), int(next(it)))
    c = (int(next(it)), int(next(it)))
    d = (int(next(it)), int(next(it)))
    out.append("YES\n" if segments_intersect(a, b, c, d) else "NO\n")


def run_bellman_ford(it, out):
    n = int(next(it))
    m = int(next(it))
    edges = []

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))

    s = int(next(it))
    dist = [INF] * n
    dist[s] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] < INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    for u, v, w in edges:
        if dist[u] < INF and dist[v] > dist[u] + w:
            out.append("NEGATIVE CYCLE\n")
            return

    out.append(" ".join("INF" if d >= INF else str(d) for d in dist) + "\n")


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    it = iter(data)
    choice = int(next(it))
    out = []

    if choice == 1:
        run_finite_automaton_dfa(it, out)
    elif choice == 2:
        run_depth_first_search_dfs(it, out)
    elif choice == 3:
        run_connected_components(it, out)
    elif choice == 4:
        run_bfs_graph(it, out)
    elif choice == 5:
        run_bfs_grid(it, out)
    elif choice == 6:
        run_topological_sort_kahn(it, out)
    elif choice == 7:
        run_dijkstra_on2(it, out)
    elif choice == 8:
        run_line_segment_intersection(it, out)
    elif choice == 11:
        run_bellman_ford(it, out)

    sys.stdout.write("".join(out))


if __name__ == "__main__":
    main()
