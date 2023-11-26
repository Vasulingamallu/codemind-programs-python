def find_original_string(N, K, S_prime):
    S_list = list(S_prime)
    reversed_segments = []
    for i in range(K, 0, -1):
        S_list[:i] = reversed(S_list[:i])
        reversed_segments.append(''.join(S_list))
        original_string = reversed_segments[-1]
    return original_string
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S_prime = input().strip()
    original_string = find_original_string(N, K, S_prime)
    print(original_string)
