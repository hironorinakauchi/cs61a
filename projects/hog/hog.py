"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    # score_list = []
    # for i in range(1, num_rolls+1):
    #     score_list.append(dice())
    # if 1 in score_list: # determines if its Pig out or not
    #     return 0
    # else:
    #     return(sum(score_list))
    roll_num = 0
    pigout = False
    total = 0
    while roll_num < num_rolls:
        dice_value = dice()
        if dice_value == 1:
            pigout = True
            total = 0
        elif pigout == False :
            total += dice_value
        roll_num += 1
    return total


    # END Question 1

def is_prime(n):
    """
    returns True if the current_score is a prime number returns False otherwise
    """
    if n <= 1:
        return False
    else:
        result=all(n % two_up_to_current for two_up_to_current in range(2, n))
        return result

def next_prime(prime_n):
    """
    Finds the next prime number
    """
    for i in range(prime_n+1, prime_n*2):
        if is_prime(i) == True:
            return i
            break

def free_bacon(s):
    """A player who chooses to roll zero dice scores one more than the 
    largest digit in the opponent's total score.
    """
    if s < 10: # if oponent_score is just one digit # (1~9)
            return max([s, s // 10]) + 1
    else: # if the digits >= 2
        return max([s//10, s%10]) + 1

def take_turn(num_rolls, opponent_score, dice=six_sided): # freebacon, hogtimus(functions are outside the function) and PIGGY BACK!!!
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    result = 0
    if num_rolls == 0:
        result = free_bacon(opponent_score)
        if is_prime(result) == True:
            return next_prime(result)
        else:
            return result
    else: # num_rolls >= 0
        result = roll_dice(num_rolls, dice)
        if is_prime(result) == True:
            return next_prime(result)
        else:
            return result
    # END Question 2


def select_dice(score, opponent_score): # a.k.a. Hog Wild
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score) % 7 == 0:
        return four_sided
    else:
        return six_sided
    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    if score0 <= 9: 
        score0 = str(float(score0)).replace(".", "")[::-1]
    elif score1 <= 9:
        score1 = str(float(score1)).replace(".", "")[::-1]
    score0, score1 = str(score0)[-2:], str(score1)[-2:]
    if score0[::-1] == score1 or score1[::-1] == score0: 
        return True 
    else: 
        return False


    # END Question 4


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5

    while score0 < goal and score1 < goal:
        if player == 0: 
            dice_type = select_dice(score0, score1)
            number_rolls = strategy0(score0, score1) # number of dice to roll
            total = take_turn(number_rolls, score1, dice_type) # roll the dice
            if total == 0: # piggy back
               score1 += number_rolls
        
            score0 += total # update the current player's score

            if is_swap(score0, score1): # swine swap
                score0, score1 = score1, score0
    
        else:
            dice_type = select_dice(score1, score0)
            number_rolls = strategy1(score1, score0)
            total = take_turn(number_rolls, score0, dice_type)

            if total == 0:
                score0 += number_rolls

            score1 += total
        if is_swap(score0, score1): # swine swap
            score0, score1 = score1, score0  
            # if is_swap(score1, score0):
            #     score0, score1 = score1, score0
        # switch turn
        player = other(player)
    # END Question 5
    return score0, score1

#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice() 
    3.75 #(3+1+5+6)/4
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5 #(5+6)/2

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    def average_generator(*args):
        total = 0
        counter = 0
        while counter < num_samples:
            total += fn(*args)
            counter += 1
        return total / num_samples
    return average_generator

    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    roll_num = 10
    dice_num = 10
    avr =  make_averaged(roll_dice)(roll_num, dice)
    while roll_num > 1:
        roll_num -= 1
        current_roll = make_averaged(roll_dice)(roll_num, dice)
        if current_roll >= avr:
            avr = current_roll
            dice_num = roll_num
    return dice_num

    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    free_baconed_score = free_bacon(opponent_score)
    if is_prime(free_baconed_score):
        free_baconed_score=next_prime(free_baconed_score)
    
    if free_baconed_score>= margin:
        return 0
    else:
       
        return num_rolls
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9

    def swap_digits(s):
        # swap the digits
        return int(str(s)[::-1])

    def free_bacon_simulator(current_score, other_score):
        """
        1. check if freebacon award point is a prime number.
        2. if yes, it returns next_prime()ed number
        2.5 otherwise, return the sum of freebacon award point + the current player's score.
        3. get the sum of freebacon award (already next_prime()ed) and the current player's score
        """
        freebacon_award = free_bacon(other_score)
        if is_prime(freebacon_award):
            return next_prime(freebacon_award) + current_score
        else:
            return freebacon_award + current_score

    if is_swap(score, opponent_score):
        if swap_digits(score) > opponent_score:
            return num_rolls

    updated_score = free_bacon_simulator(score, opponent_score)
    if is_swap(updated_score, opponent_score) or is_swap(score, opponent_score):
        if swap_digits(updated_score) > swap_digits(opponent_score):
            return 0
        else:
            return num_rolls
    else:
        return num_rolls

    # END Question 9

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    76.5
    return the num_rolls so that using the strategy can almost beat the always_roll(5)
    1. use swap_strategy first because there's more possiblity to get higher score than with bacon_strategy
    2. 
    """
    # BEGIN Question 10
    return bacon_strategy(score, opponent_score, margin=8, num_rolls=0)
    if score < opponent_score:
        pass
    # elif score + take_turn(0, opponent_score) >= 100:
    #     return 0
    #return 4
    # Replace this statement
    # END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
