import random
import pygame
import sys 

while True:
    pygame.init() # used for initializing pygame and pygame.font

    window1 = pygame.display.set_mode((600,512))

    pipeimage = 'images/pipe.png'
    pipeimage2 = 'images/pipe2.png'
    background_image = 'images/background.jpg'
    birdplayer_image = 'images/bird.png'
    sealevel_image = 'images/base.jfif'



        


    bird1 = pygame.image.load(birdplayer_image)
    birdX = 300
    birdY = 512//2

    birdX_change = 0
    birdY_change = 0.0

    def bird_display(x,y):
        window1.blit(bird1,(x,y))






    background1 = pygame.image.load(background_image)
    def background_display():
        window1.blit(background1,(0,0))






    pipe1 = pygame.image.load(pipeimage)
    pipe2 = pygame.image.load(pipeimage2)
    # pipe2 = pygame.transform.rotate(pipe1,180)


    pipeX_change = 1  

    pipeY = random.randint(0,300) # if y is 0 then the while pipe of height 320 will show and if Y = 300 the the pipe will be pushed down by 300 and only 20 of its height outof 320 will be visible
    pipeX = 512

    pipeY2 = random.randint(0,300) 
    # pipeX2 = 512 + random.randint(120,140)   # this is distance between pipes horizontal
    pipeX2 = 512 + random.randint(50,80) + 50   # this is distance between pipes horizontal
                
    distance_bet_pipes_vertical = random.randint(130,170)
    distance_bet_pipes_vertical2 = random.randint(130,170)


    def createPipe(x,y):
        
        global distance_bet_pipes_vertical,distance_bet_pipes_vertical2
        window1.blit(pipe1,(x,y+(512-320)+5)) # we have to push the image down by 512(window height) - 320(pipe img height) (+5 is the leeway)
        window1.blit(pipe2,(x,0 - distance_bet_pipes_vertical))

    def createPipe2(x,y):

        global distance_bet_pipes_vertical2,distance_bet_pipes_vertical
        window1.blit(pipe1,(x,y+(512-320)+5)) # we have to push the image down by 512(window height) - 320(pipe img height) (+5 is the leeway)
        window1.blit(pipe2,(x,0 - distance_bet_pipes_vertical2))






    def isCollided(pipeX,pipeY,pipeX2,pipeY2):


        # collision system for **PIPE SET 1**
        if(pipeX<=birdX+43/2 and pipeX + 52 >= birdX):   # if statement for when pipe is in bird path  (43 is the width of the bird image)

            if(birdY + 5 >= pipeY+(512-320)) or (birdY <= (320 - distance_bet_pipes_vertical - 10)):    # (colloision condion for bellow pipe) or (collision condition for above pipe)
                # +10 and -10 in thw above if statement is the leeway caz png image is transparent and hence the player charecter is smaller than the actual image size
                # print("game over")
                return True


        # collision system for **PIPE SET 2**
        if(pipeX2<=birdX+43/2 and pipeX2 + 52 >= birdX):   # if statement for when pipe is in bird path  (43 is the width of the bird image)

            if(birdY + 5 >= pipeY2+(512-320)) or (birdY <= (320 - distance_bet_pipes_vertical - 10)):    # (colloision condion for bellow pipe) or (collision condition for above pipe)
                # +10 and -10 in thw above if statement is the leeway caz png image is transparent and hence the player charecter is smaller than the actual image size
                # print("game over")
                return True 


    font2 = pygame.font.Font("HIGH SPEED.ttf", 60)
    def gameOver (collision):
        if collision:
            render2 = font2.render("GAME OVER", True, (255, 0, 0))
            window1.blit(render2, (100,170))
            return -1000,-1000,-1000
        





    def getInput():
        global run1,birdY_change,run2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                run1=False
                                                                                                                                                        
            if event.type == pygame.KEYDOWN:
                run1,run2 =True,False
                if event.key == pygame.K_SPACE:
                    birdY_change = -0.1/0.1


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    birdY_change = 0.1/0.08



    

    fps1 = 120
    fps_clock = pygame.time.Clock()



    score = 0
    font1 = pygame.font.Font("arial.ttf",40 )
    def displayScore(score1):
        score2_str = str(score1)
        scoreImg = font1.render(score2_str,True,(0,0,0))
        window1.blit(scoreImg,(0,0))


    global run1
    run1 = True


    while run1:



        getInput()




        background_display() 



        birdX += birdX_change
        birdY += birdY_change     

        if (birdY>500-10):
            birdY = 499-10
            run1 = False

        if (birdY<0):
            birdY = 1
            run1 = False             


        bird_display(birdX,birdY)







        pipeX -= pipeX_change
        pipeX2 -= pipeX_change

        # make pipe disappear after they reach the end of the screen(left side)
        # width of pipe is 52 hence when X value is -52 the whole pipe is invisible to the player
        if(pipeX<-52):
            pipeX = 512 + 10
            pipeY = random.randint(20,200)
            distance_bet_pipes_vertical = random.randint(130,170)

        if(pipeX2<-52):  
            pipeX2 = 512 + random.randint(60,100) # this is distance between pipes horizontal
            pipeY2 = random.randint(20,200)
            distance_bet_pipes_vertical2 = random.randint(130,170)

        if abs(pipeX - pipeX2)<40:    # hopefully this will prevens the overlapping of pipes 
            pipeX2 = pipeX2 + 100 


        
        createPipe(pipeX,pipeY)
        createPipe2(pipeX2,pipeY2)
        


        displayScore(score)



        col = isCollided(pipeX,pipeY,pipeX2,pipeY2)
        if col:
            run1=False 
            print(score)
            birdX, pipeX, pipeX2 = gameOver(col)    
            pass     

        if pipeX == 255:
            score += 1
            print(score)
        
        if pipeX2 == 255:
            score += 1
            print(score)


        pygame.display.update()

        fps_clock.tick(fps1) # should always be placed after .update()  ,, this function is to prevent errors like pipe overlaping or tilting from happening
        # and also not habe 100% cpu usage 

    run2 = True
    while run2:
        getInput()
        background_display()
        gameOver(True)
        createPipe(-1000,-1000)
        createPipe2(-1000,-1000)
        bird_display(-1000,-1000)

         

        pygame.display.update()

