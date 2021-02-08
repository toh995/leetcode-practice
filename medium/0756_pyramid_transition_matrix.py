from collections import defaultdict
from functools import cache
from itertools import product
from typing import Set, Tuple

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # key: string of length 2 representing a pair of nodes
        # value: set of strings representing potential top nodes
        self.allowed_pairs = defaultdict(set)

        # populate allowed_pairs
        for triple in allowed:
            pair = triple[:2]
            top_node = triple[2:]

            self.allowed_pairs[pair].add(top_node)

        # set of string tuples, where each tuple represents allowed nodes for the current level
        bottom = tuple(bottom)
        curr_levels = {bottom,}

        for _ in range(len(bottom) - 1):
            # set of string tuples, where each tuple represents allowed nodes for the next level
            next_levels = set()

            for curr_level in curr_levels:
                next_level = self.get_next_level(curr_level)

                if next_level:
                    next_levels = next_levels | next_level

            if next_levels:
                curr_levels = next_levels
            else:
                return False

        return True


    @cache
    def get_next_level(self, bottom: Tuple[str]) -> Set[Tuple[str]]:
        # tuple where each entry is a set representing the possible nodes
        # for the i-th position
        top_nodes = [
            set() for _ in range(len(bottom) - 1)
        ]

        for i in range(0, len(bottom)-1):
            pair = bottom[i : i+2]
            pair = "".join(pair)

            if pair in self.allowed_pairs:
                nodes_to_add = self.allowed_pairs[pair]
                top_nodes[i] = top_nodes[i].union(nodes_to_add)

        # calculate all possible permuations for the level above,
        # to see if one is allowed
        return set(
            product(*top_nodes)
        )
