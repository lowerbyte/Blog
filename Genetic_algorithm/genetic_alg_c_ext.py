import random
import struct
import math
import score

W = 240     #image width
H = 314     #image height
POPULATION = 300 #population
BEST_ONES = 2   #number of best specimens
picture = [0 for x in range(W*H)]  #list of values for every pixel in image
specimens = [[0 for x in range(W*H)] for y in range(POPULATION)]  #table of specimens
                          #list of lists, each list is representing one specimen
                          #in population and values on list representing value
                          #of each pixel in the picture for each specimen.
bests = [0 for x in range(BEST_ONES)] #list of indexes of best specimens
best_population = [[0 for x in range(W*H)] for y in range(POPULATION)] #same as in specimens
                          #but this time we will fill this list of lists with
                          #the best specimens

class Specimen:         #every instance of this class represent specimen
    def __init__(self):
        self.idx = 0        #index of specimen from 'specimens'
        self.fitness_score = 0      #fitness value of every specimen

    def fitness(self, specimen):  #function for counting fitness of each specimen
        score = 0.0
        for j in range(H):
            for i in range(W):
                s = specimen[j*W + i]
                p = picture[j*W +i]
                score += (s-p)**2
        return score

fitness = [Specimen() for x in range(POPULATION)] #list of instances of Specimen


def fillBottomFlatTriangle(k, p1, p2, p3, r):
    invslope1 = ((p2[0] - p1[0])/(p2[1] - p1[1]))
    invslope2 = ((p3[0] - p1[0])/(p3[1] - p1[1]))

    curx1 = p1[0]
    curx2 = p1[0]
    for i in range(p1[1], p2[1]):
        for j in range(int(curx1), int(curx2)):
            specimens[k][i*W + j] = (specimens[k][i*W + j] + r) >> 1
        curx1 += invslope1 
        curx2 += invslope2

def fillTopFlatTriangle(k, p1, p2, p3, r):
    invslope1 = ((p3[0] - p1[0])/(p3[1] - p1[1]))
    invslope2 = ((p3[0] - p2[0])/(p3[1] - p2[1]))

    curx1 = p3[0]
    curx2 = p3[0]

    for i in range(p3[1], p1[1], -1):
        for j in range(int(curx1), int(curx2)):
            specimens[k][i*W + j] = (specimens[k][i*W + j] + r) >> 1
        curx1 -= invslope1 
        curx2 -= invslope2

def mutate(): #very, very afwul function to mutate specimens
              #there should be class representing the Point
    for i in range(len(specimens)):
        triangle = []
        x1 = random.randrange(W)
        y1 = random.randrange(H)
        p1 = (x1, y1)
        triangle.append(p1)
        x2 = random.randrange(W)
        y2 = random.randrange(H)
        p2 = (x2, y2)
        triangle.append(p2)
        x3 = random.randrange(W)
        y3 = random.randrange(H)
        p3 = (x3, y3)
        triangle.append(p3)
        r = random.randrange(255)

        triangle.sort(key = lambda x: x[1])
        
        p4 = [0,0]
        M = (triangle[2][1]-triangle[0][1])*(triangle[2][0]-triangle[0][0])
        if M != 0:
            p4[0] = int((triangle[0][0] +
        ((triangle[1][1]-triangle[0][1])/M)))
            p4[1] = triangle[1][1]
        else: continue
        if triangle[1][1] == triangle[2][1]:
            fillBottomFlatTriangle(i, triangle[0], triangle[1], triangle[2], r)

        elif triangle[0][1] == triangle[1][1]:
            fillTopFlatTriangle(i, triangle[0], triangle[1], triangle[2], r)
        else:
            fillBottomFlatTriangle(i, triangle[0], triangle[1], p4, r)
            fillTopFlatTriangle(i, triangle[1], p4, triangle[2], r)

def scoress():
    score.score(fitness, W, H, specimens, picture)
    fitness.sort(key = lambda x: x.fitness_score)
    #for k in fitness:
    #    print(k.fitness_score)
    score.best_ones(bests, fitness, BEST_ONES)
""" 
    for i in range(POPULATION): #for every specimen in list of Specimens (fitness) 
        fitness[i].idx = i      #assign current index
        fitness[i].fitness_score = fitness[i].fitness(specimens[i]) #and count the fitness
    
    fitness.sort(key = lambda x: x.fitness_score)  #sort the fitness to get 
                                           #best results at the beginning

    for i in range(BEST_ONES):  #fill the bests with indexes of first BEST_ONES Specimens
        bests[i] = fitness[i].idx
"""
def cross():    
    for i in range(BEST_ONES):   #copy the best specimens to best_population
        best_population[i] = specimens[bests[i]][:]

    for i in range(BEST_ONES, POPULATION): #and fill with then the whole generation
        specimens[i] = best_population[i % BEST_ONES][:]

def write(): #save current generation
    with open('test_triangle_2.data', 'wb') as f:
        f.write(bytearray(specimens[bests[0]]))

if __name__ == '__main__':
     with open('The_Lady_with_an_Ermine_gray.data', 'rb') as f:
        for i in range(W*H):
            picture[i] = struct.unpack('B',f.read(1))[0] #we are representing our image
                                                         #as list of integers
    
     for i in range(2000): #for 2000 generations
        print(i)
        print('mutate')
        mutate()
        print('score')
        scoress()
        print('cross')
        cross()
        print('write')
        write()
