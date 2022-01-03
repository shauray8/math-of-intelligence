import pygame
import random
background_colour = (0, 0, 0)

screen = pygame.display.set_mode((600, 600))
  
pygame.display.set_caption('QUICK SORT')
  
screen.fill(background_colour)
  
pygame.display.flip()
  
running = True
color_line = (255,255,255)  
heights = []

def quicksort(arr, start, end):
    if(start >= end):
        return

    index = partition(arr, start, end)
    quicksort(arr, start, index-1)
    quicksort(arr, index+1, end)

def partition(arr, start, end):
    pivot_index = start
    pivot_value = end

    for i in range(start, end):
        if arr[i] < pivot_value:
            swap(arr, i, pivot_index)
            pivot_index += 1
            
    swap(arr, pivot_index, end)
    return pivot_index


def swap(arr,a,b):
    arr[a], arr[b] = arr[b], arr[a];

for i in range(600):
    heights.append(random.randint(0,600))

for i in range(600):
    pygame.draw.line(screen, color_line, (i, heights[i]), (i, 600))
    pygame.display.flip()
    
print(heights)
quicksort(heights, 0, len(heights)-1)

screen.fill((0,0,0))
for i in range(len(heights)):

    pygame.draw.line(screen, color_line, (i, heights[i]), (i, 600))
    pygame.display.flip()
print(heights)

while running:
    
    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            running = False
