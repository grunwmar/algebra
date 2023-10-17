from . import generate_basis_signature
import itertools

ELEMENT_REPR_VEC = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8"]
ELEMENT_REPR_SCALAR = "1"
ELEMENT_REPR_PSEUDO = "i"


class Element:

    def __init__(self, dim: int, rank: int, indices: list):
        self._indices = indices
        self._rank = rank
        self._dim = dim

        self.__is_scalar__ = False
        self.__is_pseudo_scalar__ = False

        if len(indices) == 0:
            self.__is_scalar__ = True

        if dim == rank:
            self.__is_pseudo_scalar__ = True

    def __repr__(self):

        if self.__is_scalar__:
            return ELEMENT_REPR_SCALAR

        if self.__is_pseudo_scalar__:
            return ELEMENT_REPR_PSEUDO

        string = ""
        for i in self._indices:
            string += ELEMENT_REPR_VEC[i-1]

        return string


def create_basis(n: int):
    sig = generate_basis_signature(n)

    elements = {0: Element(n, 0, [])}

    for k, v in sig.items():
        if 0 < k < n:
            indices = [i+1 for i in range(n)]
            perm_indices = list(itertools.combinations(indices, k))
            elements[k] = []

            for index_tuple in perm_indices:
                elements[k].append(Element(n, k, list(index_tuple)))

    elements[n] = Element(n, n, [(i+1) for i in range(n)])

    return elements
