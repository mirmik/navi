#!/usr/bin/env python3

from sympy import S, Symbol, Mul, Add
import sympy

def sort_product(product):
    while True:
        if not isinstance(product,Mul):
            return product

        arglist = list(product.args)
        i = 0
        while i < len(arglist)-1:
            slice_prod = arglist[i]*arglist[i+1]
            is_mul = isinstance(slice_prod,Mul)
            arglist[i:i+2] = slice_prod.args if is_mul else [slice_prod]
            i += 1

        new_product = Mul(*arglist)
        if product == new_product:
            return new_product
        product = new_product

def sort_products(expr):
    if expr.is_Atom:
        return expr
    else:
        simplified_args = (sort_products(arg) for arg in expr.args)
        if isinstance(expr,Mul):
            return sort_product(Mul(*simplified_args))
        else:
            return expr.func(*simplified_args)

class Ort(sympy.Symbol):
	def __new__(cls,*args,**kwargs):
		return super().__new__(cls,*args,**kwargs,commutative=False)

	def __mul__(self,other):
		if isinstance(other,Ort):
			if other.name < self.name:
				return -Symbol.__mul__(other,self)
		return super().__mul__(other)

	def __pow__(self,exponent):
		if exponent==2:
			return S.One
		return super().__pow__(exponent)

class Proj(sympy.Symbol):
	def __new__(cls,*args,**kwargs):
		return super().__new__(cls,*args,**kwargs,commutative=False)

	def __mul__(self,other):
		if isinstance(other,Ort):
			if other.name < self.name:
				return -Symbol.__mul__(other,self)
		return super().__mul__(other)

	def __pow__(self,exponent):
		if exponent==2:
			return S.Zero
		return super().__pow__(exponent)

e_1 = Ort("e_1")
e_2 = Ort("e_2")
e_3 = Ort("e_3")
e_4 = Proj("e_4")
sympy.var("n_1 n_2 n_3 n_4 a_1 a_2 a_3 m_1 m_2 m_3 m_4")

M = m_1*e_1 + m_2*e_2 + m_3*e_3 + m_4*e_4
N = n_1*e_1 + n_2*e_2 + n_3*e_3 + n_4*e_4
A = a_1*e_1 + a_2*e_2 + a_3*e_3

E1 = sympy.expand(M*N*A*N*M)
E2 = [sort_products(a) for a in E1.args]
E3 = sum(E2).expand().args

print(E2)

a0 = [ e for e in E3 if e_4 not in e.args ]
a4 = [ e for e in E3 if e_4 in e.args ]

print("Real:", len(a0))
for a in a0:
	print(a)

print("Dual:", len(a4))
for a in a4:
	print(a)