class WordFilter(object):

    def gen_data(self, word, index):
        for i in range(0, len(word) + 1):
            prefix = word[:i]  ## start from ""
            for j in range(1, len(word) + 1):
                suffix = word[-j:]  ## start from "e"
                self.use_d[prefix + "_" + suffix] = index
            self.use_d[prefix + "_"] = index

    def gen_data2(self, word, index):
        for i in range(0, len(word) + 1):
            prefix = word[:i]  ## start from ""
            for j in range(0, len(word) + 1):
                suffix = word[j:]  ## word[0:] => the whole string
                self.use_d[prefix + "_" + suffix] = index

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.use_d = {}  ### !
        p = 0
        while (p < len(words)):
            self.gen_data2(words[p], p)
            p += 1
        # print(self.use_d)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """

        key = prefix + "_" + suffix
        return self.use_d.get(key, -1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)