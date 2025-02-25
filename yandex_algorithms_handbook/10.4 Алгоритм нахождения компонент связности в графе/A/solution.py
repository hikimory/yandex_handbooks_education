from collections import defaultdict
def find_bridges(n, m, graph):
    visited = set()
    chains = []
    for begin in range(1, n + 1):
        if begin not in visited:
            stack, chain = [], []
            stack.append(begin)
            chain.append(begin)
            visited.add(begin)
            while stack:
                vi = stack.pop()
                for vj in graph[vi]:
                    if vj not in visited:
                        visited.add(vj)
                        chain.append(vj)
                        stack.append(vj)
            chains.append(chain)
    
    if len(chains) > 1:
        answer = []
        for i in range(1, len(chains)):
            answer.append(f'{chains[i - 1][0]} {chains[i][0]}') #any vi and vj
        print(len(answer))
        print('\n'.join(answer))
    else:
        print(0)
        
def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    find_bridges(n, m, graph)

if __name__ == "__main__":
    main()