import unittest
from exemplo import A, B, C

class Test_A(unittest.TestCase):
    def setUp(self):
        self.data = list(range(1, 11, 1))
        self.i = -1
        self.msg = 'metodo implantado incorretamente'
        self.a = A(self.data.copy())
        #self.a.arr.sort(reverse=True) ---for break tests---

    def test_len(self):
        self.assertEqual(len(self.a), len(self.data),
                         self.msg)

    def test_getitem(self):
        inteiro = 3
        fatiamento = slice(0, 4, 1)
        self.assertEqual(self.a[inteiro], self.data[inteiro],
                         self.msg)
        self.assertEqual(self.a[fatiamento], self.data[fatiamento],
                         self.msg)

    def test_bool(self):
        self.assertEqual(bool(self.a), bool(self.data),
                         self.msg)

    def test_iteration(self):
        for i in range(len(self.a)):
            with self.subTest(i=i):
                self.assertEqual(self.a[i], self.data[i],
                                 self.msg)

class Test_B(unittest.TestCase):
    def setUp(self):
        self.data = list(range(1, 11, 1))
        self.msg = 'metodo implantado incorretamente'
        self.b = B(self.data.copy())
        #self.a.arr.sort(reverse=True)

    def test_iterate_getitem(self):
        i = -1
        for j in self.b:
            i += 1
            with self.subTest(j=j):
                self.assertEqual(j, self.data[i],
                                 self.msg)
                
    def test_bool_with_len(self):
        self.assertEqual(bool(self.b), bool(self.data),
                                 self.msg)
        self.b = B([])
        self.data.clear()
        self.assertEqual(bool(self.b) is False, bool(self.data) is False,
                                 self.msg)

class Test_C(unittest.TestCase):
    def setUp(self):
        self.c = C()
        self.msg = 'metodo implantado incorretamente'
        
    def test_bool(self):
        self.assertEqual(bool(self.c), True,
                                 self.msg)


if __name__ == '__main__':
    
    unittest.main()
