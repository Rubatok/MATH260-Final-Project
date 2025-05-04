import math

class Edge:
    def __init__(self, source, target, rate):
        self.source = source
        self.target = target
        self.weight = -math.log(rate)  # Convert rate to log-weight

def bellman_ford(vertices, edges, source):
    """
    This is the main function where Bellman-Ford is implemented to find arbitrage opportunities given the list of vertices, the list of edges and the source.
    This functions first iterates over each node in the graph |V|-1 times to update their shortest distance from the origin and detect if any of the shortest distance would still change after |V|-1 iterations. 
    It records the predecessor each time a shortest distance is updated, so it can reconstruct the negative cycle once it finds one.
    This function outputs the list of arbitrage opportunities and the cycle corresponding to the best arbitrage opportunity, if there is any.
    """
    distance = {v: float('inf') for v in vertices}
    predecessor = {v: None for v in vertices}
    distance[source] = 0

    # Calculate shortest distance for each edge |V|-1 times
    for _ in range(len(vertices) - 1):
        for edge in edges:
            if distance[edge.source] + edge.weight < distance[edge.target]:
                distance[edge.target] = distance[edge.source] + edge.weight
                predecessor[edge.target] = edge.source

    # Detect and find all negative cycles
    best_cycle = None
    best_cycle_weight = 0

    for edge in edges:
        if distance[edge.source] + edge.weight < distance[edge.target]:
            # Negative cycle found, trace back to get full cycle
            cycle = []
            visited = set()
            v = edge.target

            # Get a vertex in the cycle
            for _ in range(len(vertices)):
                v = predecessor[v]

            # Reconstruct the cycle
            cycle_start = v
            while True:
                if v in visited:
                    break
                visited.add(v)
                cycle.append(v)
                v = predecessor[v]
            cycle.append(cycle_start)
            cycle.reverse()

            # Compute cycle weight
            cycle_weight = 0
            for i in range(len(cycle) - 1):
                for e in edges:
                    if e.source == cycle[i] and e.target == cycle[i + 1]:
                        cycle_weight += e.weight
                        break
            for e in edges:
                if e.source == 'Currency_A' and e.target == cycle[0]:
                    cycle_weight += e.weight
                if e.source == cycle[-1] and e.target == 'Currency_A':
                    cycle_weight += e.weight

            if best_cycle is None or cycle_weight < best_cycle_weight:
                best_cycle = cycle
                best_cycle_weight = cycle_weight
                print(best_cycle_weight)

    return best_cycle

# Example usage
currencies = ['Currency_A','Currency_B', 'Currency_C', 'Currency_D']
exchange_rates_test1 = {
    ('Currency_A', 'Currency_B'): 1.34,
    ('Currency_A', 'Currency_C'): 1.98,
    ('Currency_A', 'Currency_D'): 0.64,
    ('Currency_B', 'Currency_A'): 0.72,
    ('Currency_B', 'Currency_D'): 0.52,
    ('Currency_B', 'Currency_C'): 1.45,
    ('Currency_C', 'Currency_B'): 0.7,
    ('Currency_C', 'Currency_D'): 0.31,
    ('Currency_C', 'Currency_A'): 0.48,
    ('Currency_D', 'Currency_A'): 1.49,
    ('Currency_D', 'Currency_B'): 1.95,
    ('Currency_D', 'Currency_C'): 3.1
}
exchange_rates_test2 = {
    ('Currency_A', 'Currency_B'): 2.0,
    ('Currency_B', 'Currency_C'): 2.0,
    ('Currency_C', 'Currency_A'): 0.25,
    ('Currency_A', 'Currency_C'): 4.0,
    ('Currency_C', 'Currency_B'): 0.5,
    ('Currency_B', 'Currency_A'): 0.5, 
    ('Currency_A', 'Currency_D'): 1.5,
    ('Currency_D', 'Currency_B'): 1.333, 
    ('Currency_D', 'Currency_C'): 2.666,
    ('Currency_C', 'Currency_D'): 0.375,  
    ('Currency_B', 'Currency_D'): 0.75,  
    ('Currency_D', 'Currency_A'): 0.666   
}

edges = [Edge(src, tgt, rate) for (src, tgt), rate in exchange_rates_test1.items()]
best_arbitrage_cycle = bellman_ford(currencies, edges, 'Currency_A')

if best_arbitrage_cycle:
    print("Best arbitrage cycle found:")
    print(" -> ".join(best_arbitrage_cycle))
else:
    print("No arbitrage opportunity found.")
