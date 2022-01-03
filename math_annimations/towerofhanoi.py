# the goal is to make the same pattern as a in c without disturbing the order at any point of time

a = [5,4,3,2,1,0]
b = []
c = []

length = 6
# pattern to follow: bits

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
# Driver code
n = 4
#TowerOfHanoi(n,'A','B','C') 

bit = 1
done = True
while done:
    if c == [5,4,3,2,1]:
        done = False
    x = bin(bit).replace("0b","")
    while len(x) < 6:
        x += '0'
        hanoi = x[::-1]
    

    

