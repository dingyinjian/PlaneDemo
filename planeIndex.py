import pygame
from pygame.locals import *
def main():
    #创建一个窗口
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('飞机小游戏')
    background = pygame.image.load('./feiji/background.png')
    hero= pygame.image.load('./feiji/hero.png')

    background = pygame.transform.scale(background, (800, 600))
    x,y=0,550
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (x,y))
        #获取键盘事件
        for event in pygame.event.get():
            if event.type == QUIT:
                print('退出')
                exit()
                pass
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    if x>0:
                        x-=5
                    pass
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    if x<800:
                        x+=5
                    pass
                elif event.key==K_SPACE:
                    print('space')
        #更新显示内容
        pygame.display.update()
if __name__ == '__main__':
    main()
