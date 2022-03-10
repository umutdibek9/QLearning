# Only numpy
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import pygame
import sys
import tkinter

size = 50
toplam_odul= 0 
konum = dict()
for i in range(0, size*size):
    string = "S" + str(i+1)
    konum[string] = i
    
odul_listesi = []
adim_listesi= []
neigs=[]

pencere = tk.Tk()

pencere.geometry("350x250")
 
pencere.grid()

pencere.configure(background='yellow')

L1 = tk.Label(pencere, text="Baslangic",bg='#fff',fg='#1f77b4')
L1.pack()
E1 = tk.Entry(pencere, bg='#fff', fg='#000')
E1.pack()

L2 = tk.Label(pencere, text="Cikis",bg='#fff',fg='#1f77b4')
L2.pack()
E2 = tk.Entry(pencere, bg='#fff', fg='#000')
E2.pack()

returnList = list()

def end():
    
    returnList.append(E1.get())
    returnList.append(E2.get())
    pencere.destroy()

button1 = tk.Button(pencere, text = "Enter" , width=20, command=end,bg='#fff',fg='#1f77b4')
button1.pack()
pencere.mainloop()



goruntu_array = np.ones(size*size)
goruntu_array[:int(size*size*0.3)] = 0

np.random.shuffle(goruntu_array)
goruntu_array = (np.random.rand(size*size) > 0.3).astype(int)
goruntu_array = np.where(goruntu_array == 0, -5, goruntu_array)
goruntu_array = np.where(goruntu_array == 1, 3, goruntu_array)
goruntu_array = goruntu_array.reshape((size,size))

engel_array = np.zeros((size*size,size*size), dtype=bool)


durum_konum = dict((state, location)
                         for location, state in konum.items())


Q = np.array(np.zeros([size*size, size*size]))


def get_optimal_route(bas_kon, son_kon):
    max_steps = 0
    max_point = 0
    # Copy the r_array matrix to new Matrix
    
    # Get the ending state corresponding to the ending location as given
    ending_state = konum[son_kon]
    baslangic_durum = konum[bas_kon]
    # With the above information automatically set the priority of the given ending state to the highest one
    goruntu_array[int(ending_state/size)][ending_state % size]=999
    #r_array_new[baslangic_durum, baslangic_durum] = 0
    goruntu_array[int(baslangic_durum/size)][baslangic_durum % size]=0
    
    engelDosyasi = open("engel.txt", "w")

    for i in range(size):
        for j in range(size):

            if goruntu_array[i, j] == -5:
                engelDosyasi.write("("+str(i) + "," + str(j) + ",K" + ")\n")
            elif goruntu_array[i, j] == 0:
                engelDosyasi.write("("+str(i) + "," + str(j) + ",M" + ")\n")
            elif goruntu_array[i, j] == 999:
                engelDosyasi.write("("+str(i) + "," + str(j) + ",Y" + ")\n")
            else:
                engelDosyasi.write("("+str(i) + "," + str(j) + ",B" + ")\n")

    engelDosyasi.close()
