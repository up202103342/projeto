import pygame
from random import randint

pygame.mixer.init()

kill = True
counting = False
five_second_counter = 0
current_level = 1      
movement_toggle = True
score = 0
level = 1
lives = 4
fruit_out = False
special_extra_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
multiplier = 1
update_multiplier = False
gameover = True

cheats = False

pause = False

ladybug_animation_stage = 0

latest_key_pressed = 'up'

pink_background = pygame.image.load('imgs/pink_background.png')
pink_obstacles = pygame.image.load('imgs/pink_obstacles.png')

ladybug_up_1 = pygame.image.load('imgs/ladybug_up_1.png')
ladybug_up_2 = pygame.image.load('imgs/ladybug_up_2.png')
ladybug_up_3 = pygame.image.load('imgs/ladybug_up_3.png')
ladybug_up_4 = pygame.image.load('imgs/ladybug_up_4.png')
ladybug_up_5 = pygame.image.load('imgs/ladybug_up_5.png')
ladybug_up_6 = pygame.image.load('imgs/ladybug_up_6.png')
ladybug_up_7 = pygame.image.load('imgs/ladybug_up_7.png')
ladybug_down_1 = pygame.image.load('imgs/ladybug_down_1.png')
ladybug_down_2 = pygame.image.load('imgs/ladybug_down_2.png')
ladybug_down_3 = pygame.image.load('imgs/ladybug_down_3.png')
ladybug_down_4 = pygame.image.load('imgs/ladybug_down_4.png')
ladybug_down_5 = pygame.image.load('imgs/ladybug_down_5.png')
ladybug_down_6 = pygame.image.load('imgs/ladybug_down_6.png')
ladybug_down_7 = pygame.image.load('imgs/ladybug_down_7.png')
ladybug_left_1 = pygame.image.load('imgs/ladybug_left_1.png')
ladybug_left_2 = pygame.image.load('imgs/ladybug_left_2.png')
ladybug_left_3 = pygame.image.load('imgs/ladybug_left_3.png')
ladybug_left_4 = pygame.image.load('imgs/ladybug_left_4.png')
ladybug_left_5 = pygame.image.load('imgs/ladybug_left_5.png')
ladybug_left_6 = pygame.image.load('imgs/ladybug_left_6.png')
ladybug_left_7 = pygame.image.load('imgs/ladybug_left_7.png')
ladybug_right_1 = pygame.image.load('imgs/ladybug_right_1.png')
ladybug_right_2 = pygame.image.load('imgs/ladybug_right_2.png')
ladybug_right_3 = pygame.image.load('imgs/ladybug_right_3.png')
ladybug_right_4 = pygame.image.load('imgs/ladybug_right_4.png')
ladybug_right_5 = pygame.image.load('imgs/ladybug_right_5.png')
ladybug_right_6 = pygame.image.load('imgs/ladybug_right_6.png')
ladybug_right_7 = pygame.image.load('imgs/ladybug_right_7.png')

b1p1up = pygame.image.load('imgs/bug1pos1up.png')
b1p2up = pygame.image.load('imgs/bug1pos2up.png')
b1p3up = pygame.image.load('imgs/bug1pos3up.png')
b1p4up = pygame.image.load('imgs/bug1pos4up.png')
b1p1right = pygame.image.load('imgs/bug1pos1right.png')
b1p2right = pygame.image.load('imgs/bug1pos2right.png')
b1p3right = pygame.image.load('imgs/bug1pos3right.png')
b1p4right = pygame.image.load('imgs/bug1pos4right.png')
b1p1down = pygame.image.load('imgs/bug1pos1down.png')
b1p2down = pygame.image.load('imgs/bug1pos2down.png')
b1p3down = pygame.image.load('imgs/bug1pos3down.png')
b1p4down = pygame.image.load('imgs/bug1pos4down.png')
b1p1left = pygame.image.load('imgs/bug1pos1left.png')
b1p2left = pygame.image.load('imgs/bug1pos2left.png')
b1p3left = pygame.image.load('imgs/bug1pos3left.png')
b1p4left = pygame.image.load('imgs/bug1pos4left.png')
bug1 = [[b1p1up, b1p2up, b1p3up, b1p4up],
        [b1p1right, b1p2right, b1p3right, b1p4right],
        [b1p1down, b1p2down, b1p3down, b1p4down],
        [b1p1left, b1p2left, b1p3left, b1p4left]]
b2p1up = pygame.image.load('imgs/bug2pos1up.png')
b2p2up = pygame.image.load('imgs/bug2pos2up.png')
b2p3up = pygame.image.load('imgs/bug2pos3up.png')
b2p4up = pygame.image.load('imgs/bug2pos4up.png')
b2p1right = pygame.image.load('imgs/bug2pos1right.png')
b2p2right = pygame.image.load('imgs/bug2pos2right.png')
b2p3right = pygame.image.load('imgs/bug2pos3right.png')
b2p4right = pygame.image.load('imgs/bug2pos4right.png')
b2p1down = pygame.image.load('imgs/bug2pos1down.png')
b2p2down = pygame.image.load('imgs/bug2pos2down.png')
b2p3down = pygame.image.load('imgs/bug2pos3down.png')
b2p4down = pygame.image.load('imgs/bug2pos4down.png')
b2p1left = pygame.image.load('imgs/bug2pos1left.png')
b2p2left = pygame.image.load('imgs/bug2pos2left.png')
b2p3left = pygame.image.load('imgs/bug2pos3left.png')
b2p4left = pygame.image.load('imgs/bug2pos4left.png')
bug2 = [[b2p1up, b2p2up, b2p3up, b2p4up],
        [b2p1right, b2p2right, b2p3right, b2p4right],
        [b2p1down, b2p2down, b2p3down, b2p4down],
        [b2p1left, b2p2left, b2p3left, b2p4left]]
b3p1up = pygame.image.load('imgs/bug3pos1up.png')
b3p2up = pygame.image.load('imgs/bug3pos2up.png')
b3p3up = pygame.image.load('imgs/bug3pos3up.png')
b3p4up = pygame.image.load('imgs/bug3pos4up.png')
b3p1right = pygame.image.load('imgs/bug3pos1right.png')
b3p2right = pygame.image.load('imgs/bug3pos2right.png')
b3p3right = pygame.image.load('imgs/bug3pos3right.png')
b3p4right = pygame.image.load('imgs/bug3pos4right.png')
b3p1down = pygame.image.load('imgs/bug3pos1down.png')
b3p2down = pygame.image.load('imgs/bug3pos2down.png')
b3p3down = pygame.image.load('imgs/bug3pos3down.png')
b3p4down = pygame.image.load('imgs/bug3pos4down.png')
b3p1left = pygame.image.load('imgs/bug3pos1left.png')
b3p2left = pygame.image.load('imgs/bug3pos2left.png')
b3p3left = pygame.image.load('imgs/bug3pos3left.png')
b3p4left = pygame.image.load('imgs/bug3pos4left.png')
bug3 = [[b3p1up, b3p2up, b3p3up, b3p4up],
        [b3p1right, b3p2right, b3p3right, b3p4right],
        [b3p1down, b3p2down, b3p3down, b3p4down],
        [b3p1left, b3p2left, b3p3left, b3p4left]]
b4p1up = pygame.image.load('imgs/bug4pos1up.png')
b4p2up = pygame.image.load('imgs/bug4pos2up.png')
b4p3up = pygame.image.load('imgs/bug4pos3up.png')
b4p4up = pygame.image.load('imgs/bug4pos4up.png')
b4p1right = pygame.image.load('imgs/bug4pos1right.png')
b4p2right = pygame.image.load('imgs/bug4pos2right.png')
b4p3right = pygame.image.load('imgs/bug4pos3right.png')
b4p4right = pygame.image.load('imgs/bug4pos4right.png')
b4p1down = pygame.image.load('imgs/bug4pos1down.png')
b4p2down = pygame.image.load('imgs/bug4pos2down.png')
b4p3down = pygame.image.load('imgs/bug4pos3down.png')
b4p4down = pygame.image.load('imgs/bug4pos4down.png')
b4p1left = pygame.image.load('imgs/bug4pos1left.png')
b4p2left = pygame.image.load('imgs/bug4pos2left.png')
b4p3left = pygame.image.load('imgs/bug4pos3left.png')
b4p4left = pygame.image.load('imgs/bug4pos4left.png')
bug4 = [[b4p1up, b4p2up, b4p3up, b4p4up],
        [b4p1right, b4p2right, b4p3right, b4p4right],
        [b4p1down, b4p2down, b4p3down, b4p4down],
        [b4p1left, b4p2left, b4p3left, b4p4left]]
b5p1up = pygame.image.load('imgs/bug5pos1up.png')
b5p2up = pygame.image.load('imgs/bug5pos2up.png')
b5p3up = pygame.image.load('imgs/bug5pos3up.png')
b5p4up = pygame.image.load('imgs/bug5pos4up.png')
b5p1right = pygame.image.load('imgs/bug5pos1right.png')
b5p2right = pygame.image.load('imgs/bug5pos2right.png')
b5p3right = pygame.image.load('imgs/bug5pos3right.png')
b5p4right = pygame.image.load('imgs/bug5pos4right.png')
b5p1down = pygame.image.load('imgs/bug5pos1down.png')
b5p2down = pygame.image.load('imgs/bug5pos2down.png')
b5p3down = pygame.image.load('imgs/bug5pos3down.png')
b5p4down = pygame.image.load('imgs/bug5pos4down.png')
b5p1left = pygame.image.load('imgs/bug5pos1left.png')
b5p2left = pygame.image.load('imgs/bug5pos2left.png')
b5p3left = pygame.image.load('imgs/bug5pos3left.png')
b5p4left = pygame.image.load('imgs/bug5pos4left.png')
bug5 = [[b5p1up, b5p2up, b5p3up, b5p4up],
        [b5p1right, b5p2right, b5p3right, b5p4right],
        [b5p1down, b5p2down, b5p3down, b5p4down],
        [b5p1left, b5p2left, b5p3left, b5p4left]]
b6p1up = pygame.image.load('imgs/bug6pos1up.png')
b6p2up = pygame.image.load('imgs/bug6pos2up.png')
b6p3up = pygame.image.load('imgs/bug6pos3up.png')
b6p4up = pygame.image.load('imgs/bug6pos4up.png')
b6p1right = pygame.image.load('imgs/bug6pos1right.png')
b6p2right = pygame.image.load('imgs/bug6pos2right.png')
b6p3right = pygame.image.load('imgs/bug6pos3right.png')
b6p4right = pygame.image.load('imgs/bug6pos4right.png')
b6p1down = pygame.image.load('imgs/bug6pos1down.png')
b6p2down = pygame.image.load('imgs/bug6pos2down.png')
b6p3down = pygame.image.load('imgs/bug6pos3down.png')
b6p4down = pygame.image.load('imgs/bug6pos4down.png')
b6p1left = pygame.image.load('imgs/bug6pos1left.png')
b6p2left = pygame.image.load('imgs/bug6pos2left.png')
b6p3left = pygame.image.load('imgs/bug6pos3left.png')
b6p4left = pygame.image.load('imgs/bug6pos4left.png')
bug6 = [[b6p1up, b6p2up, b6p3up, b6p4up],
        [b6p1right, b6p2right, b6p3right, b6p4right],
        [b6p1down, b6p2down, b6p3down, b6p4down],
        [b6p1left, b6p2left, b6p3left, b6p4left]]
b7p1up = pygame.image.load('imgs/bug7pos1up.png')
b7p2up = pygame.image.load('imgs/bug7pos2up.png')
b7p3up = pygame.image.load('imgs/bug7pos3up.png')
b7p4up = pygame.image.load('imgs/bug7pos4up.png')
b7p1right = pygame.image.load('imgs/bug7pos1right.png')
b7p2right = pygame.image.load('imgs/bug7pos2right.png')
b7p3right = pygame.image.load('imgs/bug7pos3right.png')
b7p4right = pygame.image.load('imgs/bug7pos4right.png')
b7p1down = pygame.image.load('imgs/bug7pos1down.png')
b7p2down = pygame.image.load('imgs/bug7pos2down.png')
b7p3down = pygame.image.load('imgs/bug7pos3down.png')
b7p4down = pygame.image.load('imgs/bug7pos4down.png')
b7p1left = pygame.image.load('imgs/bug7pos1left.png')
b7p2left = pygame.image.load('imgs/bug7pos2left.png')
b7p3left = pygame.image.load('imgs/bug7pos3left.png')
b7p4left = pygame.image.load('imgs/bug7pos4left.png')
bug7 = [[b7p1up, b7p2up, b7p3up, b7p4up],
        [b7p1right, b7p2right, b7p3right, b7p4right],
        [b7p1down, b7p2down, b7p3down, b7p4down],
        [b7p1left, b7p2left, b7p3left, b7p4left]]
b8p1up = pygame.image.load('imgs/bug8pos1up.png')
b8p2up = pygame.image.load('imgs/bug8pos2up.png')
b8p3up = pygame.image.load('imgs/bug8pos3up.png')
b8p4up = pygame.image.load('imgs/bug8pos4up.png')
b8p1right = pygame.image.load('imgs/bug8pos1right.png')
b8p2right = pygame.image.load('imgs/bug8pos2right.png')
b8p3right = pygame.image.load('imgs/bug8pos3right.png')
b8p4right = pygame.image.load('imgs/bug8pos4right.png')
b8p1down = pygame.image.load('imgs/bug8pos1down.png')
b8p2down = pygame.image.load('imgs/bug8pos2down.png')
b8p3down = pygame.image.load('imgs/bug8pos3down.png')
b8p4down = pygame.image.load('imgs/bug8pos4down.png')
b8p1left = pygame.image.load('imgs/bug8pos1left.png')
b8p2left = pygame.image.load('imgs/bug8pos2left.png')
b8p3left = pygame.image.load('imgs/bug8pos3left.png')
b8p4left = pygame.image.load('imgs/bug8pos4left.png')
bug8 = [[b8p1up, b8p2up, b8p3up, b8p4up],
        [b8p1right, b8p2right, b8p3right, b8p4right],
        [b8p1down, b8p2down, b8p3down, b8p4down],
        [b8p1left, b8p2left, b8p3left, b8p4left]]
bugs = [bug1, bug2, bug3, bug4, bug5, bug6, bug7, bug8]

fruit_1 = pygame.image.load('imgs/fruit1.png')
fruit_2 = pygame.image.load('imgs/fruit2.png')
fruit_3 = pygame.image.load('imgs/fruit3.png')
fruit_4 = pygame.image.load('imgs/fruit4.png')
fruit_5 = pygame.image.load('imgs/fruit5.png')
fruit_6 = pygame.image.load('imgs/fruit6.png')
fruit_7 = pygame.image.load('imgs/fruit7.png')
fruit_8 = pygame.image.load('imgs/fruit8.png')
fruit_9 = pygame.image.load('imgs/fruit9.png')
fruit_10 = pygame.image.load('imgs/fruit10.png')
fruit_11 = pygame.image.load('imgs/fruit11.png')
fruit_12 = pygame.image.load('imgs/fruit12.png')
fruit_13 = pygame.image.load('imgs/fruit13.png')
fruit_14 = pygame.image.load('imgs/fruit14.png')
fruit_15 = pygame.image.load('imgs/fruit15.png')
fruit_16 = pygame.image.load('imgs/fruit16.png')
fruit_17 = pygame.image.load('imgs/fruit17.png')
fruit_18 = pygame.image.load('imgs/fruit18.png')

fruit_list = [fruit_1, fruit_2, fruit_3, fruit_4, fruit_5, fruit_6, fruit_7, fruit_8, fruit_9, 
              fruit_10, fruit_11, fruit_12, fruit_13, fruit_14, fruit_15, fruit_16, fruit_17, fruit_18]

