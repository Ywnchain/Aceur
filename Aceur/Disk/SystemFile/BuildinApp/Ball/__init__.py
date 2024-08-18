WIDTH = 60
HEIGHT = 20

# 球的初始位置和速度
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_vx, ball_vy = 1, 1

# 挡板的初始位置和大小
paddle_x, paddle_y = WIDTH // 2, HEIGHT - 2
paddle_width = 10

# 当前得分
score = 0

# 初始化屏幕
screen = [' ' * (WIDTH + 1) for _ in range(HEIGHT)]


def main(blver):
    import os
    import time

    # 游戏区域大小
    WIDTH = 60
    HEIGHT = 20

    # 球的初始位置和速度
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_vx, ball_vy = 1, 1

    # 挡板的初始位置和大小
    paddle_x, paddle_y = WIDTH // 2, HEIGHT - 2
    paddle_width = 10

    # 当前得分
    score = 0

    # 初始化屏幕
    screen = [' '*(WIDTH+1) for _ in range(HEIGHT)]

    # 更新屏幕内容
    def update():
        global ball_x, ball_y, ball_vx, ball_vy, paddle_x, score

        # 擦除球之前的痕迹
        screen[ball_y] = screen[ball_y][:ball_x] + ' ' + screen[ball_y][ball_x+1:]

        # 移动球
        ball_x += ball_vx
        ball_y += ball_vy

        # 判断球是否撞到左右边界
        if ball_x <= 0 or ball_x >= WIDTH-1:
            ball_vx *= -1

        # 判断球是否撞到上边界
        if ball_y <= 0:
            ball_vy *= -1

        # 判断球是否撞到挡板
        if ball_y == paddle_y - 1 and ball_vy > 0 and paddle_x <= ball_x < paddle_x+paddle_width:
            ball_vy *= -1
            score += 1

        # 判断球是否撞到下边界（游戏结束）
        if ball_y >= HEIGHT-1:
            print('Game Over! Your score is: %d' % score)


        # 更新屏幕
        screen[ball_y] = screen[ball_y][:ball_x] + 'O' + screen[ball_y][ball_x+1:]
        screen[paddle_y] = (' ' * (paddle_x - paddle_width // 2) + '=' * paddle_width +
                             ' ' * (WIDTH - paddle_x - paddle_width // 2))

        # 清屏
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        # 输出当前得分和屏幕内容
        print('Score: %d' % score)
        for row in screen:
            print(row)


    # 主循环
    while True:
        # 擦除球之前的痕迹
        screen[ball_y] = screen[ball_y][:ball_x] + ' ' + screen[ball_y][ball_x + 1:]

        # 移动球
        ball_x += ball_vx
        ball_y += ball_vy

        # 判断球是否撞到左右边界
        if ball_x <= 0 or ball_x >= WIDTH - 1:
            ball_vx *= -1

        # 判断球是否撞到上边界
        if ball_y <= 0:
            ball_vy *= -1

        # 判断球是否撞到挡板
        if ball_y == paddle_y - 1 and ball_vy > 0 and paddle_x <= ball_x < paddle_x + paddle_width:
            ball_vy *= -1
            score += 1

        # 判断球是否撞到下边界（游戏结束）
        if ball_y >= HEIGHT - 1:
            print('Game Over! Your score is: %d' % score)
            break
        time.sleep(0.1)

        # 按键检测（左右箭头移动挡板）
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                key = ord(msvcrt.getch())
                if key == 224:  # 特殊键前缀
                    key = ord(msvcrt.getch())
                    if key == 75 and paddle_x > paddle_width // 2:
                        paddle_x -= 3
                    if key == 77 and paddle_x < WIDTH - paddle_width // 2:
                        paddle_x += 3
        else:
            import sys, termios, tty
            settings = termios.tcgetattr(sys.stdin)
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)[0]
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
            if key == 'a' and paddle_x > paddle_width // 2:
                paddle_x -= 3
            if key == 'd' and paddle_x < WIDTH - paddle_width // 2:
                paddle_x += 3
