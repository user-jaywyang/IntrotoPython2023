class BasketballGame():
    #represents basketball game, two teams and their scores. Status of game is finished or in progress


    #initializer
    def __init__(self, first_team, second_team, first_score, second_score, status):
        
        self.__first_team = first_team
        self.__second_team = second_team
        self.__first_score = int(first_score)
        self.__second_score = int(second_score)
        self.__status = status
      
    #accessor function
    def get_winner(self):
        if self.__first_score == self.__second_score:
            print("Currently a draw")
        elif self.__first_score > self.__second_score:
            return(self.__first_team)
        else:
            return(self.__second_team)
    
    def display_winner(self):
        if self.__first_score == self.__second_score:
            print("Currently a draw")
        elif self.__first_score > self.__second_score:
            print(f"Current winner is {self.__first_team}")
        else:
            print(f"Current winner is {self.__second_team}")
    
    
    def get_first_score(self):
        return self.__first_score
    
    def get_second_score(self):
        return self.__second_score
    

    #mutator function
    def add_1point_first(self):
        self.__first_score += 1

    def add_1point_second(self):
        self.__second_score += 1

    def add_2point_first(self):
        self.__first_score += 2

    def add_2point_second(self):
        self.__second_score += 2

    def add_3point_first(self):
        self.__first_score += 3

    def add_3point_second(self):
        self.__second_score += 3
    
    def finish_game(self):
        self.__status = "Finished"
    
    def continue_game(self):
        self.__status = "In progress"


    #string
    def __str__(self):
        return f'First team : {self.__first_team} \n' +\
            f'Score : {self.__first_score} \n' +\
            f'Second team  : {self.__second_team} \n' +\
            f'Score : {self.__second_score} \n' +\
            f'Game status : {self.__status} \n'
