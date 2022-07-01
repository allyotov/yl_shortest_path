from itertools import permutations, combinations
from unittest import installHandler
POINTS = {
    0: (0, 2),
    1: (2, 5),
    2: (5, 2),
    3: (6, 6),
    4: (8, 3)
    }

def get_possible_sequences(points):
    point_nums = sorted(list(points.keys()))
    start_point = point_nums.pop(0)
    return [(start_point,) + seq + (start_point,) for seq in permutations(point_nums, len(point_nums))]

def get_possible_edges(points):
    edge_vars = list(combinations(points.keys(), 2))
    return edge_vars

def count_edge_len(a, b):
    return ((POINTS[b][0] - POINTS[a][0]) ** 2 + (POINTS[b][1] - POINTS[a][1]) ** 2) ** 0.5

def get_edges_len(edge_vars):
    edge_len = dict()
    for a, b in list(edge_vars):
        l = count_edge_len(a, b)
        edge_len[(a, b)] = l
        edge_len[(b, a)] = l
    return edge_len

def get_result_string(seq, intermediate_lens, path_len):
    result_str = ''
    first_point = seq[0]
    seq = seq[1:]
    result_str += str(POINTS[first_point])
    for point_num, intermediate_len in zip(seq, intermediate_lens):
        result_str += ' -> '
        result_str += str(POINTS[point_num])
        result_str += '[{}]'.format(intermediate_len)
    result_str += ' = '
    result_str += str(path_len)
    return result_str

def get_shortest_path():
    possible_edges = get_possible_edges(POINTS)
    edge_lens = get_edges_len(possible_edges)
    sequences = get_possible_sequences(POINTS)
    shortest_path_len = None
    shortest_seq = None
    shorted_path_intermediate = None
    for seq in sequences:
        path_len = 0
        intermediate_len = []
        for i in range(len(seq) - 1):
            path_len += edge_lens[(seq[i], seq[i+1])]
            intermediate_len.append(path_len)
        if shortest_path_len is None or shortest_path_len > path_len:
            shortest_path_len = path_len
            shortest_seq = seq
            shorted_path_intermediate = intermediate_len
    
    return get_result_string(shortest_seq, shorted_path_intermediate, shortest_path_len)


if __name__ == '__main__':
    print(get_shortest_path())