# Define the r_array
    r_array = np.array(np.zeros([size*size, size*size]))
    
    for i in range(0, size):
        for j in range(0, size):
            if(i != size-1):
                r_array[i*size+j][(i+1)*size+j] = goruntu_array[i+1][j]
            if(i != 0):
                r_array[i*size+j][(i-1)*size+j] = goruntu_array[i-1][j]
            if(j != 0):
                r_array[i*size+j][i*size+(j-1)] = goruntu_array[i][j-1]
            if(j != size-1):
                r_array[i*size+j][i*size+(j+1)] = goruntu_array[i][j+1]
            if(j != size-1 and i != 0):
                r_array[i*size+j][(i-1)*size+(j+1)] = goruntu_array[i-1][j+1]
            if(j != 0 and i != 0):
                r_array[i*size+j][(i-1)*size+(j-1)] = goruntu_array[i-1][j-1]
            if(j != size-1 and i != size-1):
                r_array[i*size+j][(i+1)*size+(j+1)] = goruntu_array[i+1][j+1]
            if(j != 0 and i != size-1):
                r_array[i*size+j][(i+1)*size+(j-1)] = goruntu_array[i+1][j-1]
                
    r_array_new = np.copy(r_array)
    print(goruntu_array)
    print("************************************************")
    print(r_array)
    print("************************************************")
    
    anlik_durum = baslangic_durum
   
    for i in range(5000000):
        
        if (i%100000==0):
            print(i)
        hareketler = []
        
        neigs=[]
        neigs.clear()
    
        if int((anlik_durum)/size)==0 and int((anlik_durum)%size)==0:
           b=(anlik_durum+size,anlik_durum+1,anlik_durum+size+1)
           neigs.append(b)
           
        elif int((anlik_durum)/size)==0 and (int((anlik_durum)%size)>0 and int((anlik_durum)%size)<=49):
           b=(anlik_durum+size,anlik_durum+1,anlik_durum+size+1,anlik_durum-1,anlik_durum+size-1)
           neigs.append(b)
           
        elif int((anlik_durum)/size)==0 and int((anlik_durum)%size)==49:
           b=(anlik_durum+size,anlik_durum-1,anlik_durum+size-1)
           neigs.append(b)
           
        elif int((anlik_durum)/size)==49 and int((anlik_durum)%size)==49:
          b=(anlik_durum-size,anlik_durum-1,anlik_durum-size-1)
          neigs.append(b)
          
        elif int((anlik_durum)/size)==49 and int((anlik_durum)%size)==0:
          b=(anlik_durum-size,anlik_durum+1,anlik_durum-size+1)
          neigs.append(b)
          
        elif int((anlik_durum)/size)==49 and (int((anlik_durum)%size)>0 and int((anlik_durum)%size)<=49):
          b=(anlik_durum-size,anlik_durum+1,anlik_durum-1,anlik_durum-size-1,anlik_durum-size+1)
          neigs.append(b)
          
        elif (int((anlik_durum)/size)>0 and int((anlik_durum)/size)<=49) and int((anlik_durum)%size)==49:
            b=(anlik_durum-size,anlik_durum+size,anlik_durum-1,anlik_durum-size-1,anlik_durum+size-1)
            neigs.append(b)
            
        elif (int((anlik_durum)/size)>0 and int((anlik_durum)/size)<=49) and int((anlik_durum)%size)==0:
            b=(anlik_durum-size,anlik_durum+1,anlik_durum+size,anlik_durum+size+1,anlik_durum-size+1)
            neigs.append(b)
            
        else:
            b=(anlik_durum-size,anlik_durum+size,anlik_durum+1,anlik_durum-1,anlik_durum-size-1,anlik_durum-size+1,anlik_durum+size-1,anlik_durum+size+1)
            neigs.append(b)
        
        for p in neigs:
          for variable in p:
              if r_array_new[anlik_durum, variable] != 0 and engel_array[anlik_durum,variable]!=True:
                  hareketler.append(variable)
               
        diger_durum = np.random.choice(hareketler)
       
        Q[anlik_durum, diger_durum] = r_array_new[anlik_durum,
                                                   diger_durum] + 0.75 * (Q[diger_durum, np.argmax(Q[diger_durum, ])])
       
           
        if (r_array_new[anlik_durum,diger_durum]==-5):

                engel_array[:,diger_durum]=True
                max_point = max_point-5
                max_steps = max_steps+1
                adim_listesi.append(max_steps)
                odul_listesi.append(max_point)
                anlik_durum=baslangic_durum
                max_steps = 0
                max_point=0
                
        elif r_array_new[anlik_durum,diger_durum]==999:
                max_point += 5
                print("odul")
                max_steps = max_steps+1
                adim_listesi.append(max_steps)
                odul_listesi.append(max_point)
                anlik_durum=baslangic_durum
                max_steps = 0
                max_point=0
        else:
            max_point+=3        
            anlik_durum= diger_durum
            max_steps+=1
         
    route = [bas_kon]
    diger_kon = bas_kon
    while(diger_kon != son_kon):
        
        baslangic_durum = konum[bas_kon]
        diger_durum = np.argmax(Q[baslangic_durum, ])
        diger_kon = durum_konum[diger_durum]
        route.append(diger_kon)
        bas_kon = diger_kon

    return route



gidilecek_yol = get_optimal_route('S'+str(returnList[0]), 'S'+str(returnList[1]))

fig ,axs = plt.subplots(2)
plt.figure(figsize=(20,100))
axs[0].plot(odul_listesi)
axs[0].set_xlabel("episode")
axs[0].set_ylabel("reward")

axs[1].plot(adim_listesi)
axs[1].set_xlabel("episode")
axs[1].set_ylabel("step")

axs[0].grid(True)
axs[1].grid(True)

plt.show()

def show_path():
    
    def color_path(surface, nums):
        
        for i in range(0, size):
            for j in range(0, size):
                if nums[i][j] == -5:
                    pygame.draw.rect(surface, (46, 92, 184), pygame.Rect((j * 12, i * 12,), (12, 12)))
                if nums[i][j] == 3:
                    pygame.draw.rect(surface, (77, 255, 255), pygame.Rect((j * 12, i * 12,), (12, 12)))
                if ("S"+str((i*size+j)+1) in gidilecek_yol):
                    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect((j * 12, i * 12,), (12, 12)))
                if nums[i][j] == 0:
                    pygame.draw.rect(surface, (9, 237, 28), pygame.Rect((j * 12, i * 12,), (12, 12)))
                if nums[i][j] == 999:
                    pygame.draw.rect(surface, (237, 9, 9), pygame.Rect((j * 12, i * 12,), (12, 12)))

    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    #font = pygame.font.SysFont("arial", 20)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    color_path(surface, goruntu_array)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(surface, (0, 0))

        pygame.display.update()


show_path()




