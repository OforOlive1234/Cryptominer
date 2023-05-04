import pygame #this game uses the pygame module
import button #this is just my boilerplate for making buttons work in pygame
import random #this is needed for the rng function used later
import math #this is needed to round some floating point values later

pygame.init()

#create game window
SCREEN_WIDTH = 1280 #pygame constants
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("This game is NOT a cryptominer")
clock = pygame.time.Clock()
fps = 60 #pygame constant for fps

#set timer event
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)

#array containing real life cryptocurrencies featured in game
currencies = ['BTC', 'ETH', 'LTC', 'XRP', 'BCH', 'EOS', 'XLM', 'ADA', 'TRX', 'XMR']

#module which picks one of the currencies for use in that session via a random number generator
def generateCurrencyName():
    num_id = random.randint(0, 9)
    #case statement to return the currency name based on the random number generated
    match num_id:
        case 0:
            return currencies[0]
        case 1:
            return currencies[1]
        case 2:
            return currencies[2]
        case 3:
            return currencies[3]
        case 4:
            return currencies[4]
        case 5:
            return currencies[5]
        case 6:
            return currencies[6]
        case 7:
            return currencies[7]
        case 8:
            return currencies[8]
        case 9:
            return currencies[9]



#game variables (global variables)
game_over = False
game_paused = False
menu_state = "main"
time_elapsed = 0
alg_upgrade_cost = 50
alg_count = 0
har_count = 0
har_upgrade_cost = 100
coins = 0
total_coins = 0
coins_upgrade = 1
auto_coins = 0

#define fonts
font = pygame.font.SysFont("Arial", 24, bold=True)
small_font = pygame.font.SysFont("Arial", 16, bold=True)
big_font = pygame.font.SysFont("Arial", 48, bold=True)

#define colours
TEXT_COL = (20, 30, 40)

#create currency name
currency_name = generateCurrencyName()

#load button images
resume_img = pygame.image.load("assets/button_resume.png").convert_alpha()
quit_img = pygame.image.load("assets/button_quit.png").convert_alpha()
alg_img = pygame.image.load("assets/upgradealg.png").convert_alpha()
har_img = pygame.image.load("assets/upgradehar.png").convert_alpha()
mine_img = pygame.image.load("assets/mine.png").convert_alpha()

