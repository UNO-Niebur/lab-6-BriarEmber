#WordCount.py
#Name:Devyn Conaway
#Date:2/28/2026
#Assignment:Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  characterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    characterCount += len(line)
    
    for w in words:
      wordCount = wordCount + 1
    
    #for ch in line:
     # characterCount = len(line)
    
  
  print("Lines: ", lineCount)
  print("Words:", wordCount)
  print("Characters:", characterCount)

if __name__ == '__main__':
  main()
