f = open('input.txt', 'r')
col1List = []
col2List = []
for line in f:
  splitLine = line.split()
  col1List.append(splitLine[0])
  col2List.append(splitLine[1])

col1List.sort()
col2List.sort()

finalDistanceSum = 0
finalSimilarityScore = 0

for x in range(0, len(col1List)):
  col1Num = int(col1List[x])
  col2Num = int(col2List[x])

  currentDistance = abs(col1Num - col2Num)
  similarCount = col1Num * col2List.count(col1List[x])
  print('current simil score')
  print(similarCount)
  finalDistanceSum += currentDistance
  finalSimilarityScore += similarCount

print(finalDistanceSum)
print(finalSimilarityScore)
f.close()