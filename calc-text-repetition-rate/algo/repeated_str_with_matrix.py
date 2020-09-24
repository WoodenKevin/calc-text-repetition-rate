class RepeatedStrWithMatrix(object):
    def __init__(self, org_str, cmp_str):
        self.org_str = org_str
        self.org_str_len = len(org_str)
        self.cmp_str = cmp_str
        self.cmp_str_len = len(cmp_str)
        self.res_lst = []

        self._init_matrix()
        self._calc_res_lst()

    def _init_matrix(self):
        self.matrix = [[0] * self.org_str_len for _ in range(self.cmp_str_len)]

    def _calc_res_lst(self):
        for i, str2_val in enumerate(self.cmp_str):
            for j, str1_val in enumerate(self.org_str):
                if str1_val == str2_val:
                    val = self.matrix[i - 1][j - 1] + 1 if i and j else 1
                    self.matrix[i][j] = val
                if i and j:
                    if self.matrix[i - 1][j - 1] and not self.matrix[i][j]:
                        self._push_res(i, j)
                if i == self.cmp_str_len - 1 or j == self.org_str_len - 1:
                    if self.matrix[i][j] != 0:
                        self._push_res(i + 1, j + 1)

    def _push_res(self, i, j):
        length = self.matrix[i - 1][j - 1]

        if length > 1:
            self.res_lst.append(self.org_str[j - length:j])

    def get_res(self):
        repeated_str_len = len(''.join(self.res_lst))

        return {
            'org_str': self.org_str,
            'cmp_str': self.cmp_str,
            'cmp_str_len': self.cmp_str_len,
            'res_lst': self.res_lst,
            'repeated_str_len': repeated_str_len
        }
