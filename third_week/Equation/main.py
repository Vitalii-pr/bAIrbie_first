'''polynomial'''
import math

class Polynomial:
    '''polynomial'''
    def __init__(self, coeffs:list = None) -> None:
        '''init'''
        self.degree = len(str(int(''.join([str(abs(x)) for x in coeffs]))))-1
        self.coeffs = list(coeffs[::-1][:self.degree+1]) if coeffs else [0]

    def __str__(self) -> str:
        '''str'''
        prosto, power = '',''
        single = ('+' if self.coeffs[0] >= 0 else '') + str(self.coeffs[0])
        if len(self.coeffs) > 1:
            prosto = f'{("+" if self.coeffs[1] >= 0 else "") + str(self.coeffs[1])}x'
        if len(self.coeffs) > 2:
            power = ''.join([(("+" if self.coeffs[-1-x] >= 0 else "") + \
str(self.coeffs[-1-x]) + "x**" + str(len(self.coeffs)-x-1)) for x in range(len(self.coeffs)-2)])

        full = power.replace('1x**', 'x**') + \
prosto.replace('1x', 'x').replace('+0x', '') + ('' if single == '+0' else single)
        return f'Polynomial: {(full if full.startswith("-") else full[1::]) if full else "0"}'


    def __repr__(self) -> str:
        '''repr'''
        return f'Polynomial(coeffs={list(self.coeffs)[::-1]})'

    def eval_at(self,val):
        '''count by passing value of x'''
        return sum(v*(val**(i)) for i, v in enumerate(self.coeffs))

    def __eq__(self, val: 'Polynomial') -> bool:
        '''equal method'''
        if len (self.coeffs) == 1:
            return self.coeffs[0] == val
        if isinstance(val, Polynomial):
            return self.degree == val.degree and self.coeffs == val.coeffs
        return False

    def __hash__(self) -> int:
        '''hash'''
        return hash(tuple(self.coeffs))

    def multiply_by_value(self, val):
        '''all coeffs multiple by value'''
        return Polynomial([x*int(val) for x in self.coeffs[::-1]])

    @property
    def derivative(self):
        '''derivative'''
        if len(self.coeffs)==1:
            return Polynomial([0])
        coeffs = [i*v for i, v in enumerate(self.coeffs)]
        return Polynomial(coeffs[::-1][:-1])

    def __add__(self, val):
        '''sum'''
        return Polynomial([sum(x) for x in list(zip(self.coeffs, val.coeffs))][::-1])

    def __mul__(self, val:'Polynomial'):
        '''multiplication'''
        res = [0] * (self.degree + val.degree + 1)
        for i, value in enumerate(self.coeffs):
            for j, value_2 in enumerate(val.coeffs):
                res[i + j] += value*value_2
        return Polynomial(res[::-1])

class Quadratic(Polynomial):
    '''quadratic equation'''
    def __init__(self, coeffs: list = None) -> None:
        '''init'''
        super().__init__(coeffs)
        if not list or len(self.coeffs) != 3:
            raise ValueError ('Quadratic polynomial must have exactly 3 coefficients')
        self.a = self.coeffs[2]
        self.b = self.coeffs[1]
        self.c = self.coeffs[0]

    def __repr__(self) -> str:
        '''repr'''
        return f'Quadratic(a={self.a}, b={self.b}, c={self.c})'

    def __str__(self):
        '''str'''
        return "Quadratic: "+super().__str__().split()[1]

    @property
    def discriminant(self):
        '''discriminant'''
        return self.b**2 - 4*self.a * self.c

    @property
    def number_of_real_roots(self):
        '''amount of real roots'''
        if self.discriminant<0:
            return 0
        if self.discriminant == 0:
            return 1
        return 2

    def get_real_roots(self):
        '''get roots'''
        if self.number_of_real_roots >0:
            root1 = (-self.b + self.discriminant**0.5)/(2*self.a)
            root2 = (-self.b - self.discriminant**0.5)/(2*self.a)
            res = list({root1, root2})
            res.sort()
            return res
        return []
