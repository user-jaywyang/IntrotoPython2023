import Q3class

def main():
    #test for Rational class
    instance1 = Q3class.Rational(3,4)
    print(instance1.get_numerator)
    instance1.display_value()
    instance1.set_denominator(-2)
    instance1.set_numerator(10)
    print(instance1)

if __name__ == '__main__':
    main()
