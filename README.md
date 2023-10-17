# Geometric algebra

Result of running `main.py`
````python
from cfalg.Algebra import create_basis
b = create_basis(4)
print(b)
````
is
```json
{0: 1, 1: [e1, e2, e3, e4], 2: [e1e2, e1e3, e1e4, e2e3, e2e4, e3e4], 3: [e1e2e3, e1e2e4, e1e3e4, e2e3e4], 4: i}
```
In the `./cfalg/Algebra.py` is specified which character use to label elements in basis
```python
ELEMENT_REPR_VEC = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8"]
ELEMENT_REPR_SCALAR = "1"
ELEMENT_REPR_PSEUDO = "i"
```
I plan to move these constants to `./cfalg/__init__.py` and make choice of character representation of basis element customizable.