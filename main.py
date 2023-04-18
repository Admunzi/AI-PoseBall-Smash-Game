"""
Game with Pose

This game show pose landmarks on webcam and in the screen is going to be a game where you have to hit the balls with all
the body parts that you can see in the screen.

It uses the mediapipe library to show the pose landmarks on webcam and pygame to show the game.

At the beginning it show a menu with different levels of difficulty, the first one is the easiest and the last one
is the hardest. There are 3 levels of difficulty. (Easy, Medium, Hard)

author: Daniel Ayala Cantador
"""

import sys
import pygame
import cv2

import pose_detection
from game_graphics import GameGraphics, check_difficulty_selection, draw_balls
from ball import Ball
from game import GameManager
from score import ScoreManager
from timer import Timer
from mediapipe.python.solutions import pose as mp_pose

# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN = pygame.display.set_mode((900, 600))
pygame.display.set_caption("PoseBall Smash Game")

# Initialize game objects
GAME_GRAPHICS = GameGraphics(SCREEN)
SCORE_MANAGER = ScoreManager()
GAME_MANAGER = GameManager()
CLOCK = pygame.time.Clock()


def principal_menu():
    GAME_GRAPHICS.display_menu_screen()
    difficulty = check_difficulty_selection()
    initialize_game_variables(difficulty)
    start_game()


def handle_events():
    for event in pygame.event.get():
        # Check if the user clicked the close button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        print("event.type: ", event.type)


def initialize_game_variables(difficulty):
    GAME_MANAGER.set_difficulty(difficulty)
    GAME_MANAGER.set_balls(difficulty)
    SCORE_MANAGER.reset_score()


def start_game():
    # handle_events()  TODO: Fix this
    balls_list = []
    timer = Timer()
    next_ball_time = 0

    # draw pose landmarks on screen
    cap = cv2.VideoCapture(0)
    with mp_pose.Pose(
            model_complexity=1,
            smooth_landmarks=True,
            min_tracking_confidence=0.5,
            min_detection_confidence=0.5) as pose:

        while cap.isOpened():
            # Make sure game doesn't run at more than 60 frames per second.
            CLOCK.tick(60)

            pose_landmarks = pose_detection.get_pose_landmarks(cap, pose)
            GAME_GRAPHICS.draw_landmarks(pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # remove old landmarks
            GAME_GRAPHICS.display_game_screen(SCORE_MANAGER.get_score(), timer, GAME_MANAGER.get_difficulty())
            timer.update_time()

            # add new ball to the list of balls if the time is right
            if int(timer.get_time()) % 2 == 0 and next_ball_time != int(timer.get_time()) \
                    and GAME_MANAGER.get_remaining_balls() > 0:
                next_ball_time = int(timer.get_time())
                ball = Ball(GAME_GRAPHICS.get_screen_size(), GAME_MANAGER.get_speed())
                GAME_MANAGER.decrement_ball()
                balls_list.append(ball)

            draw_balls(balls_list, GAME_GRAPHICS.get_screen())
            check_player_hit_ball(balls_list, pose_landmarks)

            check_all_balls_hit(balls_list)


def check_player_hit_ball(balls_list, pose_landmarks):
    """
    Check if the player hit a ball with the head, left hand, right hand, left foot or right foot.
    """
    for ball in balls_list:
        if ball.check_collision(pose_landmarks):
            SCORE_MANAGER.increment_score()
            balls_list.remove(ball)


def check_all_balls_hit(balls_list):
    """
    Check if all the balls have been hit.
    If all the balls have been hit, the game is over and the player can go back to the menu.
    """
    if len(balls_list) == 0 and GAME_MANAGER.get_remaining_balls() == 0:
        GAME_GRAPHICS.display_game_finish_screen(SCORE_MANAGER.get_score())
        # wait 2 seconds before going back to menu
        pygame.time.delay(20000)
        principal_menu()


principal_menu()
