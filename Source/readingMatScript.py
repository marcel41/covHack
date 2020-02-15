import time
def main():
  print ("Connection For car moving")
  #readin output from matlab script that will detect
  #output Yes or No

  #read action wave
  while(1):
    file1 = open("yesOrNo.txt", "r")
    if file1:
      print("move " + file1.readline())
      time.sleep(1)
    file1.close()
  #close file to avoid leak out

def movementCar():
    skip
  #To be implemented

def movementCar():
    skip
  #To be implemented

if __name__== "__main__":
  main()
