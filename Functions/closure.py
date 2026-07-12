# closure (inner function) , inner function stores and remembers the value of variable created in outer function

def create_discount(discount):

    def calculate(price):

        return price - (price * discount / 100)

    return calculate


student_discount = create_discount(10)

vip_discount = create_discount(20)


print(student_discount(1000))

print(vip_discount(1000))