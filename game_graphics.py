import pygame

pygame.init()


def check_difficulty_selection():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return "easy"
                elif event.key == pygame.K_m:
                    return "medium"
                elif event.key == pygame.K_h:
                    return "hard"


def draw_balls(balls_list, screen):
    for ball in balls_list:
        ball.draw(screen)
        ball.update()


class GameGraphics:
    def __init__(self, screen):
        self.screen_game = screen
        self.screen_width = self.screen_game.get_size()[0]
        self.screen_height = self.screen_game.get_size()[1]

    FONT_BIG = pygame.font.SysFont(None, 48)
    FONT_NORMAL = pygame.font.SysFont(None, 48)

    def display_menu_screen(self):
        self.screen_game.fill((250, 135, 110))
        # Draw menu options on the screen
        title_text = GameGraphics.FONT_BIG.render("PoseBall Smash Game", True, (0, 0, 0))
        options = GameGraphics.FONT_BIG.render("Choose difficulty (Press Key E, M or H)", True, (0, 0, 0))
        easy_text = GameGraphics.FONT_BIG.render("Easy", True, (0, 0, 0))
        medium_text = GameGraphics.FONT_BIG.render("Medium", True, (0, 0, 0))
        hard_text = GameGraphics.FONT_BIG.render("Hard", True, (0, 0, 0))
        self.screen_game.blit(title_text, (self.screen_width / 2 - 160, 100))
        self.screen_game.blit(options, (self.screen_width / 2 - 250, 170))
        self.screen_game.blit(easy_text, (self.screen_width / 2 - 20, 250))
        self.screen_game.blit(medium_text, (self.screen_width / 2 - 50, 300))
        self.screen_game.blit(hard_text, (self.screen_width / 2 - 20, 350))
        pygame.display.flip()

    def display_game_screen(self, score, timer, difficulty):
        self.screen_game.fill((255, 255, 255))  # Fill the screen with white color
        difficulty_text = GameGraphics.FONT_NORMAL.render(f"{difficulty.capitalize()}", True, (243, 65, 44))
        self.screen_game.blit(difficulty_text, (self.screen_width / 2 - 30, 20))
        pygame.display.flip()

        self.display_game_screen_timer(timer)
        self.display_game_screen_score(score)

    def display_game_screen_timer(self, timer):
        # Draw game graphics on the screen
        time_text = GameGraphics.FONT_NORMAL.render(f"Time: {timer}", True, (0, 0, 0))
        self.screen_game.blit(time_text, (20, 20))
        pygame.display.flip()

    def display_game_screen_score(self, score):
        score_text = GameGraphics.FONT_NORMAL.render(f"Score: {score}", True, (0, 0, 0))
        self.screen_game.blit(score_text, (20, 60))
        pygame.display.flip()

    def display_game_finish_screen(self, score):
        self.screen_game.fill((255, 255, 255))  # Fill the screen with white color
        # Draw game over message on the screen
        game_over_text = GameGraphics.FONT_BIG.render("Final", True, (0, 0, 0))
        score_text = GameGraphics.FONT_BIG.render(f"Score: {score}", True, (0, 0, 0))
        self.screen_game.blit(game_over_text, (self.screen_width / 2 - 30, 200))
        self.screen_game.blit(score_text, (self.screen_width / 2 - 50, 300))
        pygame.display.flip()

    def get_screen(self):
        return self.screen_game

    def get_screen_size(self):
        return self.screen_game.get_size()

    def draw_landmarks(self, landmark_list, pose_connections_list):
        if landmark_list is not None:
            for landmark in landmark_list.landmark:
                x, y = int(landmark.x * self.screen_width), int(landmark.y * self.screen_height)
                pygame.draw.circle(self.screen_game, (255, 0, 0), (x, y), 5)

            for pose_connection in pose_connections_list:
                x1, y1 = int(landmark_list.landmark[pose_connection[0]].x * self.screen_width), \
                    int(landmark_list.landmark[pose_connection[0]].y * self.screen_height)
                x2, y2 = int(landmark_list.landmark[pose_connection[1]].x * self.screen_width), \
                    int(landmark_list.landmark[pose_connection[1]].y * self.screen_height)

                pygame.draw.line(self.screen_game, (255, 0, 0), (x1, y1), (x2, y2), 2)
        pygame.display.flip()
