import pygame, pygame.font, pygame.event, pygame.draw
from pygame.locals import *
from tkinter import *


def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message, id):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  if(1 == id):
    pygame.draw.rect(screen, (0, 0, 0),
                       ((screen.get_width() / 2) - 100,
                        (screen.get_height() / 2) - 20,
                        200, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                     ((screen.get_width() / 2) - 102,
                      (screen.get_height() / 2) - 20,
                      204, 24), 1)
  elif(2 == id):
    pygame.draw.rect(screen, (0, 0, 0),
                       ((screen.get_width() / 2) - 100,
                        (screen.get_height() / 2) + 20,
                        200, 20), 0)
    pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) + 20,
                    204,24), 1)

  if len(message) != 0:
      if (1 == id):
        screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 20))

      elif(2 == id):
          screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                      ((screen.get_width() / 2) - 100 , (screen.get_height() / 2) + 20))

  pygame.display.flip()

def ask(screen, question1, question2):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string1 = []
  current_string2 = []
  current_string2_hide = []
  display_box(screen, question1 + ": " + "".join(current_string1), 1)
  display_box(screen, question2 + ": " + "".join(current_string2), 2)
  while 1:
    if len(current_string1) <= 16:
        inkey = get_key()
        print(inkey)
        if inkey == K_BACKSPACE:
            current_string1 = current_string1[0:-1]
        elif inkey == K_RETURN or inkey == K_TAB:
            if len(current_string1)>= 4:
                break
            else:
                showinfo("")
        elif inkey == K_MINUS:
            current_string1.append("_")
        elif inkey == K_ESCAPE:
            pygame.quit()
        elif inkey <= 127:
            current_string1.append(chr(inkey))
        display_box(screen, question1 + ": " + "".join(current_string1), 1)
    else:
        inkey = get_key()
        if inkey == K_BACKSPACE:
          current_string1 = current_string1[0:-1]
        elif inkey == K_RETURN:
          break
        display_box(screen, question1 + ": " + "".join(current_string1), 1)

  while 1:
    if len(current_string2) <= 16:
        inkey = get_key()
        print(inkey)
        if inkey == K_BACKSPACE:
            current_string2 = current_string2[0:-1]
        elif inkey == K_RETURN or inkey == K_TAB:
            if len(current_string1) >= 4:
                break
            else:
                print("too short")
        elif inkey == K_MINUS:
            current_string2.append("_")
            current_string2_hide.append("*")
        elif inkey == K_ESCAPE:
            pygame.quit()
        elif inkey <= 127:
            current_string2.append(chr(inkey))
            current_string2_hide.append("*")
        display_box(screen, question2 + ": " + "".join(current_string2_hide), 2)
    else:
        inkey = get_key()
        if inkey == K_BACKSPACE:
          current_string1 = current_string1[0:-1]
        elif inkey == K_RETURN:
          break
        display_box(screen, question2 + ": " + "".join(current_string2_hide), 2)

  answer = []
  answer.append(current_string1)
  answer.append(current_string2)
  return answer

def showinfo(infotype):
    pass

def main():
  screen = pygame.display.set_mode((800,600))
  answer = ask(screen, "Username","Password")
  username = "".join(answer[0])
  password = "".join(answer[1])
  #db.login(username, password)


if __name__ == '__main__':
    main()