extra_background = pygame.image.load('imgs/extra_background.png')

ladybug_list = [[ladybug_up_1, ladybug_up_2, ladybug_up_3, ladybug_up_4, ladybug_up_5, ladybug_up_6, ladybug_up_7, ladybug_up_6, ladybug_up_5, ladybug_up_4, ladybug_up_3, ladybug_up_2],
                [ladybug_down_1, ladybug_down_2, ladybug_down_3, ladybug_down_4, ladybug_down_5, ladybug_down_6, ladybug_down_7, ladybug_down_6, ladybug_down_5, ladybug_down_4, ladybug_down_3, ladybug_down_2],
                [ladybug_left_1, ladybug_left_2, ladybug_left_3, ladybug_left_4, ladybug_left_5, ladybug_left_6, ladybug_left_7, ladybug_left_6, ladybug_left_5, ladybug_left_4, ladybug_left_3, ladybug_left_2],
                [ladybug_right_1, ladybug_right_2, ladybug_right_3, ladybug_right_4, ladybug_right_5, ladybug_right_6, ladybug_right_7, ladybug_right_6, ladybug_right_5, ladybug_right_4, ladybug_right_3, ladybug_right_2]]

d0 = pygame.image.load('imgs/0.png')
d1 = pygame.image.load('imgs/1.png')
d2 = pygame.image.load('imgs/2.png')
d3 = pygame.image.load('imgs/3.png')
d4 = pygame.image.load('imgs/4.png')
d5 = pygame.image.load('imgs/5.png')
d6 = pygame.image.load('imgs/6.png')
d7 = pygame.image.load('imgs/7.png')
d8 = pygame.image.load('imgs/8.png')
d9 = pygame.image.load('imgs/9.png')
p100x1 = pygame.image.load('imgs/100x1.png')
p100x2 = pygame.image.load('imgs/100x2.png')
p100x3 = pygame.image.load('imgs/100x3.png')
p100x5 = pygame.image.load('imgs/100x5.png')
p300x1 = pygame.image.load('imgs/300x1.png')
p300x2 = pygame.image.load('imgs/300x2.png')
p300x3 = pygame.image.load('imgs/300x3.png')
p300x5 = pygame.image.load('imgs/300x5.png')
p800x1 = pygame.image.load('imgs/800x1.png')
p800x2 = pygame.image.load('imgs/800x2.png')
p800x3 = pygame.image.load('imgs/800x3.png')
p800x5 = pygame.image.load('imgs/800x5.png')
red_S = pygame.image.load('imgs/red_S.png')
red_P = pygame.image.load('imgs/red_P.png')
red_E = pygame.image.load('imgs/red_E.png')
red_C = pygame.image.load('imgs/red_C.png')
red_I = pygame.image.load('imgs/red_I.png')
red_A = pygame.image.load('imgs/red_A.png')
red_L = pygame.image.load('imgs/red_L.png')
red_X = pygame.image.load('imgs/red_X.png')
red_T = pygame.image.load('imgs/red_T.png')
red_R = pygame.image.load('imgs/red_R.png')
red_heart = pygame.image.load('imgs/red_heart.png')
green_S = pygame.image.load('imgs/green_S.png')
green_P = pygame.image.load('imgs/green_P.png')
green_E = pygame.image.load('imgs/green_E.png')
green_C = pygame.image.load('imgs/green_C.png')
green_I = pygame.image.load('imgs/green_I.png')
green_A = pygame.image.load('imgs/green_A.png')
green_L = pygame.image.load('imgs/green_L.png')
green_X = pygame.image.load('imgs/green_X.png')
green_T = pygame.image.load('imgs/green_T.png')
green_R = pygame.image.load('imgs/green_R.png')
green_heart = pygame.image.load('imgs/green_heart.png')
blue_S = pygame.image.load('imgs/blue_S.png')
blue_P = pygame.image.load('imgs/blue_P.png')
blue_E = pygame.image.load('imgs/blue_E.png')
blue_C = pygame.image.load('imgs/blue_C.png')
blue_I = pygame.image.load('imgs/blue_I.png')
blue_A = pygame.image.load('imgs/blue_A.png')
blue_L = pygame.image.load('imgs/blue_L.png')
blue_X = pygame.image.load('imgs/blue_X.png')
blue_T = pygame.image.load('imgs/blue_T.png')
blue_R = pygame.image.load('imgs/blue_R.png')
blue_heart = pygame.image.load('imgs/blue_heart.png')
skull = pygame.image.load('imgs/skull.png')
dead1 = pygame.image.load('imgs/dead.png')
dead2 = pygame.image.load('imgs/dead2.png')
dead3 = pygame.image.load('imgs/dead3.png')
dead4 = pygame.image.load('imgs/dead4.png')
dead5 = pygame.image.load('imgs/dead5.png')
angel = pygame.image.load('imgs/angel.png')

game_over = pygame.image.load('imgs/game_over.png')

lvl_1 = pygame.image.load('imgs/lvl_1.png')
lvl_2 = pygame.image.load('imgs/lvl_2.png')
lvl_3 = pygame.image.load('imgs/lvl_3.png')
lvl_4 = pygame.image.load('imgs/lvl_4.png')
lvl_5 = pygame.image.load('imgs/lvl_5.png')
lvl_6 = pygame.image.load('imgs/lvl_6.png')
lvl_7 = pygame.image.load('imgs/lvl_7.png')
lvl_8 = pygame.image.load('imgs/lvl_8.png')
lvl_9 = pygame.image.load('imgs/lvl_9.png')
lvl_10 = pygame.image.load('imgs/lvl_10.png')
lvl_11 = pygame.image.load('imgs/lvl_11.png')
lvl_12 = pygame.image.load('imgs/lvl_12.png')
lvl_13 = pygame.image.load('imgs/lvl_13.png')
lvl_14 = pygame.image.load('imgs/lvl_14.png')
lvl_15 = pygame.image.load('imgs/lvl_15.png')
lvl_16 = pygame.image.load('imgs/lvl_16.png')
lvl_17 = pygame.image.load('imgs/lvl_17.png')
lvl_18 = pygame.image.load('imgs/lvl_18.png')
lvl_19 = pygame.image.load('imgs/lvl_19.png')
b0 = pygame.image.load('imgs/0b.png')
b1 = pygame.image.load('imgs/1b.png')
b2 = pygame.image.load('imgs/2b.png')
b3 = pygame.image.load('imgs/3b.png')
b4 = pygame.image.load('imgs/4b.png')
b5 = pygame.image.load('imgs/5b.png')
b6 = pygame.image.load('imgs/6b.png')
b7 = pygame.image.load('imgs/7b.png')
b8 = pygame.image.load('imgs/8b.png')
b9 = pygame.image.load('imgs/9b.png')
blue_digit_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9]



black = pygame.image.load('imgs/black.png')

digit_list = [0, -1, -1, -1, -1, -1, -1, -1]
digit_coord_list = [(382, 396), (350, 396), (318, 396), (286, 396), (254, 396), (222, 396), (190, 396), (158, 396)]

border_color_change_list = [((0, 0, 0), (0, 0, 0)), ((314, 50, 1), (330, 50, 1)), ((298, 50, 1), (346, 50, 1)), ((282, 50, 1), (362, 50, 1)), 
                            ((266, 50, 1), (378, 50, 1)), ((250, 50, 1), (394, 50, 1)), ((234, 50, 1), (410, 50, 1)), ((218, 50, 1), (426, 50, 1)), 
                            ((202, 50, 1), (442, 50, 1)), ((186, 50, 1), (458, 50, 1)), ((170, 50, 1), (474, 50, 1)), ((154, 50, 1), (490, 50, 1)), 
                            ((138, 50, 1), (506, 50, 1)), ((122, 50, 1), (522, 50, 1)), ((106, 50, 1), (538, 50, 1)), ((90, 50, 1), (554, 50, 1)), 
                            ((74, 50, 1), (570, 50, 1)), ((58, 50, 1), (586, 50, 1)),
                            ((58,58,2), (586,58,2)), ((58,76,2), (586,76,2)), ((58,94,2), (586,94,2)), ((58,112,2), (586,112,2)),
                            ((58,130,2), (586,130,2)), ((58,148,2), (586,148,2)), ((58,166,2), (586,166,2)), ((58,184,2), (586,184,2)),
                            ((58,202,2), (586,202,2)), ((58,220,2), (586,220,2)), ((58,238,2), (586,238,2)), ((58,256,2), (586,256,2)),
                            ((58,274,2), (586,274,2)), ((58,292,2), (586,292,2)), ((58,310,2), (586,310,2)), ((58,328,2), (586,328,2)), 
                            ((58,346,3), (586,346,3)),
                            ((74,358,1),(570,358,1)), ((90,358,1),(554,358,1)), ((106,358,1),(538,358,1)), ((122,358,1),(522,358,1)),
                            ((138,358,1),(506,358,1)), ((154,358,1),(490,358,1)), ((170,358,1),(474,358,1)), ((186,358,1),(458,358,1)),
                            ((202,358,1),(442,358,1)), ((218,358,1),(426,358,1)), ((234,358,1),(410,358,1)), ((250,358,1),(394,358,1)),
                            ((266,358,1),(378,358,1)), ((282,358,1),(362,358,1)), ((298,358,1),(346,358,1)), ((314,358,1),(330,358,1)),
                            ((0, 0, 0), (0, 0, 0))]

border_h_green = pygame.image.load('imgs/border_horizontal_green.png')
border_v_green = pygame.image.load('imgs/border_vertical_green.png')
border_v_green2 = pygame.image.load('imgs/border_vertical_green2.png')


lx = [74, 122, 170, 218, 266, 314, 362, 410, 458, 506, 554] #list of x at which Ladybug can be when in a column
ly = [56, 90, 124, 158, 192, 226, 260, 294, 328] #list of y at which ladybug can be when in a row

lxb = [74, 122, 170, 218, 266, 314, 362, 410, 458, 506, 554]
lyb = [56, 90, 124, 158, 192, 226, 260, 294, 328]

mx = [[], [74, 122, 170, 218, 314, 410, 458, 506, 554],
      [74, 170, 218, 266, 314, 362, 410, 458, 554],
      [74, 122, 170, 218, 314, 410, 458, 506, 554],
      [74, 170, 218, 266, 314, 362, 410, 458, 554],
      [74, 122, 170, 218, 266, 362, 410, 458, 506, 554],
      [74, 170, 218, 314, 410, 458, 554],
      [74, 218, 266, 314, 362, 410, 554],
      [74, 122, 170, 266, 314, 362, 458, 506, 554], []]

my = [[], [56, 124, 158, 192, 260, 328],
      [56, 90, 124, 192, 226, 260, 294, 328],
      [56, 124, 192, 260, 294, 328],
      [56, 90, 124, 192, 226, 260, 294, 328],
      [56, 124, 158, 226, 260, 328],
      [56, 124, 158, 226, 260, 328],
      [56, 90, 124, 192, 226, 260, 294, 328],
      [56, 124, 192, 260, 294, 328],
      [56, 90, 124, 192, 226, 260, 294, 328],
      [56, 124, 158, 192, 260, 328], []]

object_coords = [[(74, 56), (122, 56), (170, 56), (218, 56), (266, 56), (362, 56), (410, 56), (458, 56), (506, 56), (554, 56)],
                  [(74, 90), (122, 90), (170, 90), (218, 90), (266, 90), (362, 90), (410, 90), (458, 90), (506, 90), (554, 90)],
                  [(74, 124), (122, 124), (170, 124), (218, 124), (266, 124), (362, 124), (410, 124), (458, 124), (506, 124), (554, 124)],
                  [(74, 158), (122, 158), (170, 158), (218, 158), (266, 158), (362, 158), (410, 158), (458, 158), (506, 158), (554, 158)],
                  [(74, 192), (122, 192), (170, 192), (218, 192), (266, 192), (362, 192), (410, 192), (458, 192), (506, 192), (554, 192)],
                  [(74, 226), (122, 226), (170, 226), (218, 226), (266, 226), (362, 226), (410, 226), (458, 226), (506, 226), (554, 226)],
                  [(74, 260), (122, 260), (170, 260), (218, 260), (266, 260), (362, 260), (410, 260), (458, 260), (506, 260), (554, 260)],
                  [(74, 294), (122, 294), (170, 294), (218, 294), (266, 294), (362, 294), (410, 294), (458, 294), (506, 294), (554, 294)],
                  [(74, 328), (122, 328), (170, 328), (218, 328), (266, 328), (362, 328), (410, 328), (458, 328), (506, 328), (554, 328)]]



door_h_coords = [(122,86), (74,154), (122,222), (122,324), (218,120), (218,222), (218,290), (362,120), (362,222), (362,290), (458,86), (506,154), (458,222), (458,324)]
door_v_coords = [(154,58), (106,126), (154,194), (154,296), (250,92), (250,194), (250,262), (394,92), (394,194), (394,262), (490,58), (538,126), (490,194), (490,296)]

SCREEN_SIZE = (660, 420)
screen = pygame.display.set_mode(SCREEN_SIZE)

ladybug_speed = 1.8

left_key = right_key = up_key = down_key = False
running = True

background = pygame.image.load('imgs/background.png')
obstacles = pygame.image.load('imgs/obstacles.png')
starting_animation_block = pygame.image.load('imgs/animation_block.png')
door_h = pygame.image.load('imgs/door_horizontal.png')        
door_v = pygame.image.load('imgs/door_vertical.png')
bar_right = pygame.image.load("imgs/bar_right.png")
bar_left = pygame.image.load("imgs/bar_left.png")
special_extra = pygame.image.load('imgs/special_extra.png')
Sr = pygame.image.load('imgs/S.png')
Pr = pygame.image.load('imgs/P.png')
Er = pygame.image.load('imgs/Er.png')
Cr = pygame.image.load('imgs/C.png')
Ir = pygame.image.load('imgs/I.png')
Ar = pygame.image.load('imgs/Ar.png')
Lr = pygame.image.load('imgs/L.png')
Eg = pygame.image.load('imgs/Eg.png')
Xg = pygame.image.load('imgs/X.png')
Tg = pygame.image.load('imgs/T.png')
Rg = pygame.image.load('imgs/R.png')
Ag = pygame.image.load('imgs/Ag.png')

special_extra_lighted_list = [(Sr, (262,10)), (Pr, (278,10)), (Er, (294,10)), (Cr, (310,10)), (Ir, (326,10)), (Ar, (342,10)), (Lr, (358,10)), 
                              (Eg, (262,28)), (Xg, (294,28)), (Tg, (310,28)), (Rg, (326,28)), (Ag, (342,28))]

lives_4 = pygame.image.load('imgs/4_lives.png')
lives_3 = pygame.image.load('imgs/3_lives.png')
lives_2 = pygame.image.load('imgs/2_lives.png')

x2 = pygame.image.load('imgs/2x.png')
x3 = pygame.image.load('imgs/3x.png')
x5 = pygame.image.load('imgs/5x.png')

controls_lit = pygame.image.load('imgs/controls_click.png')

pregame = pygame.image.load('imgs/pregame.png')

bug_obstacles_y = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
                   [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

bug_obstacles_x = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [0, 1, 0, 0, 0, 1, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 1, 0, 0, 1, 0],
                   [0, 1, 0, 0, 1, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 1, 0, 1, 0],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1]]


sound_intro = pygame.mixer.Sound('audio/intro.mp3')
sound_background = pygame.mixer.Sound('audio/background.mp3')
sound_door = pygame.mixer.Sound('audio/door.mp3')
sound_death = pygame.mixer.Sound('audio/death.mp3')
sound_bug_death = pygame.mixer.Sound('audio/bug_death.mp3')
sound_extra = pygame.mixer.Sound('audio/extra.mp3')
sound_special = pygame.mixer.Sound('audio/special.mp3')
sound_point = pygame.mixer.Sound('audio/point.mp3')
sound_letter = pygame.mixer.Sound('audio/letter.mp3')
sound_bug_out = pygame.mixer.Sound('audio/bug_out.mp3')
sound_level_end = pygame.mixer.Sound('audio/level_end.mp3')
sound_fruit = pygame.mixer.Sound('audio/fruit.mp3')

