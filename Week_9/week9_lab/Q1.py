import Q1class

def main():
    #test for counter classs
    instance1 = Q1class.Counter()
    instance1.decrease()
    instance1.increase()
    instance1.display_count()
    instance1.increase()
    instance1.set_zero()
    print(instance1)


if __name__ == '__main__':
    main()
