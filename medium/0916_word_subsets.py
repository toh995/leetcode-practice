class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # create b_counter
        b_counter = self.word_to_counter(B[0])

        for i in range(1, len(B)):
            counter = self.word_to_counter(B[i])
            for char in counter:
                b_counter[char] = max(counter[char], b_counter[char])

        # check each word in A
        ret = []
        for a in A:
            a_counter = self.word_to_counter(a)

            if all(a_counter[char] >= b_counter[char] for char in b_counter.keys()):
                ret.append(a)

        return ret

    def word_to_counter(self, word: str) -> Counter:
        counter = Counter()
        for char in word:
            counter[char] += 1
        return counter