#create button instances
resume_button = button.Button((SCREEN_WIDTH // 2) - 75, SCREEN_HEIGHT // 3, resume_img, 1)
quit_button = button.Button((SCREEN_WIDTH // 2) - 50, SCREEN_HEIGHT*2 // 3, quit_img, 1)
alg_button = button.Button((SCREEN_WIDTH // 2) - 75, SCREEN_HEIGHT // 3, alg_img, 1)
har_button = button.Button((SCREEN_WIDTH // 2) - 75, SCREEN_HEIGHT*2 // 3, har_img, 1)
mine_button = button.Button((SCREEN_WIDTH // 7), SCREEN_HEIGHT // 2 - 60, mine_img, 1)

#function to draw text in pygame
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop (while loop)
run = True

while run:
  #draw background
  screen.fill((255, 255, 255))
  clock.tick(fps)

  #pygame event handler (for loop)
  for event in pygame.event.get():
    # nested if for handling various events
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        game_paused = True
    
    elif event.type == pygame.QUIT:
      run = False
    elif event.type == timer_event: #makes auto_coins increase coins every second
      if game_paused == False:
        coins += auto_coins
        total_coins += auto_coins
  
  else:
    if time_elapsed >= 180:
      game_over = True

    if game_paused == False:
      time_elapsed += 1/fps

    if game_over == True:
      auto_coins = 0
      draw_text("Game Over", big_font, TEXT_COL, (SCREEN_WIDTH // 2) - 90, SCREEN_HEIGHT // 4)
      draw_text(f"You mined a total of {math.floor(total_coins)} {currency_name}", font, TEXT_COL, (SCREEN_WIDTH // 2) - 120, SCREEN_HEIGHT // 3)
      draw_text("Press CTRL to restart or SHIFT to quit", small_font, TEXT_COL, (SCREEN_WIDTH // 2) - 125, SCREEN_HEIGHT // 2)
      
    #WHEN GAME IS OVER AND CTRL IS PRESSED, RESTART GAME
    if game_over == True and event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
        game_over = False
        game_paused = False
        menu_state = "main"
        time_elapsed = 0
        alg_upgrade_cost = 50.0
        alg_count = 0
        har_count = 0
        har_upgrade_cost = 100.0
        coins = 0
        total_coins = 0
        coins_upgrade = 1
        auto_coins = 0
        currency_name = generateCurrencyName()
      elif event.key == pygame.K_LALT or event.key == pygame.K_RALT:
        draw_text("Secret easter egg!", font, TEXT_COL, (SCREEN_WIDTH // 2) - 90, SCREEN_HEIGHT // 4)
        pygame.time.delay(2000)
        run = False
      elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
        run = False
      else:
        pass

    else:
       #draw game elements
      if game_paused == False and game_over == False:
        draw_text(f"Time: {int(180 - time_elapsed)} seconds", font, TEXT_COL, (SCREEN_WIDTH // 2) - 80, 50)
        draw_text(f"You have {math.floor(coins)} {currency_name}", font, TEXT_COL, (SCREEN_WIDTH // 2) - 75, SCREEN_HEIGHT // 5)
        draw_text(f"Esc to open Menu", font, TEXT_COL, SCREEN_WIDTH*2 // 2, SCREEN_HEIGHT // 5)
        draw_text(f"Click to mine", font, TEXT_COL, (SCREEN_WIDTH // 5), SCREEN_HEIGHT // 2 - 90)

        draw_text(f"Algorithm Upgrades Purchased: {alg_count}", small_font, TEXT_COL, (SCREEN_WIDTH // 2) - 90, SCREEN_HEIGHT // 3 + 85)
        draw_text(f"Next Upgrade Cost: {math.ceil(alg_upgrade_cost)} {currency_name}", small_font, TEXT_COL, (SCREEN_WIDTH // 2) - 70, SCREEN_HEIGHT // 3 + 105)
        draw_text(f"Hardware Upgrades Purchased: {har_count}", small_font, TEXT_COL, (SCREEN_WIDTH // 2) - 90, SCREEN_HEIGHT*2 // 3 + 85)
        draw_text(f"Next Upgrade Cost: {math.ceil(har_upgrade_cost)} {currency_name}", small_font, TEXT_COL, (SCREEN_WIDTH // 2) - 70, SCREEN_HEIGHT*2 // 3 + 105)

        draw_text(f"Coins per click: {coins_upgrade}", font, TEXT_COL, (SCREEN_WIDTH*4 // 5) - 100, SCREEN_HEIGHT // 2 - 30)
        draw_text(f"Coins per second: {auto_coins}", font, TEXT_COL, (SCREEN_WIDTH*4 // 5) - 100, SCREEN_HEIGHT // 2 + 30)
        if alg_button.draw(screen) and coins >= alg_upgrade_cost: #this runs if they click the button 
          coins_upgrade += (1 + math.floor(coins_upgrade*0.1) ) #this increases the amount of coins you get per click
          alg_count += 1
          coins -= alg_upgrade_cost
          alg_upgrade_cost *= 1.3
        if mine_button.draw(screen): #this runs if they click the mine button
          coins += coins_upgrade
          total_coins += coins_upgrade
        if har_button.draw(screen) and coins >= har_upgrade_cost:
          auto_coins += (5 + math.floor(auto_coins*0.2) ) #this increases the amount of coins you get per second
          har_count += 1
          coins -= har_upgrade_cost
          har_upgrade_cost *= 1.6
      #controls what happens when the game is paused
      if game_paused == True:
      #check menu state
        if menu_state == "main":
        #draw pause screen buttons
          if resume_button.draw(screen):
            game_paused = False
          if quit_button.draw(screen):
            run = False
        draw_text(f"Game and Assets by Oliver Grant", small_font, TEXT_COL, (SCREEN_WIDTH // 2) - 90, SCREEN_HEIGHT*3 // 4 + 40)
        draw_text(f"Made with PyGame", small_font, TEXT_COL, (SCREEN_WIDTH // 2) - 50, SCREEN_HEIGHT*3 // 4 + 60)

    pygame.display.update()

pygame.quit()