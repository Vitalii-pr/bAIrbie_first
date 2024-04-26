"""Polynomial task"""

class Mono:
    """Mono element class"""
    def __init__(self, coef, degree, next_el = None) -> None:
        self.coefficient = coef
        self.degree = degree if coef != 0 else 0
        self.next = next_el

    def __str__(self):
        if self.degree < 0:
            return "Mono: 0"
        if self.coefficient == 0:
            return "Mono: 0"
        if abs(self.coefficient) == 1 and self.degree == 0:
            return f"Mono: {self.coefficient}"

        return f"Mono: {self.coefficient if abs(self.coefficient) != 1 else ('-' if self.coefficient == -1 else '')}{'x' if self.degree> 0 else ''}{'**'+str(self.degree) if self.degree > 1 else ''}"

    def __repr__(self) -> str:
        return f"Mono(coeff={self.coefficient}, degree={self.degree})"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Mono):
            return False
        return self.degree == value.degree and self.coefficient == value.coefficient

class Polynomial:
    "Polynomial class"
    def __init__(self, *args, derivative = True) -> None:
        self.head = None
        self.first = None
        self.degree = 0

        def add_element(element):
            if isinstance(element, Mono):
                next_el = Mono(element.coefficient, element.degree)
                if self.head is not None:
                    self.head.next = next_el
                    self.head = next_el
                else:
                    self.head = next_el
                    self.first = next_el
            elif isinstance(element, Polynomial):
                temp_head = element.head
                while temp_head:
                    add_element(temp_head)
                    temp_head = temp_head.next
            else:
                raise TypeError("Unsupported element type")

        for elem in args:
            add_element(elem)
        if self.head:
            self.head.next = None
        self.head = self.first

        temp_head = self.head

        while temp_head:
            if temp_head.degree > self.degree:
                self.degree = temp_head.degree
            temp_head = temp_head.next

        self.derivative = self.derivative_func() if derivative else None

    def __str__(self):
        if self.head:
            output = ""

            temp_head = self.head
            while temp_head:
                add_string = str(temp_head)[6:] \
                if str(temp_head)[6:][0] == "-" else "+"+str(temp_head)[6:]
                output += add_string if add_string not in ('+0', '-0') else ""
                temp_head = temp_head.next
            output = "0" if not output else output

            output = output[1:] if output[0] == "+" else output

            return "Polynomial: " + output
        return "Polynomial: 0"

    def __repr__(self):
        if self.head:
            output = ""

            temp_head = self.head
            while temp_head:
                output += " -> " + repr(temp_head)
                temp_head = temp_head.next

            return f"Polynomial({output[4:]})"
        return "Polynomial()"

    def copy(self):
        """Copy function"""
        return Polynomial(self)

    def sort(self):
        """Sort polynomial"""
        if self.head is None or self.head.next is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.degree < current.next.degree:
                    current.degree, current.next.degree = current.next.degree, current.degree
                    current.coefficient, current.next.coefficient = \
                    current.next.coefficient, current.coefficient
                    swapped = True

                elif current.degree == current.next.degree == 0\
                    and current.coefficient < current.next.coefficient:
                    current.degree, current.next.degree = current.next.degree, current.degree
                    current.coefficient, current.next.coefficient = \
                    current.next.coefficient, current.coefficient
                    swapped = True
                current = current.next

    def simplify(self):
        """Simplify polynomial"""
        self.sort()
        current = self.head
        while current and current.next:
            next_node = current.next
            while next_node and (current.degree == next_node.degree or next_node.coefficient == 0):
                current.coefficient += next_node.coefficient
                current.next = next_node.next
                next_node = current.next
            current = current.next
        self.sort()
        if self.head == Mono(0,0):
            self.head = None

    def eval_at(self, x):
        """Evaluate at certain x value"""
        output = 0

        temp_head = self.head
        while temp_head:
            output += temp_head.coefficient * (x**temp_head.degree)
            temp_head = temp_head.next
        return output

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Polynomial):
            return False
        new_self = Polynomial(self, derivative=False)
        new_self.simplify()
        value.simplify()
        return str(new_self) == str(value)

    def __hash__(self):
        return 1

    def derivative_func(self):
        """Derivative of the polynomial"""
        if self.head:
            der_pol = Polynomial(self, derivative=False)
            der_pol.simplify()
            current_term = der_pol.head
            while current_term:
                if current_term.degree > 0:
                    current_term.coefficient *= current_term.degree
                    current_term.degree -= 1
                else:
                    current_term.coefficient = 0
                current_term = current_term.next
            der_pol.simplify()
            return der_pol
        return Polynomial(derivative=None)

    def __add__(self, value):
        new_polynom = Polynomial(self, value)
        new_polynom.simplify()
        return new_polynom

    def __sub__(self, value):
        new_polynom = Polynomial(self, value*-1)
        new_polynom.simplify()
        return new_polynom

    def __mul__(self, value):
        if isinstance(value, Polynomial):
            new_polynom = Polynomial(derivative=False)
            new_head = None
            temp_head = self.head
            while temp_head:
                temp_head2 = value.head
                while temp_head2:
                    new_coefficient = temp_head.coefficient * temp_head2.coefficient
                    new_degree = temp_head.degree + temp_head2.degree
                    new_elem = Mono(new_coefficient, new_degree)
                    if new_head:
                        new_head.next = new_elem
                        new_head = new_elem
                    else:
                        new_head = new_elem
                        new_polynom.head = new_head
                    temp_head2 = temp_head2.next
                temp_head = temp_head.next
            new_polynom.simplify()
            return new_polynom

        if isinstance(value, int):
            new_polynom = Polynomial(self, derivative=False)
            temp_head = new_polynom.head
            while temp_head:
                temp_head.coefficient *= value
                temp_head = temp_head.next

            new_polynom.simplify()
            return new_polynom
        return "Wrong value"

    def __rmul__(self, value):
        return self.__mul__(value)