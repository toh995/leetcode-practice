class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.forward_mapping = defaultdict(set)
        self.backward_mapping = defaultdict(set)

        for u, v in connections:
            self.forward_mapping[u].add(v)
            self.backward_mapping[v].add(u)

        return self.helper(0, -1)


    def helper(self, curr_node: int, parent: int) -> int:
        num_bad_edges = len(self.forward_mapping[curr_node])

        if parent in self.forward_mapping[curr_node]:
            num_bad_edges -= 1

        for child in self.forward_mapping[curr_node]:
            if child == parent:
                continue
            num_bad_edges += self.helper(child, curr_node)

        for child in self.backward_mapping[curr_node]:
            if child == parent:
                continue
            num_bad_edges += self.helper(child, curr_node)

        return num_bad_edges
