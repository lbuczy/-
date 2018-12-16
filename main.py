from tkinter import *

root = Tk()
root.title("五子棋")
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
direction = [[0, 1],
             [-1, 0],
             [-1, -1],
             [0, -1],
             [-1, 1],
             [1, 0],
             [1, 1],
             [1, -1]
             ]
turn_who = 1  # 黑棋先走
checkerboard = Canvas(root, width=300, height=300, bg='white')
source = 0


def paint(event):
    global turn_who

    class Point:
        pass

    # 使下子落在网格上
    Point.x = int(event.x / 30) * 30
    if event.x % 30 > 15:
        Point.x = 30 + Point.x
    Point.y = int(event.y / 30) * 30
    if event.y % 30 > 15:
        Point.y = 30 + Point.y
    #  画出棋子
    x1, y1 = (Point.x - 10), (Point.y - 10)
    x2, y2 = (Point.x + 10), (Point.y + 10)
    if turn_who:
        fill_color = 'black'
    else:
        fill_color = 'white'
    checkerboard.create_oval(x1, y1, x2, y2, fill=fill_color)
    turn_who = turn_who + 1
    if turn_who > 1:
        turn_who = 0
    Point.x = Point.x / 30 - 1
    Point.y = Point.y / 30 - 1
    board_update(int(Point.x), int(Point.y))
    pre_judge(int(Point.x), int(Point.y))


def draw_con():
    #  绘制格子
    for num in range(1, 10):
        checkerboard.create_line(num * 30, 30, num * 30, 270, width=2)
    for num in range(1, 10):
        checkerboard.create_line(30, num * 30, 270, num * 30, width=2)


def board_update(x, y):
    if turn_who:
        board[x][y] = 1
    else:
        board[x][y] = 2
    # print(board)


def pre_judge(x, y):
    global source
    source = 0
    if turn_who == 0:
        judge_black(x, y)
    else:
        judge_white(x, y)


def judge_black(x, y):
    global source
    for i in range(0, 7):
        if board[x + direction[i][0]][y + direction[i][1]] == 2:
            source = 0
            judge_black1(x, y, i)


def judge_black1(x, y, i):
    global source
    if board[x + direction[i][0]][y + direction[i][1]] == 2:
        source = source + 1
        judge_black1(x + direction[i][0], y + direction[i][1], i)
    if source >= 4:
        print('black win')


def judge_white(x, y):
    global source
    for i in range(0, 7):
        if board[x + direction[i][0]][y + direction[i][1]] == 1:
            source = 0
            judge_white1(x, y, i)


def judge_white1(x, y, i):
    global source
    if board[x + direction[i][0]][y + direction[i][1]] == 1:
        source = source + 1
        judge_white1(x + direction[i][0], y + direction[i][1], i)
    if source >= 4:
        print('white win')


if __name__ == '__main__':
    draw_con()
    checkerboard.bind(sequence='<Button-1>', func=paint)
    checkerboard.pack(fill=BOTH)
    root.mainloop()