bug_list = [] 

direction_to_number = [None, 'up', 'right', 'down', 'left']

class bug:
    def __init__(self, bug_type, x, y, direction, speed, animation_phase, toggle):
        self.type = bug_type
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.animation_phase = animation_phase
        self.toggle = toggle
        self.target_chosen = False
        
    def walk(self):
        self.walking = True
        if not self.target_chosen:
            self.available = []
            self.x = nearest(self.x, lxb)
            self.y = nearest(self.y, lyb)
            if bug_obstacles_x[int(int((self.x - 74) / 48))][int(int(self.y - 56) / 34)] == 0:
                self.available.append('left')
            if bug_obstacles_x[int(int((self.x - 74) / 48))+1][int(int(self.y - 56) / 34)] == 0:
                self.available.append('right')
            if bug_obstacles_y[int(int(self.y - 56) / 34)][int(int((self.x - 74) / 48))] == 0:
                self.available.append('up')
            if bug_obstacles_y[int(int(self.y - 56) / 34)+1][int(int((self.x - 74) / 48))] == 0:
                self.available.append('down')
            if len(self.available) == 1:
                if self.available[0] == 'up':
                    self.direction = 1
                    self.target_y = self.y - 34
                elif self.available[0] == 'right':
                    self.direction = 2
                    self.target_x = self.x + 48
                elif self.available[0] == 'down':
                    self.direction = 3
                    self.target_y = self.y + 34
                elif self.available[0] == 'left':
                    self.direction = 4
                    self.target_x = self.x - 48
            elif int(l_x) == int(self.x) and l_y > self.y and 'down' in self.available:
                    self.direction = 3
                    self.target_y = self.y + 34
            elif int(l_x) == int(self.x) and l_y < self.y and 'up' in self.available:
                    self.direction = 1
                    self.target_y = self.y - 34
            elif int(l_y) == int(self.y) and l_x > self.x and 'right' in self.available:
                    self.direction = 2
                    self.target_x = self.x + 48
            elif int(l_y) == int(self.y) and l_x < self.x and 'left' in self.available:
                    self.direction = 4
                    self.target_x = self.x - 48
            elif direction_to_number[self.direction] in self.available:
                if randint(1, 5) > 1:
                    if self.direction == 1:
                        self.target_y = self.y - 34
                    elif self.direction == 2:
                        self.target_x = self.x + 48
                    elif self.direction == 3:
                        self.target_y = self.y + 34
                    elif self.direction == 4:
                        self.target_x = self.x - 48
                else:
                    self.available.pop(self.available.index(direction_to_number[self.direction]))
                    self.direction = direction_to_number.index(self.available[randint(0, len(self.available)-1)])
                    if self.direction == 1:
                        self.target_y = self.y - 34
                    elif self.direction == 2:
                        self.target_x = self.x + 48
                    elif self.direction == 3:
                        self.target_y = self.y + 34
                    elif self.direction == 4:
                        self.target_x = self.x - 48
            else:
                    self.direction = direction_to_number.index(self.available[randint(0, len(self.available)-1)])
                    if self.direction == 1:
                        self.target_y = self.y - 34
                    elif self.direction == 2:
                        self.target_x = self.x + 48
                    elif self.direction == 3:
                        self.target_y = self.y + 34
                    elif self.direction == 4:
                        self.target_x = self.x - 48
            self.target_chosen = True
        if self.toggle:
            if self.direction == 1:
                if self.y > self.target_y:
                    self.y -= self.speed
                else:
                    self.target_chosen = False
            elif self.direction == 3:
                if self.y < self.target_y:
                    self.y += self.speed
                else:
                    self.target_chosen = False
            elif self.direction == 2:
                if self.x < self.target_x:
                    self.x += self.speed
                else:
                    self.target_chosen = False
            elif self.direction == 4:
                if self.x > self.target_x:
                    self.x -= self.speed
                else:
                    self.target_chosen = False
            
            if not near(self.x, lxb):
                self.y = nearest(self.y, lyb)
            if not near(self.y, lyb):
                self.x = nearest(self.x, lxb)
            
    def change_phase(self):
        self.animation_phase = (self.animation_phase + 1) % 4
    
    def return_x_y_image(self):
        self.x_y_image = ((int(self.x), int(self.y)), bugs[self.type][self.direction - 1][self.animation_phase])
        return self.x_y_image
    
    def return_x(self):
        return self.x
    
    def return_y(self):
        return self.y
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
    
    def set_direction(self, direction):
        self.direction = direction
    
    def set_movement(self, binary):
        self.toggle = binary
        
    def is_moving(self):
        return self.toggle
        
def near(x, lx):
    for i in lx:
        if i - 9.5 < x < i + 9.5:
            return True
    return False
def nearest(x, lx):
    dx = list(map(lambda a: abs(a - x), lx))
    return lx[dx.index(min(dx))]

def is_point():
    for i in range(len(object_matrix)):
        for j in object_matrix[i]:
            if 1 <= j <= 12:
                return True
    return False

def show_screen_plus_object(obj, x, y):
    screen.fill(pygame.Color('black'))
    screen.blit(background, (0,0))
    screen.blit(obstacles, (0,0))
    screen.blit(special_extra, (254,10))
    for i in range(len(door_pos)):
        if door_pos[i] == 1:
            screen.blit(door_v, door_v_coords[i])
        else:
            screen.blit(door_h, door_h_coords[i])
    for i in range(len(object_matrix)):
        for j in range(len(object_matrix[i])):
            if object_matrix[i][j] == 1:
                if i % 2 == 0:
                    screen.blit(bar_right, object_coords[i][j])
                else:
                    screen.blit(bar_left, object_coords[i][j])
            elif object_matrix[i][j] == 2:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_S, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_S, object_coords[i][j])
                else:
                    screen.blit(blue_S, object_coords[i][j])
            elif object_matrix[i][j] == 3:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_P, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_P, object_coords[i][j])
                else:
                    screen.blit(blue_P, object_coords[i][j])
            elif object_matrix[i][j] == 4:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_E, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_E, object_coords[i][j])
                else:
                    screen.blit(blue_E, object_coords[i][j])
            elif object_matrix[i][j] == 5:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_C, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_C, object_coords[i][j])
                else:
                    screen.blit(blue_C, object_coords[i][j])
            elif object_matrix[i][j] == 6:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_I, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_I, object_coords[i][j])
                else:
                    screen.blit(blue_I, object_coords[i][j])
            elif object_matrix[i][j] == 7:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_A, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_A, object_coords[i][j])
                else:
                    screen.blit(blue_A, object_coords[i][j])
            elif object_matrix[i][j] == 8:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_L, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_L, object_coords[i][j])
                else:
                    screen.blit(blue_L, object_coords[i][j])
            elif object_matrix[i][j] == 9:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_X, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_X, object_coords[i][j])
                else:
                    screen.blit(blue_X, object_coords[i][j])
            elif object_matrix[i][j] == 10:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_T, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_T, object_coords[i][j])
                else:
                    screen.blit(blue_T, object_coords[i][j])
            elif object_matrix[i][j] == 11:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_R, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_R, object_coords[i][j])
                else:
                    screen.blit(blue_R, object_coords[i][j])
            elif object_matrix[i][j] == 12:
                if 0 <= timer % 10 < 1:
                    screen.blit(red_heart, object_coords[i][j])
                elif 1 <= timer % 10 < 4:
                    screen.blit(green_heart, object_coords[i][j])
                else:
                    screen.blit(blue_heart, object_coords[i][j])
            elif object_matrix[i][j] == 13:
                screen.blit(skull, object_coords[i][j])
                    
    for i in range(border_color_change_state):
        if border_color_change_list[i][0][2] == 1:
            screen.blit(border_h_green, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
            screen.blit(border_h_green, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
        elif border_color_change_list[i][0][2] == 2:
            screen.blit(border_v_green, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
            screen.blit(border_v_green, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
        elif border_color_change_list[i][0][2] == 3:
            screen.blit(border_v_green2, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
            screen.blit(border_v_green2, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
    for i in range(len(special_extra_list)):
        if special_extra_list[i] == 1:
            screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
    if lives == 4:
        screen.blit(lives_4, (58, 370))
    elif lives == 3:
        screen.blit(lives_3, (58, 370))
    elif lives == 2:
        screen.blit(lives_2, (58, 370))
    if multiplier == 2:
        screen.blit(x2, (310,368))
    elif multiplier == 3:
        screen.blit(x3, (310,368))
    elif multiplier == 5:
        screen.blit(x5, (310,368))
    for n in range(len(digit_list)):
        if digit_list[n] == 0:
            screen.blit(d0, digit_coord_list[n])
        elif digit_list[n] == 1:
            screen.blit(d1, digit_coord_list[n])
        elif digit_list[n] == 2:
            screen.blit(d2, digit_coord_list[n])
        elif digit_list[n] == 3:
            screen.blit(d3, digit_coord_list[n])
        elif digit_list[n] == 4:
            screen.blit(d4, digit_coord_list[n])
        elif digit_list[n] == 5:
            screen.blit(d5, digit_coord_list[n])
        elif digit_list[n] == 6:
            screen.blit(d6, digit_coord_list[n])
        elif digit_list[n] == 7:
            screen.blit(d7, digit_coord_list[n])
        elif digit_list[n] == 8:
            screen.blit(d8, digit_coord_list[n])
        elif digit_list[n] == 9:
            screen.blit(d9, digit_coord_list[n])
    screen.blit(obj, (x, y))
    if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
    else:
                    screen.blit(fruit_list[17], (566, 368))
            
    if fruit_out:
                if level < 18:
                    screen.blit(fruit_list[level-1], (314,196))
                else:
                    screen.blit(fruit_list[17], (314,196))
    
    
    bug_coord_list = []
    for b in bug_list:
                    already_exists = False
                    for t in bug_coord_list:
                        if b.return_x() == t[0] and b.return_y() == t[1]:
                            already_exists = True
                    if not already_exists:
                        tup = b.return_x_y_image()
                        screen.blit(tup[1], tup[0])
                        bug_coord_list.append(tup[0])
    pygame.display.flip()
    pygame.event.pump()

veggie_bounty_harvest = pygame.image.load('imgs/vbh.png')

def special_pre_screen(bol):
    screen.fill(pygame.Color('black'))
    screen.blit(pink_background, (0,0))
    screen.blit(special_extra, (254,10))
    for n in range(len(digit_list)):
        if digit_list[n] == 0:
            screen.blit(d0, digit_coord_list[n])
        elif digit_list[n] == 1:
            screen.blit(d1, digit_coord_list[n])
        elif digit_list[n] == 2:
            screen.blit(d2, digit_coord_list[n])
        elif digit_list[n] == 3:
            screen.blit(d3, digit_coord_list[n])
        elif digit_list[n] == 4:
            screen.blit(d4, digit_coord_list[n])
        elif digit_list[n] == 5:
            screen.blit(d5, digit_coord_list[n])
        elif digit_list[n] == 6:
            screen.blit(d6, digit_coord_list[n])
        elif digit_list[n] == 7:
            screen.blit(d7, digit_coord_list[n])
        elif digit_list[n] == 8:
            screen.blit(d8, digit_coord_list[n])
        elif digit_list[n] == 9:
            screen.blit(d9, digit_coord_list[n])   
    if lives == 4:
        screen.blit(lives_4, (58, 370))
    elif lives == 3:
        screen.blit(lives_3, (58, 370))
    elif lives == 2:
        screen.blit(lives_2, (58, 370)) 
    if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
    else:
                    screen.blit(fruit_list[17], (566, 368))
    for i in range(len(special_extra_list)):
        if i > 6:
            if special_extra_list[i] == 1:
                screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
        else:
            if bol:
                screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
    screen.blit(veggie_bounty_harvest, (256, 164))
    pygame.display.flip()
    pygame.event.pump()
    
                    
          
def death():
    sound_death.play()
    x = nearest(int(l_x), lx)
    y = nearest(int(l_y), ly)
    show_screen_plus_object(dead1, x, y)
    pygame.time.wait(1000)
    show_screen_plus_object(dead2, x, y)
    pygame.time.wait(125)
    show_screen_plus_object(dead3, x, y)
    pygame.time.wait(125)
    show_screen_plus_object(dead4, x, y)
    pygame.time.wait(125)
    show_screen_plus_object(dead5, x, y)
    pygame.time.wait(125)
    show_screen_plus_object(angel, x, y)
    pygame.time.wait(500)
    for i in range(16):
        x += 1
        show_screen_plus_object(angel, x, y)
        pygame.time.wait(10)
    for i in range(16):
        x += 1
        y -= 1
        show_screen_plus_object(angel, x, y)
        pygame.time.wait(10)
    for i in range(6):
        y -= 1
        show_screen_plus_object(angel, x, y)
        pygame.time.wait(10)
    for n in range(2):
        for i in range(16):
            x -= 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)
        for i in range(16):
            x -= 1
            y -= 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)
        for i in range(6):
            y -= 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)
    for n in range(2):
        for i in range(16):
            x += 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)
        for i in range(16):
            x += 1
            y -= 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)
        for i in range(6):
            y -= 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)
    for n in range(2):
        for i in range(16):
            x -= 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)
        for i in range(16):
            x -= 1
            y -= 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)
        for i in range(6):
            y -= 1
            show_screen_plus_object(angel, x, y)
            pygame.time.wait(10)

def extra_animation_screen(l_x, l_y, direction, phase):
                screen.fill(pygame.Color('black'))
                screen.blit(extra_background, (0,0))
                screen.blit(special_extra, (254,10))
                screen.blit(ladybug_list[direction][phase], (int(l_x), int(l_y)))
                screen.blit(black, (74, 366))
                screen.blit(pink_background, (0,0))
                for i in range(len(special_extra_list)):
                    if special_extra_list[i] == 1:
                        screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
                if lives == 4:
                    screen.blit(lives_4, (58, 370))
                elif lives == 3:
                    screen.blit(lives_3, (58, 370))
                elif lives == 2:
                    screen.blit(lives_2, (58, 370))
                if multiplier == 2:
                    screen.blit(x2, (310,368))
                elif multiplier == 3:
                    screen.blit(x3, (310,368))
                elif multiplier == 5:
                    screen.blit(x5, (310,368))
                for n in range(len(digit_list)):
                    if digit_list[n] == 0:
                        screen.blit(d0, digit_coord_list[n])
                    elif digit_list[n] == 1:
                        screen.blit(d1, digit_coord_list[n])
                    elif digit_list[n] == 2:
                        screen.blit(d2, digit_coord_list[n])
                    elif digit_list[n] == 3:
                        screen.blit(d3, digit_coord_list[n])
                    elif digit_list[n] == 4:
                        screen.blit(d4, digit_coord_list[n])
                    elif digit_list[n] == 5:
                        screen.blit(d5, digit_coord_list[n])
                    elif digit_list[n] == 6:
                        screen.blit(d6, digit_coord_list[n])
                    elif digit_list[n] == 7:
                        screen.blit(d7, digit_coord_list[n])
                    elif digit_list[n] == 8:
                        screen.blit(d8, digit_coord_list[n])
                    elif digit_list[n] == 9:
                        screen.blit(d9, digit_coord_list[n])
                if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
                else:
                    screen.blit(fruit_list[17], (566, 368))
                pygame.display.flip()
                pygame.event.pump()

