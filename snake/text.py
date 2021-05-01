class S():
    class _d():
        def __init__(self):
            self._a = 4
    def __init__(self):
        self._size = 0
    def i(self):
        self._size = self._d()

ret = S()
ret.i()
print(ret._size)