#!/usr/bin/env python3
from typing import List, Union


class A:
    def __init__(self, arr: List):
        self.arr = arr

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, index: Union[int, slice]):
        return self.arr[index]

    def __bool__(self):
        return True if bool(self.arr) else False

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self.arr):
            return self.arr[self.i]

        else:
            raise StopIteration

class B:
    """
    Objeto que pode gerar um iteravel so com __getitem__ e bool com __len__
    """
    def __init__(self, arr: List):
        self.arr = arr

    def __getitem__(self, index: Union[int, slice]):
        return self.arr[index]

    def __len__(self):
        return len(self.arr)

class C:...


if __name__ == '__main__':    # Testando os metodos
    
    # 1) __init__
    a = A(list(range(1, 11, 1)))
    
    # 2) __len__
    print(f'Tamanho do objeto:\t{len(a)}')
    
    # 3) __getitem__
    print(f'Com tipo \'int\':\n3° elemento: {a[2]} ''\nCom tipo \'slice\':\nde 1° a 4° elemento:\t{0} '.format(a[:4]))
    
    # 4) __bool__
    valor = True if a else False
    print(f"O valor logico: {valor}")
    
    # 5)__iter__
    iter_ = iter(a)
    print(f"Estrutura iteravel {iter_}")
    
    # 5) __next__
    try:
      while (a:=next(iter_)):
        print(f"Item da iteracao: {a}")
      
    except StopIteration:
     print("\n--Acabou a iteracao--")
