# python3

from collections import deque


def max_sliding_window_naive(sequence, m):
    q = deque()
    res = []
    cur_max = float('-inf')

    for idx, item in enumerate(sequence):
        if idx == 0:
            q.append(item)
        elif idx == m - 1:
            q.append(cur_max)
        elif idx < m:
            cur_max = item if cur_max < item else cur_max
        else:
            drop_item = q[0]
            psudo_max = q[-1]
            res.append(max(drop_item, psudo_max))
            q.popleft()
            q.append(item)

    drop_item = q[0]
    psudo_max = q[-1]
    res.append(max(drop_item, psudo_max))

    return res


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
