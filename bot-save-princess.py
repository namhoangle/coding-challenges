"""Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move
 one step at a time in any of the four directions. Can you rescue the princess?

Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid.
Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output format

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline.
The valid moves are LEFT or RIGHT or UP or DOWN.

Sample input

>>> 3
>>> ---
>>> -m-
>>> p--
Sample output

DOWN
LEFT
Task

Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the character array grid.
The grid will be formatted exactly as you see it in the input, so for the sample input the princess is at grid[2][0].
The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. The goal
is to reach the princess in as few moves as possible.

The above sample input is just to help you understand the format. The princess ('p') can be in any one of the four corners.

Scoring
Your score is calculated as follows : (NxN - number of moves made to rescue the princess)/10, where N is the size of
the grid (3x3 in the sample testcase).

Solved score: 13.90pts

Submissions: 80065
Max Score: 13
Difficulty: Easy
Rate This Challenge:

More
"""


def displayPathtoPrincess(n, grid):

    # find the position of the bot and the princess
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot_position = (i, j)
            elif grid[i][j] == 'p':
                princess_position = (i, j)

    # find the difference between the bot and the princess
    diff = (princess_position[0] - bot_position[0], princess_position[1] - bot_position[1])

    answer = ''
    # move the bot to the princess
    if diff[0] > 0:
        for i in range(diff[0]):
            answer += 'DOWN'
            answer += '\n'
    elif diff[0] < 0:
        for i in range(abs(diff[0])):
            answer += 'UP'
            answer += '\n'

    if diff[1] > 0:
        for i in range(diff[1]):
            answer += 'RIGHT'
            answer += '\n'

    elif diff[1] < 0:
        for i in range(abs(diff[1])):
            answer += 'LEFT'
            answer += '\n'


    return answer



if __name__ == '__main__':
    print('Welcome to the Bot Save Princess Challenge!')
    print('Test mode? (y/n): ')
    test_mode = input()
    if test_mode == 'y':
        # test mode
        test_cases = [
            {
                'grid_size': 4,
                'grid': [
                    '----',
                    '--m-',
                    '----',
                    'p---'
                ],
                'expected_output': 'DOWN\nDOWN\nLEFT\nLEFT\n'
            },
        ]

        answer = displayPathtoPrincess(test_cases[0]['grid_size'], test_cases[0]['grid'])

        print('Answer: ', answer)
        print('Expected answer: ', test_cases[0]['expected_output'])

        if answer == test_cases[0]['expected_output']:
            print('Test case 1 passed!')

        assert answer == test_cases[0]['expected_output']

    else:

        # prompt user to enter grid size, which is an odd integer N (3 <= N < 100) denoting the size of the grid
        print("Enter the grid size: ")
        grid_size = int(input())
        # prompt user to enter grid, which is an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position
        # is denoted by 'm' and the princess position is denoted by 'p'.
        print("Enter the grid: ")
        grid = []
        for i in range(grid_size):
            grid.append(input().strip())
        print(grid)
        displayPathtoPrincess(grid_size, grid)