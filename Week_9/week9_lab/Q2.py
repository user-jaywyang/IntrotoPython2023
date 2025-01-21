import Q2class

def main():
    #test for BasketballGame classs
    instance1 = Q2class.BasketballGame("Eagles", "Hawks", 0, 0 , "In progress")
    instance1.add_3point_first()
    instance1.add_2point_second()
    instance1.add_2point_first()
    instance1.add_1point_second()
    print(instance1)
    instance1.get_winner()
    instance1.finish_game()
    instance1.get_first_score
    print(instance1)
 

if __name__ == '__main__':
    main()