back_is_lit = False
back = pygame.image.load('imgs/back.png')
controls_menu = pygame.image.load('imgs/controls.png')
control_is_lit = False
in_levels = True
menu = True
menu_background = pygame.image.load('imgs/menu_background.png')
menu_ladybug = pygame.image.load('imgs/menu_ladybug_1.png')
menu_ladybug_stage = 1
menu_ladybug_dir = 0
while menu: #menu screen
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            in_levels = False
            lives = 0
            menu = False
            gameover = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                running = False
                in_levels = False
                lives = 0
                menu = False
                gameover = False
            elif ev.key == pygame.K_SPACE:
                menu = False
        elif ev.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if 253 < mouse_pos[0] < 410 and 299 < mouse_pos[1] < 312:
                control_is_lit = True
            else:
                control_is_lit = False
        elif ev.type == pygame.MOUSEBUTTONDOWN and control_is_lit:
            control_menu = True
            while control_menu:
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEMOTION:
                        mouse_pos = pygame.mouse.get_pos()
                        if 453 < mouse_pos[0] < 530 and 291 < mouse_pos[1] < 304:
                            back_is_lit = True
                        else:
                            back_is_lit = False
                    elif ev.type == pygame.MOUSEBUTTONDOWN and back_is_lit:
                        control_menu = False
                screen.fill(pygame.Color('black'))
                screen.blit(controls_menu, (0,0))
                if back_is_lit:
                    screen.blit(back, (454, 292))
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.wait(10)
                
    screen.fill(pygame.Color('black'))
    screen.blit(menu_ladybug, (318,194))
    screen.blit(menu_background, (0,0))
    if control_is_lit == True:
        screen.blit(controls_lit, (254, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.wait(15)
    if menu_ladybug_dir == 0:
        if menu_ladybug_stage == 1:
            menu_ladybug_stage = 2
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_2.png')
        elif menu_ladybug_stage == 2:
            menu_ladybug_stage = 3
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_3.png')
        elif menu_ladybug_stage == 3:
            menu_ladybug_stage = 4
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_4.png')
        elif menu_ladybug_stage == 4:
            menu_ladybug_stage = 5
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_5.png')
        elif menu_ladybug_stage == 5:
            menu_ladybug_stage = 6
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_6.png')
        elif menu_ladybug_stage == 6:
            menu_ladybug_stage = 7
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_7.png')
        elif menu_ladybug_stage == 7:
            menu_ladybug_stage = 6
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_6.png')
            menu_ladybug_dir = 1
    elif menu_ladybug_dir == 1:
        if menu_ladybug_stage == 1:
            menu_ladybug_stage = 2
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_2.png')
            menu_ladybug_dir = 0
        elif menu_ladybug_stage == 2:
            menu_ladybug_stage = 1
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_1.png')
        elif menu_ladybug_stage == 3:
            menu_ladybug_stage = 2
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_2.png')
        elif menu_ladybug_stage == 4:
            menu_ladybug_stage = 3
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_3.png')
        elif menu_ladybug_stage == 5:
            menu_ladybug_stage = 4
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_4.png')
        elif menu_ladybug_stage == 6:
            menu_ladybug_stage = 5
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_5.png')
        elif menu_ladybug_stage == 7:
            menu_ladybug_stage = 6
            menu_ladybug = pygame.image.load('imgs/menu_ladybug_6.png')
         



while in_levels == True:  
    border_color_change_state = 0
    frame_number = 0
    timer = 0
    letter_and_hearts_coords = []
    object_matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    while len(letter_and_hearts_coords) < 8:
        randcoord = (randint(0,9), randint(0, 8))
        if object_matrix[randcoord[1]][randcoord[0]] == 1:
            c = 0
            for i in letter_and_hearts_coords:
                if i == randcoord:
                    c = 1
            if c == 0:
                letter_and_hearts_coords.append(randcoord)
    
    
    
    SPCIL = [2, 3, 5, 6, 8]
    SPCIL_chosen = SPCIL[randint(0, 4)]
    EA = [4, 7]
    EA_chosen = EA[randint(0, 1)]
    XTR = [9, 10, 11]
    XTR_chosen = XTR[randint(0, 2)]
    
    object_matrix[letter_and_hearts_coords[0][1]][letter_and_hearts_coords[0][0]] = SPCIL_chosen
    object_matrix[letter_and_hearts_coords[1][1]][letter_and_hearts_coords[1][0]] = EA_chosen
    object_matrix[letter_and_hearts_coords[2][1]][letter_and_hearts_coords[2][0]] = XTR_chosen
    object_matrix[letter_and_hearts_coords[3][1]][letter_and_hearts_coords[3][0]] = 12
    object_matrix[letter_and_hearts_coords[4][1]][letter_and_hearts_coords[4][0]] = 12
    object_matrix[letter_and_hearts_coords[5][1]][letter_and_hearts_coords[5][0]] = 12
    object_matrix[letter_and_hearts_coords[6][1]][letter_and_hearts_coords[6][0]] = 13
    object_matrix[letter_and_hearts_coords[7][1]][letter_and_hearts_coords[7][0]] = 13
    door_pos = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]
    
        
    
    #pre-game screen
    screen.fill(pygame.Color('black'))
    screen.blit(background, (0,0))
    screen.blit(pregame, (0,0))
    screen.blit(special_extra, (254,10))
    if SPCIL_chosen == 2:
        screen.blit(blue_S, (254,244))
    elif SPCIL_chosen == 3:
        screen.blit(blue_P, (254,244))
    elif SPCIL_chosen == 5:
        screen.blit(blue_C, (254,244))
    elif SPCIL_chosen == 6:
        screen.blit(blue_I, (254,244))
    elif SPCIL_chosen == 8:
        screen.blit(blue_L, (254,244))
    if XTR_chosen == 9:
        screen.blit(blue_X, (318,244))
    elif XTR_chosen == 10:
        screen.blit(blue_T, (318,244))
    elif XTR_chosen == 11:
        screen.blit(blue_R, (318,244))
    if EA_chosen == 4:
        screen.blit(blue_E, (382,244))
    elif EA_chosen == 7:
        screen.blit(blue_A, (382,244))
    
    if level == 1:
        screen.blit(lvl_1, (234,82))
    elif level == 2:
        screen.blit(lvl_2, (234,82))
    elif level == 3:
        screen.blit(lvl_3, (234,82))
    elif level == 4:
        screen.blit(lvl_4, (234,82))
    elif level == 5:
        screen.blit(lvl_5, (234,82))
    elif level == 6:
        screen.blit(lvl_6, (234,82))
    elif level == 7:
        screen.blit(lvl_7, (234,82))
    elif level == 8:
        screen.blit(lvl_8, (234,82))
    elif level == 9:
        screen.blit(lvl_9, (234,82))
    elif level == 10:
        screen.blit(lvl_10, (234,82))
    elif level == 11:
        screen.blit(lvl_11, (234,82))
    elif level == 12:
        screen.blit(lvl_12, (234,82))
    elif level == 13:
        screen.blit(lvl_13, (234,82))
    elif level == 14:
        screen.blit(lvl_14, (234,82))
    elif level == 15:
        screen.blit(lvl_15, (234,82))
    elif level == 16:
        screen.blit(lvl_16, (234,82))
    elif level == 17:
        screen.blit(lvl_17, (234,82))
    elif level == 18:
        screen.blit(lvl_18, (234,82))
    else:
        screen.blit(lvl_19, (234,82))
        l = level % 10
        screen.blit(blue_digit_list[l], (402,82))
        screen.blit(blue_digit_list[int(((level - l) % 100) / 10)], (370,82))
    
    
    for i in range(len(special_extra_list)):
                if special_extra_list[i] == 1:
                    screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
    if lives == 4:
                screen.blit(lives_4, (58, 370))
    elif lives == 3:
                screen.blit(lives_3, (58, 370))
    elif lives == 2:
                screen.blit(lives_2, (58, 370))
    for n in range(len(digit_list)):
                if digit_list[n] == 0:
                    screen.blit(d0, digit_coord_list[n])
                elif digit_list[n] == 1:
                    screen.blit(d1, digit_coord_list[n])
                elif digit_list[n] == 2:
                    screen.blit(d2, digit_coord_list[n])
                elif digit_list[n] == 3:
                    screen.blit(d3, digit_coord_list[n])
                elif digit_list[n] == 4:
                    screen.blit(d4, digit_coord_list[n])
                elif digit_list[n] == 5:
                    screen.blit(d5, digit_coord_list[n])
                elif digit_list[n] == 6:
                    screen.blit(d6, digit_coord_list[n])
                elif digit_list[n] == 7:
                    screen.blit(d7, digit_coord_list[n])
                elif digit_list[n] == 8:
                    screen.blit(d8, digit_coord_list[n])
                elif digit_list[n] == 9:
                    screen.blit(d9, digit_coord_list[n])
    if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
    else:
                    screen.blit(fruit_list[17], (566, 368))
                
    pygame.display.flip()    
    pygame.event.pump()
    pygame.time.wait(4000)
    
    current_level = level
    multiplier = 1
    while lives > 0 and level == current_level:
        frame_count = 0
        running = True
        l_x = 314
        l_y = 358
        border_color_change_state = 0
        frame_number = 0
        ladybug_animation_stage = 0
        not_released_bugs = []
        if level < 9:
            for i in range(4):
                bug_ = bug(level - 1, 314, 192, 1, (40+level)/34, 0, False)
                bug_list.append(bug_)
        elif level < 40:
            for i in range(4):
                bug_ = bug(randint(0,7), 314, 192, 1, (40+level)/34, 0, False)
                bug_list.append(bug_)
        else:
            for i in range(4):
                bug_ = bug(randint(0,7), 314, 192, 1, 40, 0, False)
                bug_list.append(bug_)
        for b in bug_list:
            not_released_bugs.append(b)
        sound_intro.play()
        while l_y != 260: # starting animation
            fruit_lock = 0
            counter = 0
            bugs_out = 0
            l_y -= 1  
            screen.fill(pygame.Color('black'))
            screen.blit(ladybug_list[0][ladybug_animation_stage], (int(l_x), int(l_y)))
            screen.blit(starting_animation_block, (0,0))
            screen.blit(background, (0,0))
            screen.blit(obstacles, (0,0))
            screen.blit(special_extra, (254,10))
            for i in range(len(door_pos)):
                if door_pos[i] == 1:
                    screen.blit(door_v, door_v_coords[i])
                else:
                    screen.blit(door_h, door_h_coords[i])
            for i in range(len(object_matrix)):
                for j in range(len(object_matrix[i])):
                    if object_matrix[i][j] == 1:
                        if i % 2 == 0:
                            screen.blit(bar_right, object_coords[i][j])
                        else:
                            screen.blit(bar_left, object_coords[i][j])
                    elif object_matrix[i][j] == 2:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_S, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_S, object_coords[i][j])
                        else:
                            screen.blit(blue_S, object_coords[i][j])
                    elif object_matrix[i][j] == 3:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_P, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_P, object_coords[i][j])
                        else:
                            screen.blit(blue_P, object_coords[i][j])
                    elif object_matrix[i][j] == 4:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_E, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_E, object_coords[i][j])
                        else:
                            screen.blit(blue_E, object_coords[i][j])
                    elif object_matrix[i][j] == 5:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_C, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_C, object_coords[i][j])
                        else:
                            screen.blit(blue_C, object_coords[i][j])
                    elif object_matrix[i][j] == 6:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_I, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_I, object_coords[i][j])
                        else:
                            screen.blit(blue_I, object_coords[i][j])
                    elif object_matrix[i][j] == 7:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_A, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_A, object_coords[i][j])
                        else:
                            screen.blit(blue_A, object_coords[i][j])
                    elif object_matrix[i][j] == 8:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_L, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_L, object_coords[i][j])
                        else:
                            screen.blit(blue_L, object_coords[i][j])
                    elif object_matrix[i][j] == 9:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_X, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_X, object_coords[i][j])
                        else:
                            screen.blit(blue_X, object_coords[i][j])
                    elif object_matrix[i][j] == 10:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_T, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_T, object_coords[i][j])
                        else:
                            screen.blit(blue_T, object_coords[i][j])
                    elif object_matrix[i][j] == 11:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_R, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_R, object_coords[i][j])
                        else:
                            screen.blit(blue_R, object_coords[i][j])
                    elif object_matrix[i][j] == 12:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_heart, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_heart, object_coords[i][j])
                        else:
                            screen.blit(blue_heart, object_coords[i][j])
                    elif object_matrix[i][j] == 13:
                        screen.blit(skull, object_coords[i][j])
            for i in range(len(special_extra_list)):
                if special_extra_list[i] == 1:
                    screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
            
            if lives == 4:
                screen.blit(lives_4, (58, 370))
            elif lives == 3:
                screen.blit(lives_3, (58, 370))
            elif lives == 2:
                screen.blit(lives_2, (58, 370))
        
            if multiplier == 2:
                screen.blit(x2, (310,368))
            elif multiplier == 3:
                screen.blit(x3, (310,368))
            elif multiplier == 5:
                screen.blit(x5, (310,368))
            
            
            for n in range(len(digit_list)):
                if digit_list[n] == 0:
                    screen.blit(d0, digit_coord_list[n])
                elif digit_list[n] == 1:
                    screen.blit(d1, digit_coord_list[n])
                elif digit_list[n] == 2:
                    screen.blit(d2, digit_coord_list[n])
                elif digit_list[n] == 3:
                    screen.blit(d3, digit_coord_list[n])
                elif digit_list[n] == 4:
                    screen.blit(d4, digit_coord_list[n])
                elif digit_list[n] == 5:
                    screen.blit(d5, digit_coord_list[n])
                elif digit_list[n] == 6:
                    screen.blit(d6, digit_coord_list[n])
                elif digit_list[n] == 7:
                    screen.blit(d7, digit_coord_list[n])
                elif digit_list[n] == 8:
                    screen.blit(d8, digit_coord_list[n])
                elif digit_list[n] == 9:
                    screen.blit(d9, digit_coord_list[n])
            if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
            else:
                    screen.blit(fruit_list[17], (566, 368))
            frame_count += 1
            
            bug_coord_list = []
            for b in bug_list:
                    already_exists = False
                    for t in bug_coord_list:
                        if b.return_x() == t[0] and b.return_y() == t[1]:
                            already_exists = True
                    if not already_exists:
                        tup = b.return_x_y_image()
                        screen.blit(tup[1], tup[0])
                        bug_coord_list.append(tup[0])
                    if frame_count % 10 == 0:
                        b.change_phase()
            pygame.display.flip()
            pygame.event.pump()
            ladybug_animation_stage = (ladybug_animation_stage + 2) % 12
            pygame.time.wait(30)
            
        screen.fill(pygame.Color('black'))
        screen.blit(background, (0,0))
        
        while running:  # gameloop
        #1
            t0 = pygame.time.get_ticks()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                    in_levels = False
                    lives = 0
                    gameover = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        running = False
                        in_levels = False
                        lives = 0
                        gameover = False
                    elif ev.key == pygame.K_LEFT:
                        left_key = True
                        right_key = False
                        up_key = False
                        down_key = False
                        latest_key_pressed = 'left'
                    elif ev.key == pygame.K_RIGHT:
                        right_key = True
                        left_key = False
                        up_key = False
                        down_key = False
                        latest_key_pressed = 'right'
                    elif ev.key == pygame.K_UP:
                        up_key = True
                        left_key = False
                        right_key = False
                        down_key = False
                        latest_key_pressed = 'up'
                    elif ev.key == pygame.K_DOWN:
                        down_key = True
                        left_key = False
                        right_key = False
                        up_key = False
                        latest_key_pressed = 'down'
                    elif ev.key == pygame.K_c:
                        if cheats:
                            cheats = False
                        else:
                            cheats = True
                    elif ev.key == pygame.K_k and cheats:
                        if kill:
                            kill = False
                        else:
                            kill = True
                    elif ev.key == pygame.K_n and cheats:
                        running = False
                        pygame.time.wait(2000)
                        level += 1
                        bug_list = []
                    elif ev.key == pygame.K_l and cheats:
                        if lives < 4:
                            lives += 1
                    elif ev.key == pygame.K_e and cheats:
                        special_extra_list[11] = 1
                        special_extra_list[10] = 1
                        special_extra_list[9] = 1
                        special_extra_list[8] = 1
                        special_extra_list[7] = 1
                    elif ev.key == pygame.K_s and cheats:
                        special_extra_list[0] = 1
                        special_extra_list[1] = 1
                        special_extra_list[2] = 1
                        special_extra_list[3] = 1
                        special_extra_list[4] = 1
                        special_extra_list[5] = 1
                        special_extra_list[6] = 1
                    elif ev.key == pygame.K_p:
                            pause = True
                            pygame.event.clear()
                    elif ev.key == pygame.K_t and cheats:
                        if movement_toggle:
                            movement_toggle = False
                            bugs_moving = []
                            for b in bug_list:
                                if b.is_moving():
                                    b.set_movement(False)
                                    bugs_moving.append(b)
                        else:
                            movement_toggle = True
                            for b in bugs_moving:
                                b.set_movement(True)
                            
                elif ev.type == pygame.KEYUP:
                    if ev.key == pygame.K_LEFT:
                        left_key = False
                    elif ev.key == pygame.K_RIGHT:
                        right_key = False
                    elif ev.key == pygame.K_UP:
                        up_key = False
                    elif ev.key == pygame.K_DOWN:
                        down_key = False
        
        
        #2
            while pause:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        running = False
                        in_levels = False
                        lives = 0
                        gameover = False
                        pause = False
                    elif ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_ESCAPE:
                            running = False
                            in_levels = False
                            lives = 0
                            gameover = False
                            pause = False
                        elif ev.key == pygame.K_p:
                            pause = False
                pygame.time.wait(10)
            
            col = int((nearest(l_x, lx)-74)/48) #determining what the closest column and row ladybug is at to use in the obstacle part
            row = int((nearest(l_y, ly)-56)/34)
        
        
            n = 10
            for m in range(n):
                if left_key and l_x > 74: #ladybug movement and blocking by obstacles
                    if int(l_x) in lx:
                        if nearest(l_y, ly) in my[col]:
                            l_x -= ladybug_speed/n
                    else:
                        l_x -= ladybug_speed/n
                elif right_key and l_x < 554:
                    if int(l_x) in lx:
                        if nearest(l_y, ly) in my[col+1]:
                            l_x += ladybug_speed/n
                    else:
                        l_x += ladybug_speed/n
                elif up_key and l_y > 56:
                    if int(l_y) in ly:
                        if nearest(l_x, lx) in mx[row]:
                            l_y -= ladybug_speed/n
                    else:
                        l_y -= ladybug_speed/n
                elif down_key and l_y < 328:
                    if int(l_y) in ly:
                        if nearest(l_x, lx) in mx[row+1]:
                            l_y += ladybug_speed/n
                    else:
                        l_y += ladybug_speed/n
                  
                if not near(l_x, lx): #putting ladybug exactly in a column/row if not in an intersection
                    l_y = nearest(l_y, ly)
                if not near(l_y, ly):
                    l_x = nearest(l_x, lx)
                  
                door_pos_save = door_pos.copy()
                    
                for i in range(len(door_pos)): #door opening/closing
                    if door_pos[i] == 0:
                        if door_h_coords[i][0] - 1 < l_x < door_h_coords[i][0] + 49 and door_h_coords[i][1] - 29 < l_y < door_h_coords[i][1] + 1:
                            door_pos[i] = 1
                            if i <= 3:
                                door_pos[i+10] = 1
                            elif 4 <= i <= 6:
                                door_pos[i+3] = 1
                            elif 7 <= i <= 9:
                                door_pos[i-3] = 1
                            elif 10 <= i:
                                door_pos[i-10] = 1
                    elif door_pos[i] == 1:
                        if door_h_coords[i][0] + 1 < l_x < door_h_coords[i][0] + 48 and door_h_coords[i][1] - 31 < l_y < door_h_coords[i][1] + 5:
                            door_pos[i] = 0
                            if i <= 3:
                                door_pos[i+10] = 0
                            elif 4 <= i <= 6:
                                door_pos[i+3] = 0
                            elif 7 <= i <= 9:
                                door_pos[i-3] = 0
                            elif 10 <= i:
                                door_pos[i-10] = 0
                if door_pos != door_pos_save:     
                                sound_door.play() 
            for i in range(len(object_matrix)):
                for j in range(len(object_matrix[i])):
                        update_multiplier = False
                        if object_coords[i][j][0] - 8 < l_x < object_coords[i][j][0] + 8 and object_coords[i][j][1] - 8 < l_y < object_coords[i][j][1] + 8:
                            catch = object_matrix[i][j]
                            object_matrix[i][j] = 0
                            if catch == 1:
                                score += 10*multiplier
                                sound_point.play()
                            elif catch == 2:
                                if 0 <= timer % 10 < 1:
                                    special_extra_list[0] = 1
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 3:
                                if 0 <= timer % 10 < 1:
                                    special_extra_list[1] = 1
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 4:
                                if 0 <= timer % 10 < 1:
                                    special_extra_list[2] = 1
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    special_extra_list[7] = 1
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 5:
                                if 0 <= timer % 10 < 1:
                                    special_extra_list[3] = 1
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 6:
                                if 0 <= timer % 10 < 1:
                                    special_extra_list[4] = 1
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 7:
                                if 0 <= timer % 10 < 1:
                                    special_extra_list[5] = 1
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    special_extra_list[11] = 1
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 8:
                                if 0 <= timer % 10 < 1:
                                    special_extra_list[6] = 1
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 9:
                                if 0 <= timer % 10 < 1:
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    special_extra_list[8] = 1
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 10:
                                if 0 <= timer % 10 < 1:
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    special_extra_list[9] = 1
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 11:
                                if 0 <= timer % 10 < 1:
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    special_extra_list[10] = 1
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                            elif catch == 12:
                                if 0 <= timer % 10 < 1:
                                    score += 800*multiplier
                                elif 1 <= timer % 10 < 4:
                                    score += 300*multiplier
                                else:
                                    score += 100*multiplier
                                    update_multiplier = True
                            elif catch == 13:
                                death()
                                fruit_lock = 0
                                fruit_out = False
                                counter = 0
                                bugs_out = 0
                                lives -= 1
                                running = False
                                bug_list = []
                            if 13 > catch > 1:
                                sound_letter.play()
                                screen.fill(pygame.Color('black'))
                                screen.blit(background, (0,0))
                                screen.blit(obstacles, (0,0))
                                screen.blit(special_extra, (254,10))
                                for n in range(len(door_pos)):
                                    if door_pos[n] == 1:
                                        screen.blit(door_v, door_v_coords[n])
                                    else:
                                        screen.blit(door_h, door_h_coords[n])
                                for n in range(len(object_matrix)):
                                    for m in range(len(object_matrix[n])):
                                        if object_matrix[n][m] == 1:
                                            if n % 2 == 0:
                                                screen.blit(bar_right, object_coords[n][m])
                                            else:
                                                screen.blit(bar_left, object_coords[n][m])
                                        elif object_matrix[n][m] == 2:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_S, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_S, object_coords[n][m])
                                            else:
                                                screen.blit(blue_S, object_coords[n][m])
                                        elif object_matrix[n][m] == 3:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_P, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_P, object_coords[n][m])
                                            else:
                                                screen.blit(blue_P, object_coords[n][m])
                                        elif object_matrix[n][m] == 4:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_E, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_E, object_coords[n][m])
                                            else:
                                                screen.blit(blue_E, object_coords[n][m])
                                        elif object_matrix[n][m] == 5:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_C, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_C, object_coords[n][m])
                                            else:
                                                screen.blit(blue_C, object_coords[n][m])
                                        elif object_matrix[n][m] == 6:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_I, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_I, object_coords[n][m])
                                            else:
                                                screen.blit(blue_I, object_coords[n][m])
                                        elif object_matrix[n][m] == 7:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_A, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_A, object_coords[n][m])
                                            else:
                                                screen.blit(blue_A, object_coords[n][m])
                                        elif object_matrix[n][m] == 8:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_L, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_L, object_coords[n][m])
                                            else:
                                                screen.blit(blue_L, object_coords[n][m])
                                        elif object_matrix[n][m] == 9:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_X, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_X, object_coords[n][m])
                                            else:
                                                screen.blit(blue_X, object_coords[n][m])
                                        elif object_matrix[n][m] == 10:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_T, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_T, object_coords[n][m])
                                            else:
                                                screen.blit(blue_T, object_coords[n][m])
                                        elif object_matrix[n][m] == 11:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_R, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_R, object_coords[n][m])
                                            else:
                                                screen.blit(blue_R, object_coords[n][m])
                                        elif object_matrix[n][m] == 12:
                                            if 0 <= timer % 10 < 1:
                                                screen.blit(red_heart, object_coords[n][m])
                                            elif 1 <= timer % 10 < 4:
                                                screen.blit(green_heart, object_coords[n][m])
                                            else:
                                                screen.blit(blue_heart, object_coords[n][m])
                                        elif object_matrix[n][m] == 13:
                                            screen.blit(skull, object_coords[n][m])
                                                
                                for n in range(border_color_change_state):
                                    if border_color_change_list[n][0][2] == 1:
                                        screen.blit(border_h_green, (border_color_change_list[n][0][0], border_color_change_list[n][0][1]))
                                        screen.blit(border_h_green, (border_color_change_list[n][1][0], border_color_change_list[n][1][1]))
                                    elif border_color_change_list[n][0][2] == 2:
                                        screen.blit(border_v_green, (border_color_change_list[n][0][0], border_color_change_list[n][0][1]))
                                        screen.blit(border_v_green, (border_color_change_list[n][1][0], border_color_change_list[n][1][1]))
                                    elif border_color_change_list[n][0][2] == 3:
                                        screen.blit(border_v_green2, (border_color_change_list[n][0][0], border_color_change_list[n][0][1]))
                                        screen.blit(border_v_green2, (border_color_change_list[n][1][0], border_color_change_list[n][1][1]))
                                for n in range(len(special_extra_list)):
                                    if special_extra_list[n] == 1:
                                        screen.blit(special_extra_lighted_list[n][0], special_extra_lighted_list[n][1])
                                if lives == 4:
                                    screen.blit(lives_4, (58, 370))
                                elif lives == 3:
                                    screen.blit(lives_3, (58, 370))
                                elif lives == 2:
                                    screen.blit(lives_2, (58, 370))
                                if 0 <= timer % 10 < 1:
                                    if multiplier == 1:
                                        screen.blit(p800x1, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 2:
                                        screen.blit(p800x2, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 3:
                                        screen.blit(p800x3, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 5:
                                        screen.blit(p800x5, (object_coords[i][j][0], object_coords[i][j][1]))
                                elif 1 <= timer % 10 < 4:
                                    if multiplier == 1:
                                        screen.blit(p300x1, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 2:
                                        screen.blit(p300x2, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 3:
                                        screen.blit(p300x3, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 5:
                                        screen.blit(p300x5, (object_coords[i][j][0], object_coords[i][j][1]))
                                else:
                                    if multiplier == 1:
                                        screen.blit(p100x1, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 2:
                                        screen.blit(p100x2, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 3:
                                        screen.blit(p100x3, (object_coords[i][j][0], object_coords[i][j][1]))
                                    elif multiplier == 5:
                                        screen.blit(p100x5, (object_coords[i][j][0], object_coords[i][j][1]))
                                if update_multiplier:
                                    if multiplier == 1:
                                        multiplier = 2
                                    elif multiplier == 2:
                                        multiplier = 3
                                    elif multiplier == 3:
                                        multiplier = 5
                                if multiplier == 2:
                                    screen.blit(x2, (310,368))
                                elif multiplier == 3:
                                    screen.blit(x3, (310,368))
                                elif multiplier == 5:
                                    screen.blit(x5, (310,368))
                                score_string = str(score)[::-1]
                                for n in range(len(score_string)):
                                    digit_list[n] = int(score_string[n])
                                if score / 10 < 1:
                                    digit_list[1] = -1
                                elif score / 100 < 1:
                                    digit_list[2] = -1
                                elif score / 1000 < 1:
                                    digit_list[3] = -1
                                elif score / 10000 < 1:
                                    digit_list[4] = -1
                                elif score / 100000 < 1:
                                    digit_list[5] = -1
                                elif score / 1000000 < 1:
                                    digit_list[6] = -1
                                elif score / 10000000 < 1:
                                    digit_list[7] = -1
                                for n in range(len(digit_list)):
                                        if digit_list[n] == 0:
                                            screen.blit(d0, digit_coord_list[n])
                                        elif digit_list[n] == 1:
                                            screen.blit(d1, digit_coord_list[n])
                                        elif digit_list[n] == 2:
                                            screen.blit(d2, digit_coord_list[n])
                                        elif digit_list[n] == 3:
                                            screen.blit(d3, digit_coord_list[n])
                                        elif digit_list[n] == 4:
                                            screen.blit(d4, digit_coord_list[n])
                                        elif digit_list[n] == 5:
                                            screen.blit(d5, digit_coord_list[n])
                                        elif digit_list[n] == 6:
                                            screen.blit(d6, digit_coord_list[n])
                                        elif digit_list[n] == 7:
                                            screen.blit(d7, digit_coord_list[n])
                                        elif digit_list[n] == 8:
                                            screen.blit(d8, digit_coord_list[n])
                                        elif digit_list[n] == 9:
                                            screen.blit(d9, digit_coord_list[n])
                                if level < 18:
                                    screen.blit(fruit_list[level-1], (566, 368))
                                else:
                                    screen.blit(fruit_list[17], (566, 368))    
                                if fruit_out:
                                    if level < 18:
                                        screen.blit(fruit_list[level-1], (314,196))
                                    else:
                                        screen.blit(fruit_list[17], (314,196))
                                
                                
                                bug_coord_list = []
                                for b in bug_list:
                                    already_exists = False
                                    for t in bug_coord_list:
                                        if b.return_x() == t[0] and b.return_y() == t[1]:
                                            already_exists = True
                                    if not already_exists:
                                        tup = b.return_x_y_image()
                                        screen.blit(tup[1], tup[0])
                                        bug_coord_list.append(tup[0])
                                pygame.display.flip()
                                pygame.time.wait(500)
            
            lady_bug_alive = True
            for b in bug_list:
                for i in range(len(object_matrix)):
                    for j in range(len(object_matrix[i])):
                        if object_coords[i][j][0] - 3 < b.return_x() < object_coords[i][j][0] + 3 and object_coords[i][j][1] - 3 < b.return_y() < object_coords[i][j][1] + 3 and object_matrix[i][j] == 13:
                            b.set_movement(False)
                            sound_bug_death.play()
                            b.set_coords(314, 192)
                            b.set_direction(1)
                            not_released_bugs.append(b)
                            object_matrix[i][j] = 0
                if lady_bug_alive and kill and b.is_moving() and b.return_x() - 20 < l_x < b.return_x() + 20 and b.return_y() - 20 < l_y < b.return_y() + 20:
                                death()
                                fruit_lock = 0
                                fruit_out = False
                                counter = 0
                                bugs_out = 0
                                lives -= 1
                                running = False
                                bug_list = []
                                lady_bug_alive = False
            
            if is_point() == False:
                sound_level_end.play()
                running = False
                bug_list = []
                pygame.time.wait(2000)
                level += 1
            
            frame_number = (frame_number + 1) % 100
            if frame_number == 0:
                timer += 1
            if border_color_change_state == 0:
                
                border_color_becoming_green = True
                counter += 1
                if counter == 1:
                    if len(not_released_bugs) > 0 and bugs_out > 0:
                        not_released_bugs[0].set_movement(True)
                        not_released_bugs.pop(0)
                        sound_bug_out.play()
                    bugs_out += 1
                    counter += 1
            if border_color_change_state > 0:
                counter = 0
            if border_color_change_state == len(border_color_change_list):
                border_color_becoming_green = False
            if frame_number % round(42/(2.5+0.7*level)) == 0 and movement_toggle:
                    if border_color_becoming_green:
                        border_color_change_state += 1
                    else:
                        border_color_change_state -= 1
            if frame_number % 2 == 0 or frame_number % 3 == 0:
                if ladybug_animation_stage == 11:
                    ladybug_animation_stage = 0
                else:
                    ladybug_animation_stage += 1
            
            if len(not_released_bugs) > 0:
                fruit_out = False
            
            if bugs_out > 4:
                if fruit_lock == 0 and len(not_released_bugs) == 0:
                    fruit_out = True
                if 192 < l_y < 197 and 313 < l_x < 315 and fruit_out:
                    sound_fruit.play()
                    fruit_out = False
                    if level < 18:
                        score += 500 + 500*level
                    else:
                        score += 9500
                    movement_toggle = False
                    for b in bug_list:
                        b.set_movement(False)
                    counting = True
                    fruit_lock = 1
                    
            if frame_number == 0 and counting:
                five_second_counter += 1
            
            if frame_number % 10 == 0:
                sound_background.play()
            
            if five_second_counter == 5:
                five_second_counter = 0
                for b in bug_list:
                    b.set_movement(True)
                movement_toggle = True
                counting = False
                    
            if door_pos[0] == 0:
                bug_obstacles_x[2][0] = 0
                bug_obstacles_x[2][1] = 0
                bug_obstacles_y[1][1] = 1
                bug_obstacles_y[1][2] = 1
            else:
                bug_obstacles_x[2][0] = 1
                bug_obstacles_x[2][1] = 1
                bug_obstacles_y[1][1] = 0
                bug_obstacles_y[1][2] = 0
            if door_pos[1] == 0:
                bug_obstacles_x[1][2] = 0
                bug_obstacles_x[1][3] = 0
                bug_obstacles_y[3][1] = 1
                bug_obstacles_y[3][0] = 1
            else:
                bug_obstacles_x[1][2] = 1
                bug_obstacles_x[1][3] = 1
                bug_obstacles_y[3][1] = 0
                bug_obstacles_y[3][0] = 0
            if door_pos[2] == 0:
                bug_obstacles_x[2][4] = 0
                bug_obstacles_x[2][5] = 0
                bug_obstacles_y[5][1] = 1
                bug_obstacles_y[5][2] = 1
            else:
                bug_obstacles_x[2][4] = 1
                bug_obstacles_x[2][5] = 1
                bug_obstacles_y[5][1] = 0
                bug_obstacles_y[5][2] = 0
            if door_pos[3] == 0:
                bug_obstacles_x[2][7] = 0
                bug_obstacles_x[2][8] = 0
                bug_obstacles_y[8][1] = 1
                bug_obstacles_y[8][2] = 1
            else:
                bug_obstacles_x[2][7] = 1
                bug_obstacles_x[2][8] = 1
                bug_obstacles_y[8][1] = 0
                bug_obstacles_y[8][2] = 0
            if door_pos[4] == 0:
                bug_obstacles_x[4][1] = 0
                bug_obstacles_x[4][2] = 0
                bug_obstacles_y[2][3] = 1
                bug_obstacles_y[2][4] = 1
            else:
                bug_obstacles_x[4][1] = 1
                bug_obstacles_x[4][2] = 1
                bug_obstacles_y[2][3] = 0
                bug_obstacles_y[2][4] = 0
            if door_pos[5] == 0:
                bug_obstacles_x[4][4] = 0
                bug_obstacles_x[4][5] = 0
                bug_obstacles_y[5][3] = 1
                bug_obstacles_y[5][4] = 1
            else:
                bug_obstacles_x[4][4] = 1
                bug_obstacles_x[4][5] = 1
                bug_obstacles_y[5][3] = 0
                bug_obstacles_y[5][4] = 0
            if door_pos[6] == 0:
                bug_obstacles_x[4][6] = 0
                bug_obstacles_x[4][7] = 0
                bug_obstacles_y[7][3] = 1
                bug_obstacles_y[7][4] = 1
            else:
                bug_obstacles_x[4][6] = 1
                bug_obstacles_x[4][7] = 1
                bug_obstacles_y[7][3] = 0
                bug_obstacles_y[7][4] = 0
        
            if door_pos[7] == 0:
                bug_obstacles_x[7][1] = 0
                bug_obstacles_x[7][2] = 0
                bug_obstacles_y[2][6] = 1
                bug_obstacles_y[2][7] = 1
            else:
                bug_obstacles_x[7][1] = 1
                bug_obstacles_x[7][2] = 1
                bug_obstacles_y[2][6] = 0
                bug_obstacles_y[2][7] = 0
            if door_pos[8] == 0:
                bug_obstacles_x[7][4] = 0
                bug_obstacles_x[7][5] = 0
                bug_obstacles_y[5][6] = 1
                bug_obstacles_y[5][7] = 1
            else:
                bug_obstacles_x[7][4] = 1
                bug_obstacles_x[7][5] = 1
                bug_obstacles_y[5][6] = 0
                bug_obstacles_y[5][7] = 0
            if door_pos[9] == 0:
                bug_obstacles_x[7][6] = 0
                bug_obstacles_x[7][7] = 0
                bug_obstacles_y[7][6] = 1
                bug_obstacles_y[7][7] = 1
            else:
                bug_obstacles_x[7][6] = 1
                bug_obstacles_x[7][7] = 1
                bug_obstacles_y[7][6] = 0
                bug_obstacles_y[7][7] = 0
            if door_pos[10] == 0:
                bug_obstacles_x[9][0] = 0
                bug_obstacles_x[9][1] = 0
                bug_obstacles_y[1][8] = 1
                bug_obstacles_y[1][9] = 1
            else:
                bug_obstacles_x[9][0] = 1
                bug_obstacles_x[9][1] = 1
                bug_obstacles_y[1][8] = 0
                bug_obstacles_y[1][9] = 0
            if door_pos[11] == 0:
                bug_obstacles_x[10][2] = 0
                bug_obstacles_x[10][3] = 0
                bug_obstacles_y[3][9] = 1
                bug_obstacles_y[3][10] = 1
            else:
                bug_obstacles_x[10][2] = 1
                bug_obstacles_x[10][3] = 1
                bug_obstacles_y[3][9] = 0
                bug_obstacles_y[3][10] = 0
            if door_pos[12] == 0:
                bug_obstacles_x[9][4] = 0
                bug_obstacles_x[9][5] = 0
                bug_obstacles_y[5][8] = 1
                bug_obstacles_y[5][9] = 1
            else:
                bug_obstacles_x[9][4] = 1
                bug_obstacles_x[9][5] = 1
                bug_obstacles_y[5][8] = 0
                bug_obstacles_y[5][9] = 0
            if door_pos[13] == 0:
                bug_obstacles_x[9][7] = 0
                bug_obstacles_x[9][8] = 0
                bug_obstacles_y[8][8] = 1
                bug_obstacles_y[8][9] = 1
            else:
                bug_obstacles_x[9][7] = 1
                bug_obstacles_x[9][8] = 1
                bug_obstacles_y[8][8] = 0
                bug_obstacles_y[8][9] = 0
        
            if special_extra_list[0] == 1 and special_extra_list[1] == 1 and special_extra_list[2] == 1 and special_extra_list[3] == 1 and special_extra_list[4] == 1 and special_extra_list[5] == 1 and special_extra_list[6] == 1:
                running = False
                bug_list = []
                screen.fill(pygame.Color('black'))
                screen.blit(pink_background, (0,0))
                screen.blit(pink_obstacles, (0,0))
                screen.blit(special_extra, (254,10))
                extra_blinking = 0
                for i in range(len(door_pos)):
                    if door_pos[i] == 1:
                        screen.blit(door_v, door_v_coords[i])
                    else:
                        screen.blit(door_h, door_h_coords[i])
                for i in range(len(object_matrix)):
                    for j in range(len(object_matrix[i])):
                        if object_matrix[i][j] == 1:
                            if i % 2 == 0:
                                screen.blit(bar_right, object_coords[i][j])
                            else:
                                screen.blit(bar_left, object_coords[i][j])
                        elif object_matrix[i][j] == 2:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_S, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_S, object_coords[i][j])
                            else:
                                screen.blit(blue_S, object_coords[i][j])
                        elif object_matrix[i][j] == 3:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_P, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_P, object_coords[i][j])
                            else:
                                screen.blit(blue_P, object_coords[i][j])
                        elif object_matrix[i][j] == 4:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_E, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_E, object_coords[i][j])
                            else:
                                screen.blit(blue_E, object_coords[i][j])
                        elif object_matrix[i][j] == 5:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_C, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_C, object_coords[i][j])
                            else:
                                screen.blit(blue_C, object_coords[i][j])
                        elif object_matrix[i][j] == 6:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_I, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_I, object_coords[i][j])
                            else:
                                screen.blit(blue_I, object_coords[i][j])
                        elif object_matrix[i][j] == 7:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_A, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_A, object_coords[i][j])
                            else:
                                screen.blit(blue_A, object_coords[i][j])
                        elif object_matrix[i][j] == 8:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_L, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_L, object_coords[i][j])
                            else:
                                screen.blit(blue_L, object_coords[i][j])
                        elif object_matrix[i][j] == 9:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_X, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_X, object_coords[i][j])
                            else:
                                screen.blit(blue_X, object_coords[i][j])
                        elif object_matrix[i][j] == 10:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_T, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_T, object_coords[i][j])
                            else:
                                screen.blit(blue_T, object_coords[i][j])
                        elif object_matrix[i][j] == 11:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_R, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_R, object_coords[i][j])
                            else:
                                screen.blit(blue_R, object_coords[i][j])
                        elif object_matrix[i][j] == 12:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_heart, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_heart, object_coords[i][j])
                            else:
                                screen.blit(blue_heart, object_coords[i][j])
                        elif object_matrix[i][j] == 13:
                            screen.blit(skull, object_coords[i][j])
                         
                if latest_key_pressed == 'up':      
                    screen.blit(ladybug_list[0][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'down':      
                    screen.blit(ladybug_list[1][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'left':      
                    screen.blit(ladybug_list[2][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'right':      
                    screen.blit(ladybug_list[3][ladybug_animation_stage], (int(l_x), int(l_y)))
                
                
                for i in range(len(special_extra_list)):
                    if special_extra_list[i] == 1:
                        screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
                if lives == 4:
                    screen.blit(lives_4, (58, 370))
                elif lives == 3:
                    screen.blit(lives_3, (58, 370))
                elif lives == 2:
                    screen.blit(lives_2, (58, 370))
                if multiplier == 2:
                    screen.blit(x2, (310,368))
                elif multiplier == 3:
                    screen.blit(x3, (310,368))
                elif multiplier == 5:
                    screen.blit(x5, (310,368))
                for n in range(len(digit_list)):
                    if digit_list[n] == 0:
                        screen.blit(d0, digit_coord_list[n])
                    elif digit_list[n] == 1:
                        screen.blit(d1, digit_coord_list[n])
                    elif digit_list[n] == 2:
                        screen.blit(d2, digit_coord_list[n])
                    elif digit_list[n] == 3:
                        screen.blit(d3, digit_coord_list[n])
                    elif digit_list[n] == 4:
                        screen.blit(d4, digit_coord_list[n])
                    elif digit_list[n] == 5:
                        screen.blit(d5, digit_coord_list[n])
                    elif digit_list[n] == 6:
                        screen.blit(d6, digit_coord_list[n])
                    elif digit_list[n] == 7:
                        screen.blit(d7, digit_coord_list[n])
                    elif digit_list[n] == 8:
                        screen.blit(d8, digit_coord_list[n])
                    elif digit_list[n] == 9:
                        screen.blit(d9, digit_coord_list[n])
                if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
                else:
                    screen.blit(fruit_list[17], (566, 368))
                    
                if fruit_out:
                    if level < 18:
                        screen.blit(fruit_list[level-1], (314,196))
                    else:
                        screen.blit(fruit_list[17], (314,196))
                bug_coord_list = []
                for b in bug_list:
                    already_exists = False
                    for t in bug_coord_list:
                        if b.return_x() == t[0] and b.return_y() == t[1]:
                            already_exists = True
                    if not already_exists:
                        tup = b.return_x_y_image()
                        screen.blit(tup[1], tup[0])
                        bug_coord_list.append(tup[0])
                pygame.display.flip()
                pygame.event.pump()
                
                sound_special.play()
                pygame.time.wait(1000)
                special_pre_screen(False)
                pygame.time.wait(500)
                special_pre_screen(True)
                pygame.time.wait(500)
                special_pre_screen(False)
                pygame.time.wait(500)
                special_pre_screen(True)
                pygame.time.wait(500)
                special_pre_screen(False)
                pygame.time.wait(500)
                special_pre_screen(True)
                pygame.time.wait(500)
                special_pre_screen(False)
                pygame.time.wait(500)
                special_pre_screen(True)
                pygame.time.wait(500)
                special_pre_screen(False)
                pygame.time.wait(500)
                special_pre_screen(True)
                pygame.time.wait(500)
                special_pre_screen(False)
                pygame.time.wait(500)
                special_pre_screen(True)
                pygame.time.wait(500)
                
                
                l_x = 314
                l_y = 260
                special = True
                frame_number = 0
                end_lock = False
                border_color_change_state = 0
                ladybug_animation_stage = 0
                left_key = False
                right_key = False
                up_key = False
                down_key = False
                latest_key_pressed = 'up'
                fruit_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                for i in range(6):
                    new_fruit = (randint(0, 8), randint(0, 9))
                    while fruit_matrix[new_fruit[0]][new_fruit[1]] != 0:
                        new_fruit = (randint(0, 8), randint(0, 9))
                    fruit_matrix[new_fruit[0]][new_fruit[1]] = randint(1, 18)
                special_blinking = 0
                while special:
                    t0 = pygame.time.get_ticks()
                    for ev in pygame.event.get():
                            if ev.type == pygame.QUIT:
                                running = False
                                in_levels = False
                                lives = 0
                                gameover = False
                                special = False
                            elif ev.type == pygame.KEYDOWN:
                                if ev.key == pygame.K_ESCAPE:
                                    running = False
                                    in_levels = False
                                    lives = 0
                                    gameover = False
                                    special = False
                                elif ev.key == pygame.K_LEFT:
                                    left_key = True
                                    right_key = False
                                    up_key = False
                                    down_key = False
                                    latest_key_pressed = 'left'
                                elif ev.key == pygame.K_RIGHT:
                                    right_key = True
                                    left_key = False
                                    up_key = False
                                    down_key = False
                                    latest_key_pressed = 'right'
                                elif ev.key == pygame.K_UP:
                                    up_key = True
                                    left_key = False
                                    right_key = False
                                    down_key = False
                                    latest_key_pressed = 'up'
                                elif ev.key == pygame.K_DOWN:
                                    down_key = True
                                    left_key = False
                                    right_key = False
                                    up_key = False
                                    latest_key_pressed = 'down'
                            elif ev.type == pygame.KEYUP:
                                if ev.key == pygame.K_LEFT:
                                    left_key = False
                                elif ev.key == pygame.K_RIGHT:
                                    right_key = False
                                elif ev.key == pygame.K_UP:
                                    up_key = False
                                elif ev.key == pygame.K_DOWN:
                                    down_key = False
                    col = int((nearest(l_x, lx)-74)/48) #determining what the closest column and row ladybug is at to use in the obstacle part
                    row = int((nearest(l_y, ly)-56)/34)
                    
                    
                    n = 10
                    ladybug_speed = 1.3
                    for m in range(n):
                            if left_key and l_x > 74: #ladybug movement and blocking by obstacles
                                if int(l_x) in lx:
                                    if nearest(l_y, ly) in my[col]:
                                        l_x -= ladybug_speed/n
                                else:
                                    l_x -= ladybug_speed/n
                            elif right_key and l_x < 554:
                                if int(l_x) in lx:
                                    if nearest(l_y, ly) in my[col+1]:
                                        l_x += ladybug_speed/n
                                else:
                                    l_x += ladybug_speed/n
                            elif up_key and l_y > 56:
                                if int(l_y) in ly:
                                    if nearest(l_x, lx) in mx[row]:
                                        l_y -= ladybug_speed/n
                                else:
                                    l_y -= ladybug_speed/n
                            elif down_key and l_y < 328:
                                if int(l_y) in ly:
                                    if nearest(l_x, lx) in mx[row+1]:
                                        l_y += ladybug_speed/n
                                else:
                                    l_y += ladybug_speed/n
                              
                            if not near(l_x, lx): #putting ladybug exactly in a column/row if not in an intersection
                                l_y = nearest(l_y, ly)
                            if not near(l_y, ly):
                                l_x = nearest(l_x, lx)
                                
                    frame_number = (frame_number + 1) % 100
                    if border_color_change_state == 0:
                            border_color_becoming_green = True
                            if end_lock:
                                special = False
                    if border_color_change_state == len(border_color_change_list):
                            border_color_becoming_green = False
                            end_lock = True
                    if frame_number % 17 == 0 and movement_toggle:
                                if border_color_becoming_green:
                                    border_color_change_state += 1
                                else:
                                    border_color_change_state -= 1
                    if frame_number % 2 == 0 or frame_number % 3 == 0:
                            if ladybug_animation_stage == 11:
                                ladybug_animation_stage = 0
                            else:
                                ladybug_animation_stage += 1
                    if frame_number % 50 == 0:
                        if special_blinking:
                            special_blinking = False
                        else:
                            special_blinking = True
                    for i in range(len(fruit_matrix)):
                            for j in range(len(fruit_matrix[i])):
                                    if object_coords[i][j][0] - 8 < l_x < object_coords[i][j][0] + 8 and object_coords[i][j][1] - 8 < l_y < object_coords[i][j][1] + 8 and fruit_matrix[i][j] > 0:
                                        score += 500 + 500*fruit_matrix[i][j]
                                        fruit_matrix[i][j] = 0        
                                        new_fruit = (randint(0, 8), randint(0, 9))
                                        while fruit_matrix[new_fruit[0]][new_fruit[1]] != 0:
                                            new_fruit = (randint(0, 8), randint(0, 9))
                                        fruit_matrix[new_fruit[0]][new_fruit[1]] = randint(1, 18)
            
                    screen.fill(pygame.Color('black'))          
                    screen.blit(pink_background, (0,0))
                    screen.blit(pink_obstacles, (0,0))
                    if latest_key_pressed == 'up':      
                                screen.blit(ladybug_list[0][ladybug_animation_stage], (int(l_x), int(l_y)))
                    elif latest_key_pressed == 'down':      
                                screen.blit(ladybug_list[1][ladybug_animation_stage], (int(l_x), int(l_y)))
                    elif latest_key_pressed == 'left':      
                                screen.blit(ladybug_list[2][ladybug_animation_stage], (int(l_x), int(l_y)))
                    elif latest_key_pressed == 'right':      
                                screen.blit(ladybug_list[3][ladybug_animation_stage], (int(l_x), int(l_y)))
                    if lives == 4:
                                screen.blit(lives_4, (58, 370))
                    elif lives == 3:
                                screen.blit(lives_3, (58, 370))
                    elif lives == 2:
                                screen.blit(lives_2, (58, 370))
                    
                    score_string = str(score)[::-1]
                    for n in range(len(score_string)):
                                                digit_list[n] = int(score_string[n])
                    if score / 10 < 1:
                                                digit_list[1] = -1
                    elif score / 100 < 1:
                                                digit_list[2] = -1
                    elif score / 1000 < 1:
                                                digit_list[3] = -1
                    elif score / 10000 < 1:
                                                digit_list[4] = -1
                    elif score / 100000 < 1:
                                                digit_list[5] = -1
                    elif score / 1000000 < 1:
                                                digit_list[6] = -1
                    elif score / 10000000 < 1:
                                                digit_list[7] = -1
                    for i in range(len(fruit_matrix)):
                            for j in range(len(fruit_matrix[i])):
                                if fruit_matrix[i][j] > 0:
                                    screen.blit(fruit_list[fruit_matrix[i][j] - 1], (object_coords[i][j][0], object_coords[i][j][1] + 2))
                    for n in range(len(digit_list)):
                                if digit_list[n] == 0:
                                    screen.blit(d0, digit_coord_list[n])
                                elif digit_list[n] == 1:
                                    screen.blit(d1, digit_coord_list[n])
                                elif digit_list[n] == 2:
                                    screen.blit(d2, digit_coord_list[n])
                                elif digit_list[n] == 3:
                                    screen.blit(d3, digit_coord_list[n])
                                elif digit_list[n] == 4:
                                    screen.blit(d4, digit_coord_list[n])
                                elif digit_list[n] == 5:
                                    screen.blit(d5, digit_coord_list[n])
                                elif digit_list[n] == 6:
                                    screen.blit(d6, digit_coord_list[n])
                                elif digit_list[n] == 7:
                                    screen.blit(d7, digit_coord_list[n])
                                elif digit_list[n] == 8:
                                    screen.blit(d8, digit_coord_list[n])
                                elif digit_list[n] == 9:
                                    screen.blit(d9, digit_coord_list[n])
                    if level < 18:
                                screen.blit(fruit_list[level-1], (566, 368))
                    else:
                                screen.blit(fruit_list[17], (566, 368))
                    screen.blit(special_extra, (254, 10))
                    for i in range(len(special_extra_list)):
                        if i > 6:
                            if special_extra_list[i] == 1:
                                screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
                        else:
                            if special_blinking:
                                screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
                    for i in range(border_color_change_state):
                            if border_color_change_list[i][0][2] == 1:
                                screen.blit(border_h_green, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
                                screen.blit(border_h_green, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
                            elif border_color_change_list[i][0][2] == 2:
                                screen.blit(border_v_green, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
                                screen.blit(border_v_green, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
                            elif border_color_change_list[i][0][2] == 3:
                                screen.blit(border_v_green2, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
                                screen.blit(border_v_green2, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
                    pygame.display.flip()
                    t1 = pygame.time.get_ticks()
                    pygame.time.wait(int(10 - (t1 - t0)))
                
                screen.fill(pygame.Color('black'))
                screen.blit(pink_background, (0,0))
                screen.blit(pink_obstacles, (0,0))
                if latest_key_pressed == 'up':      
                                screen.blit(ladybug_list[0][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'down':      
                                screen.blit(ladybug_list[1][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'left':      
                                screen.blit(ladybug_list[2][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'right':      
                                screen.blit(ladybug_list[3][ladybug_animation_stage], (int(l_x), int(l_y)))
                if lives == 4:
                                screen.blit(lives_4, (58, 370))
                elif lives == 3:
                                screen.blit(lives_3, (58, 370))
                elif lives == 2:
                                screen.blit(lives_2, (58, 370))
                    
                score_string = str(score)[::-1]
                for n in range(len(score_string)):
                                                digit_list[n] = int(score_string[n])
                if score / 10 < 1:
                                                digit_list[1] = -1
                elif score / 100 < 1:
                                                digit_list[2] = -1
                elif score / 1000 < 1:
                                                digit_list[3] = -1
                elif score / 10000 < 1:
                                                digit_list[4] = -1
                elif score / 100000 < 1:
                                                digit_list[5] = -1
                elif score / 1000000 < 1:
                                                digit_list[6] = -1
                elif score / 10000000 < 1:
                                                digit_list[7] = -1
                for n in range(len(digit_list)):
                                if digit_list[n] == 0:
                                    screen.blit(d0, digit_coord_list[n])
                                elif digit_list[n] == 1:
                                    screen.blit(d1, digit_coord_list[n])
                                elif digit_list[n] == 2:
                                    screen.blit(d2, digit_coord_list[n])
                                elif digit_list[n] == 3:
                                    screen.blit(d3, digit_coord_list[n])
                                elif digit_list[n] == 4:
                                    screen.blit(d4, digit_coord_list[n])
                                elif digit_list[n] == 5:
                                    screen.blit(d5, digit_coord_list[n])
                                elif digit_list[n] == 6:
                                    screen.blit(d6, digit_coord_list[n])
                                elif digit_list[n] == 7:
                                    screen.blit(d7, digit_coord_list[n])
                                elif digit_list[n] == 8:
                                    screen.blit(d8, digit_coord_list[n])
                                elif digit_list[n] == 9:
                                    screen.blit(d9, digit_coord_list[n])
                if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
                else:
                                screen.blit(fruit_list[17], (566, 368))
                screen.blit(special_extra, (254, 10))
                for i in range(len(special_extra_list)):
                        if i > 6:
                            if special_extra_list[i] == 1:
                                screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.wait(2000)
                special_extra_list[0] = 0
                special_extra_list[1] = 0
                special_extra_list[2] = 0
                special_extra_list[3] = 0
                special_extra_list[4] = 0
                special_extra_list[5] = 0
                special_extra_list[6] = 0
                level += 1
                ladybug_speed = 1.8
        
            if special_extra_list[11] == 1 and special_extra_list[10] == 1 and special_extra_list[9] == 1 and special_extra_list[8] == 1 and special_extra_list[7] == 1:
                
                sound_extra.play()
                running = False
                bug_list = []
                screen.fill(pygame.Color('black'))
                screen.blit(pink_background, (0,0))
                screen.blit(pink_obstacles, (0,0))
                screen.blit(special_extra, (254,10))
                extra_blinking = 0
                for i in range(len(door_pos)):
                    if door_pos[i] == 1:
                        screen.blit(door_v, door_v_coords[i])
                    else:
                        screen.blit(door_h, door_h_coords[i])
                for i in range(len(object_matrix)):
                    for j in range(len(object_matrix[i])):
                        if object_matrix[i][j] == 1:
                            if i % 2 == 0:
                                screen.blit(bar_right, object_coords[i][j])
                            else:
                                screen.blit(bar_left, object_coords[i][j])
                        elif object_matrix[i][j] == 2:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_S, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_S, object_coords[i][j])
                            else:
                                screen.blit(blue_S, object_coords[i][j])
                        elif object_matrix[i][j] == 3:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_P, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_P, object_coords[i][j])
                            else:
                                screen.blit(blue_P, object_coords[i][j])
                        elif object_matrix[i][j] == 4:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_E, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_E, object_coords[i][j])
                            else:
                                screen.blit(blue_E, object_coords[i][j])
                        elif object_matrix[i][j] == 5:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_C, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_C, object_coords[i][j])
                            else:
                                screen.blit(blue_C, object_coords[i][j])
                        elif object_matrix[i][j] == 6:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_I, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_I, object_coords[i][j])
                            else:
                                screen.blit(blue_I, object_coords[i][j])
                        elif object_matrix[i][j] == 7:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_A, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_A, object_coords[i][j])
                            else:
                                screen.blit(blue_A, object_coords[i][j])
                        elif object_matrix[i][j] == 8:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_L, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_L, object_coords[i][j])
                            else:
                                screen.blit(blue_L, object_coords[i][j])
                        elif object_matrix[i][j] == 9:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_X, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_X, object_coords[i][j])
                            else:
                                screen.blit(blue_X, object_coords[i][j])
                        elif object_matrix[i][j] == 10:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_T, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_T, object_coords[i][j])
                            else:
                                screen.blit(blue_T, object_coords[i][j])
                        elif object_matrix[i][j] == 11:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_R, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_R, object_coords[i][j])
                            else:
                                screen.blit(blue_R, object_coords[i][j])
                        elif object_matrix[i][j] == 12:
                            if 0 <= timer % 10 < 1:
                                screen.blit(red_heart, object_coords[i][j])
                            elif 1 <= timer % 10 < 4:
                                screen.blit(green_heart, object_coords[i][j])
                            else:
                                screen.blit(blue_heart, object_coords[i][j])
                        elif object_matrix[i][j] == 13:
                            screen.blit(skull, object_coords[i][j])
                         
                if latest_key_pressed == 'up':      
                    screen.blit(ladybug_list[0][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'down':      
                    screen.blit(ladybug_list[1][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'left':      
                    screen.blit(ladybug_list[2][ladybug_animation_stage], (int(l_x), int(l_y)))
                elif latest_key_pressed == 'right':      
                    screen.blit(ladybug_list[3][ladybug_animation_stage], (int(l_x), int(l_y)))
                
                
                for i in range(len(special_extra_list)):
                    if special_extra_list[i] == 1:
                        screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
                if lives == 4:
                    screen.blit(lives_4, (58, 370))
                elif lives == 3:
                    screen.blit(lives_3, (58, 370))
                elif lives == 2:
                    screen.blit(lives_2, (58, 370))
                if multiplier == 2:
                    screen.blit(x2, (310,368))
                elif multiplier == 3:
                    screen.blit(x3, (310,368))
                elif multiplier == 5:
                    screen.blit(x5, (310,368))
                for n in range(len(digit_list)):
                    if digit_list[n] == 0:
                        screen.blit(d0, digit_coord_list[n])
                    elif digit_list[n] == 1:
                        screen.blit(d1, digit_coord_list[n])
                    elif digit_list[n] == 2:
                        screen.blit(d2, digit_coord_list[n])
                    elif digit_list[n] == 3:
                        screen.blit(d3, digit_coord_list[n])
                    elif digit_list[n] == 4:
                        screen.blit(d4, digit_coord_list[n])
                    elif digit_list[n] == 5:
                        screen.blit(d5, digit_coord_list[n])
                    elif digit_list[n] == 6:
                        screen.blit(d6, digit_coord_list[n])
                    elif digit_list[n] == 7:
                        screen.blit(d7, digit_coord_list[n])
                    elif digit_list[n] == 8:
                        screen.blit(d8, digit_coord_list[n])
                    elif digit_list[n] == 9:
                        screen.blit(d9, digit_coord_list[n])
                if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
                else:
                    screen.blit(fruit_list[17], (566, 368))
                    
                if fruit_out:
                    if level < 18:
                        screen.blit(fruit_list[level-1], (314,196))
                    else:
                        screen.blit(fruit_list[17], (314,196))
                bug_coord_list = []
                for b in bug_list:
                    already_exists = False
                    for t in bug_coord_list:
                        if b.return_x() == t[0] and b.return_y() == t[1]:
                            already_exists = True
                    if not already_exists:
                        tup = b.return_x_y_image()
                        screen.blit(tup[1], tup[0])
                        bug_coord_list.append(tup[0])
                pygame.display.flip()
                pygame.event.pump()
                
                pygame.time.wait(1000)
                
                l_x = 330
                l_y = 146
                screen.fill(pygame.Color('black'))
                screen.blit(extra_background, (0,0))
                screen.blit(special_extra, (254,10))
                screen.blit(ladybug_list[0][0], (int(l_x), int(l_y)))
                screen.blit(pink_background, (0,0))
                for i in range(len(special_extra_list)):
                    if special_extra_list[i] == 1:
                        screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
                if lives == 4:
                    screen.blit(lives_4, (58, 370))
                elif lives == 3:
                    screen.blit(lives_3, (58, 370))
                elif lives == 2:
                    screen.blit(lives_2, (58, 370))
                if multiplier == 2:
                    screen.blit(x2, (310,368))
                elif multiplier == 3:
                    screen.blit(x3, (310,368))
                elif multiplier == 5:
                    screen.blit(x5, (310,368))
                for n in range(len(digit_list)):
                    if digit_list[n] == 0:
                        screen.blit(d0, digit_coord_list[n])
                    elif digit_list[n] == 1:
                        screen.blit(d1, digit_coord_list[n])
                    elif digit_list[n] == 2:
                        screen.blit(d2, digit_coord_list[n])
                    elif digit_list[n] == 3:
                        screen.blit(d3, digit_coord_list[n])
                    elif digit_list[n] == 4:
                        screen.blit(d4, digit_coord_list[n])
                    elif digit_list[n] == 5:
                        screen.blit(d5, digit_coord_list[n])
                    elif digit_list[n] == 6:
                        screen.blit(d6, digit_coord_list[n])
                    elif digit_list[n] == 7:
                        screen.blit(d7, digit_coord_list[n])
                    elif digit_list[n] == 8:
                        screen.blit(d8, digit_coord_list[n])
                    elif digit_list[n] == 9:
                        screen.blit(d9, digit_coord_list[n])
                if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
                else:
                    screen.blit(fruit_list[17], (566, 368))
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.wait(500)
                
                phase = 0
                while l_y < 182:
                    l_y += 2
                    if extra_blinking == 0:
                        special_extra_list[11] = (special_extra_list[11] + 1) % 2
                        special_extra_list[10] = (special_extra_list[10] + 1) % 2
                        special_extra_list[9] = (special_extra_list[9] + 1) % 2
                        special_extra_list[8] = (special_extra_list[8] + 1) % 2
                        special_extra_list[7] = (special_extra_list[7] + 1) % 2
                    extra_animation_screen(l_x, l_y, 1, phase)
                    phase = (phase + 1) % 12
                    extra_blinking = (extra_blinking + 1) % 33
                    pygame.time.wait(15)
                while l_x > 266:
                    l_x -= 2
                    if extra_blinking == 0:
                        special_extra_list[11] = (special_extra_list[11] + 1) % 2
                        special_extra_list[10] = (special_extra_list[10] + 1) % 2
                        special_extra_list[9] = (special_extra_list[9] + 1) % 2
                        special_extra_list[8] = (special_extra_list[8] + 1) % 2
                        special_extra_list[7] = (special_extra_list[7] + 1) % 2
                    extra_animation_screen(l_x, l_y, 2, phase)
                    phase = (phase + 1) % 12
                    extra_blinking = (extra_blinking + 1) % 33
                    pygame.time.wait(15)
                while l_y < 270:
                    l_y += 2
                    if extra_blinking == 0:
                        special_extra_list[11] = (special_extra_list[11] + 1) % 2
                        special_extra_list[10] = (special_extra_list[10] + 1) % 2
                        special_extra_list[9] = (special_extra_list[9] + 1) % 2
                        special_extra_list[8] = (special_extra_list[8] + 1) % 2
                        special_extra_list[7] = (special_extra_list[7] + 1) % 2
                    extra_animation_screen(l_x, l_y, 1, phase)
                    phase = (phase + 1) % 12
                    extra_blinking = (extra_blinking + 1) % 33
                    pygame.time.wait(15)
                while l_x < 376:
                    l_x += 2
                    if extra_blinking == 0:
                        special_extra_list[11] = (special_extra_list[11] + 1) % 2
                        special_extra_list[10] = (special_extra_list[10] + 1) % 2
                        special_extra_list[9] = (special_extra_list[9] + 1) % 2
                        special_extra_list[8] = (special_extra_list[8] + 1) % 2
                        special_extra_list[7] = (special_extra_list[7] + 1) % 2
                    extra_animation_screen(l_x, l_y, 3, phase)
                    phase = (phase + 1) % 12
                    extra_blinking = (extra_blinking + 1) % 33
                    pygame.time.wait(15)
                while l_y > 182:
                    l_y -= 2
                    if extra_blinking == 0:
                        special_extra_list[11] = (special_extra_list[11] + 1) % 2
                        special_extra_list[10] = (special_extra_list[10] + 1) % 2
                        special_extra_list[9] = (special_extra_list[9] + 1) % 2
                        special_extra_list[8] = (special_extra_list[8] + 1) % 2
                        special_extra_list[7] = (special_extra_list[7] + 1) % 2
                    extra_animation_screen(l_x, l_y, 0, phase)
                    phase = (phase + 1) % 12
                    extra_blinking = (extra_blinking + 1) % 33
                    pygame.time.wait(15)
                while l_x > 82:
                    l_x -= 2
                    if extra_blinking == 0:
                        special_extra_list[11] = (special_extra_list[11] + 1) % 2
                        special_extra_list[10] = (special_extra_list[10] + 1) % 2
                        special_extra_list[9] = (special_extra_list[9] + 1) % 2
                        special_extra_list[8] = (special_extra_list[8] + 1) % 2
                        special_extra_list[7] = (special_extra_list[7] + 1) % 2
                    extra_animation_screen(l_x, l_y, 2, phase)
                    phase = (phase + 1) % 12
                    extra_blinking = (extra_blinking + 1) % 33
                    pygame.time.wait(15)
                while l_y < 358:
                    l_y += 2
                    if extra_blinking == 0:
                        special_extra_list[11] = (special_extra_list[11] + 1) % 2
                        special_extra_list[10] = (special_extra_list[10] + 1) % 2
                        special_extra_list[9] = (special_extra_list[9] + 1) % 2
                        special_extra_list[8] = (special_extra_list[8] + 1) % 2
                        special_extra_list[7] = (special_extra_list[7] + 1) % 2
                    extra_animation_screen(l_x, l_y, 1, phase)
                    phase = (phase + 1) % 12
                    extra_blinking = (extra_blinking + 1) % 33
                    pygame.time.wait(15)
                if lives < 4:
                    lives += 1
                extra_animation_screen(l_x, l_y, 1, phase)
                pygame.time.wait(1000)
                special_extra_list[11] = 0
                special_extra_list[10] = 0
                special_extra_list[9] = 0
                special_extra_list[8] = 0
                special_extra_list[7] = 0
                level += 1
                
                
                
            score_string = str(score)[::-1]
            for n in range(len(score_string)):
                digit_list[n] = int(score_string[n])
            if score / 10 < 1:
                digit_list[1] = -1
            elif score / 100 < 1:
                digit_list[2] = -1
            elif score / 1000 < 1:
                digit_list[3] = -1
            elif score / 10000 < 1:
                digit_list[4] = -1
            elif score / 100000 < 1:
                digit_list[5] = -1
            elif score / 1000000 < 1:
                digit_list[6] = -1
            elif score / 10000000 < 1:
                digit_list[7] = -1
            
            for i in bug_list:
                i.walk()
                if frame_number % 20 == 0:
                    i.change_phase()
            t1 = pygame.time.get_ticks()
            pygame.time.wait(int(10 - (t1 - t0)))
            
        #3
            screen.fill(pygame.Color('black'))
            screen.blit(background, (0,0))
            screen.blit(obstacles, (0,0))
            screen.blit(special_extra, (254,10))
            for i in range(len(door_pos)):
                if door_pos[i] == 1:
                    screen.blit(door_v, door_v_coords[i])
                else:
                    screen.blit(door_h, door_h_coords[i])
            for i in range(len(object_matrix)):
                for j in range(len(object_matrix[i])):
                    if object_matrix[i][j] == 1:
                        if i % 2 == 0:
                            screen.blit(bar_right, object_coords[i][j])
                        else:
                            screen.blit(bar_left, object_coords[i][j])
                    elif object_matrix[i][j] == 2:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_S, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_S, object_coords[i][j])
                        else:
                            screen.blit(blue_S, object_coords[i][j])
                    elif object_matrix[i][j] == 3:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_P, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_P, object_coords[i][j])
                        else:
                            screen.blit(blue_P, object_coords[i][j])
                    elif object_matrix[i][j] == 4:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_E, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_E, object_coords[i][j])
                        else:
                            screen.blit(blue_E, object_coords[i][j])
                    elif object_matrix[i][j] == 5:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_C, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_C, object_coords[i][j])
                        else:
                            screen.blit(blue_C, object_coords[i][j])
                    elif object_matrix[i][j] == 6:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_I, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_I, object_coords[i][j])
                        else:
                            screen.blit(blue_I, object_coords[i][j])
                    elif object_matrix[i][j] == 7:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_A, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_A, object_coords[i][j])
                        else:
                            screen.blit(blue_A, object_coords[i][j])
                    elif object_matrix[i][j] == 8:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_L, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_L, object_coords[i][j])
                        else:
                            screen.blit(blue_L, object_coords[i][j])
                    elif object_matrix[i][j] == 9:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_X, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_X, object_coords[i][j])
                        else:
                            screen.blit(blue_X, object_coords[i][j])
                    elif object_matrix[i][j] == 10:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_T, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_T, object_coords[i][j])
                        else:
                            screen.blit(blue_T, object_coords[i][j])
                    elif object_matrix[i][j] == 11:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_R, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_R, object_coords[i][j])
                        else:
                            screen.blit(blue_R, object_coords[i][j])
                    elif object_matrix[i][j] == 12:
                        if 0 <= timer % 10 < 1:
                            screen.blit(red_heart, object_coords[i][j])
                        elif 1 <= timer % 10 < 4:
                            screen.blit(green_heart, object_coords[i][j])
                        else:
                            screen.blit(blue_heart, object_coords[i][j])
                    elif object_matrix[i][j] == 13:
                        screen.blit(skull, object_coords[i][j])
                            
            for i in range(border_color_change_state):
                if border_color_change_list[i][0][2] == 1:
                    screen.blit(border_h_green, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
                    screen.blit(border_h_green, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
                elif border_color_change_list[i][0][2] == 2:
                    screen.blit(border_v_green, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
                    screen.blit(border_v_green, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
                elif border_color_change_list[i][0][2] == 3:
                    screen.blit(border_v_green2, (border_color_change_list[i][0][0], border_color_change_list[i][0][1]))
                    screen.blit(border_v_green2, (border_color_change_list[i][1][0], border_color_change_list[i][1][1]))
                    
            if latest_key_pressed == 'up':      
                screen.blit(ladybug_list[0][ladybug_animation_stage], (int(l_x), int(l_y)))
            elif latest_key_pressed == 'down':      
                screen.blit(ladybug_list[1][ladybug_animation_stage], (int(l_x), int(l_y)))
            elif latest_key_pressed == 'left':      
                screen.blit(ladybug_list[2][ladybug_animation_stage], (int(l_x), int(l_y)))
            elif latest_key_pressed == 'right':      
                screen.blit(ladybug_list[3][ladybug_animation_stage], (int(l_x), int(l_y)))
            
            
            for i in range(len(special_extra_list)):
                if special_extra_list[i] == 1:
                    screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
            if lives == 4:
                screen.blit(lives_4, (58, 370))
            elif lives == 3:
                screen.blit(lives_3, (58, 370))
            elif lives == 2:
                screen.blit(lives_2, (58, 370))
            if multiplier == 2:
                screen.blit(x2, (310,368))
            elif multiplier == 3:
                screen.blit(x3, (310,368))
            elif multiplier == 5:
                screen.blit(x5, (310,368))
            for n in range(len(digit_list)):
                if digit_list[n] == 0:
                    screen.blit(d0, digit_coord_list[n])
                elif digit_list[n] == 1:
                    screen.blit(d1, digit_coord_list[n])
                elif digit_list[n] == 2:
                    screen.blit(d2, digit_coord_list[n])
                elif digit_list[n] == 3:
                    screen.blit(d3, digit_coord_list[n])
                elif digit_list[n] == 4:
                    screen.blit(d4, digit_coord_list[n])
                elif digit_list[n] == 5:
                    screen.blit(d5, digit_coord_list[n])
                elif digit_list[n] == 6:
                    screen.blit(d6, digit_coord_list[n])
                elif digit_list[n] == 7:
                    screen.blit(d7, digit_coord_list[n])
                elif digit_list[n] == 8:
                    screen.blit(d8, digit_coord_list[n])
                elif digit_list[n] == 9:
                    screen.blit(d9, digit_coord_list[n])
                
            if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
            else:
                    screen.blit(fruit_list[17], (566, 368))
                    
            if fruit_out:
                if level < 18:
                    screen.blit(fruit_list[level-1], (314,196))
                else:
                    screen.blit(fruit_list[17], (314,196))
            
            bug_coord_list = []
            for b in bug_list:
                already_exists = False
                for t in bug_coord_list:
                    if b.return_x() == t[0] and b.return_y() == t[1]:
                        already_exists = True
                if not already_exists:
                    tup = b.return_x_y_image()
                    screen.blit(tup[1], tup[0])
                    bug_coord_list.append(tup[0])
            pygame.display.flip()
    if lives == 0:
        in_levels = False


while gameover:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    gameover = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        gameover = False
            screen.fill(pygame.Color('black'))
            screen.blit(game_over, (0,0))
            screen.blit(special_extra, (254,10))
            for i in range(len(special_extra_list)):
                if special_extra_list[i] == 1:
                    screen.blit(special_extra_lighted_list[i][0], special_extra_lighted_list[i][1])
            if multiplier == 2:
                screen.blit(x2, (310,368))
            elif multiplier == 3:
                screen.blit(x3, (310,368))
            elif multiplier == 5:
                screen.blit(x5, (310,368))
            for n in range(len(digit_list)):
                if digit_list[n] == 0:
                    screen.blit(d0, digit_coord_list[n])
                elif digit_list[n] == 1:
                    screen.blit(d1, digit_coord_list[n])
                elif digit_list[n] == 2:
                    screen.blit(d2, digit_coord_list[n])
                elif digit_list[n] == 3:
                    screen.blit(d3, digit_coord_list[n])
                elif digit_list[n] == 4:
                    screen.blit(d4, digit_coord_list[n])
                elif digit_list[n] == 5:
                    screen.blit(d5, digit_coord_list[n])
                elif digit_list[n] == 6:
                    screen.blit(d6, digit_coord_list[n])
                elif digit_list[n] == 7:
                    screen.blit(d7, digit_coord_list[n])
                elif digit_list[n] == 8:
                    screen.blit(d8, digit_coord_list[n])
                elif digit_list[n] == 9:
                    screen.blit(d9, digit_coord_list[n])
                
            if level == 1:
                screen.blit(lvl_1, (234,82))
            elif level == 2:
                screen.blit(lvl_2, (234,82))
            elif level == 3:
                screen.blit(lvl_3, (234,82))
            elif level == 4:
                screen.blit(lvl_4, (234,82))
            elif level == 5:
                screen.blit(lvl_5, (234,82))
            elif level == 6:
                screen.blit(lvl_6, (234,82))
            elif level == 7:
                screen.blit(lvl_7, (234,82))
            elif level == 8:
                screen.blit(lvl_8, (234,82))
            elif level == 9:
                screen.blit(lvl_9, (234,82))
            elif level == 10:
                screen.blit(lvl_10, (234,82))
            elif level == 11:
                screen.blit(lvl_11, (234,82))
            elif level == 12:
                screen.blit(lvl_12, (234,82))
            elif level == 13:
                screen.blit(lvl_13, (234,82))
            elif level == 14:
                screen.blit(lvl_14, (234,82))
            elif level == 15:
                screen.blit(lvl_15, (234,82))
            elif level == 16:
                screen.blit(lvl_16, (234,82))
            elif level == 17:
                screen.blit(lvl_17, (234,82))
            elif level == 18:
                screen.blit(lvl_18, (234,82))
            else:
                screen.blit(lvl_19, (234,82))
                l = level % 10
                screen.blit(blue_digit_list[l], (402,82))
                screen.blit(blue_digit_list[int(((level - l) % 100) / 10)], (370,82))
            if level < 18:
                    screen.blit(fruit_list[level-1], (566, 368))
            else:
                    screen.blit(fruit_list[17], (566, 368))
            pygame.display.flip()
            
            
pygame.quit()