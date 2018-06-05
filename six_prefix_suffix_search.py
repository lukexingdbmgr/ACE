class WordFilter(object):
    prefix_d = {}
    suffix_d = {}

    def gen_prefix(self, word, index):
        for i in range(1, len(word)):
            self.prefix_d[word[:i]] = index

    def gen_suffix(self, word, index):
        # word = word[::-1]  ## reverse word
        for i in range(1, len(word)):
            # self.suffix_d[word[:-i]] = index
            self.suffix_d[word[-i:]] = index  ## from last i to the end; the above one is wrong

    def __init__(self, words):
        """
        :type words: List[str]
        """
        p = 0
        while (p < len(words)):
            self.gen_prefix(words[p], p)
            self.gen_suffix(words[p], p)
            p += 1

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """

        if prefix == "" or suffix == "":
            return -1

        prefix_match = self.prefix_d.get(prefix, None)
        suffix_match = self.suffix_d.get(suffix, None)
        if prefix_match == suffix_match and prefix_match is not None:
            return prefix_match
        else:
            return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

c = WordFilter(["apple"])
print(c.f("", ""))
