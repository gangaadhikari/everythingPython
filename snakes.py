import random
import curses

s = curses.initscr()
curses.curs_set(0)
x, y = s.getmaxyx()
w = curses.newwin(x, y, 0, 0)
w.keypad(1)
w.timeout(100)

snakeHorizontal = x/4
snakeVertical = y/4
snake = [
    [snakeVertical, snakeHorizontal],
    [snakeVertical, snakeHorizontal-1],
    [snakeVertical, snakeHorizontal-2]
]

food = [x/2, y/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    nextKey = w.getch()
    key = key if nextKey == -1 else nextKey

    if snake[0][0] in [0, x] or snake[0][1]  in [0, y] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nextFood = [
                random.randint(1, x-1),
                random.randint(1, y-1)
            ]
            food = nextFood if nextFood not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)


w.addch(int(food[0]), int(food[1]), curses.ACS_PI)