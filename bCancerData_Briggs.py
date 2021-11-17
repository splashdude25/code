'''
Breast Cancer Data:

'''

filename = 'breastCancerDataReducedDimensions.csv'
file = open(filename, 'r')

radius = {}
texture = {}
perimeter = {}
area = {}
dict = {}

lines = file.readlines()[1:]

#create a dictionary of {'id': ['diagnosis', 'radius', 'texture', 'perimeter', 'area']}
for line in lines:
    temp = line.strip('\n')
    tempList = temp.split(',')
    dict[tempList[0]] = tempList[1:]
file.close()


#write to radius file if value is >= 13.
radiusFile = open('q3_gte_13.txt', 'w')
for key, value in dict.items():
    if float(value[1]) >= 13.0:
        radiusFile.write(key + ' ' + value[0] + ' ' + value[1] + ' ' + '\n')
    else:
        continue
radiusFile.close()

#write to texture file if value is >= 18.
textureFile = open('q4_gte_18.txt', 'w')
for key, value in dict.items():
    if float(value[2]) >= 18.0:
        textureFile.write(key + ' ' + value[0] + ' ' + value[2] + ' ' + '\n')
    else:
        continue
textureFile.close()

#write to perimeter file if value is >= 85.
perimeterFile = open('q5_gte_85.txt', 'w')
for key, value in dict.items():
    if float(value[3]) >= 85.0:
        perimeterFile.write(key + ' ' + value[0] + ' ' + value[3] + ' ' + '\n')
    else:
        continue
perimeterFile.close()

#write to area file if value is >= 500.
areaFile = open('q6_gte_500.txt', 'w')
for key, value in dict.items():
    if float(value[4]) >= 500.0:
        areaFile.write(key + ' ' + value[0] + ' ' + value[4] + ' ' + '\n')
    else:
        continue
areaFile.close()


##############################################################################

'''MALIGNANT & BENIGN'''
q3_B = set()
benignRadius = open('q3_B.txt', 'w')
file = open('q3_gte_13.txt', 'r')
lines = file.readlines()
for line in lines:
    for i in range(len(line)):
        if line[i] == 'B':
            benignRadius.write(line)
        else:
            continue
for line in lines:
    words = line.split()[0]
    q3_B.add(words)
benignRadius.close()
file.close()


q3_M = set()
malignantRadius = open('q3_M.txt', 'w')
file = open('q3_gte_13.txt', 'r')
lines = file.readlines()
for line in lines:
    for i in range(len(line)):
        if line[i] == 'M':
            malignantRadius.write(line)
        else:
            continue
for line in lines:
    words = line.split()[0]
    q3_M.add(words)
malignantRadius.close()
file.close()


q4_B = set()
benignTexture = open('q4_B.txt', 'w')
file = open('q4_gte_18.txt', 'r')
lines = file.readlines()
for line in lines:
    for i in range(len(line)):
        if line[i] == 'B':
            benignTexture.write(line)
        else:
            continue
for line in lines:
    words = line.split()[0]
    q4_B.add(words)
benignTexture.close()
file.close()


q4_M = set()
malignantTexture = open('q4_M.txt', 'w')
file = open('q4_gte_18.txt', 'r')
lines = file.readlines()
for line in lines:
    for i in range(len(line)):
        if line[i] == 'M':
            malignantTexture.write(line)
        else:
            continue
for line in lines:
    words = line.split()[0]
    q4_M.add(words)
malignantTexture.close()
file.close()


q5_B = set()
benignPerimeter = open('q5_B.txt', 'w')
file = open('q5_gte_85.txt', 'r')
lines = file.readlines()
for line in lines:
    for i in range(len(line)):
        if line[i] == 'B':
            benignPerimeter.write(line)
        else:
            continue
for line in lines:
    words = line.split()[0]
    q5_B.add(words)
benignPerimeter.close()
file.close()


q5_M = set()
malignantPerimeter = open('q5_M.txt', 'w')
file = open('q5_gte_85.txt', 'r')
lines = file.readlines()
for line in lines:
    for i in range(len(line)):
        if line[i] == 'M':
            malignantPerimeter.write(line)
        else:
            continue
for line in lines:
    words = line.split()[0]
    q5_M.add(words)
malignantPerimeter.close()
file.close()


q6_B = set()
benignArea = open('q6_B.txt', 'w')
file = open('q6_gte_500.txt', 'r')
lines = file.readlines()
for line in lines:
    for i in range(len(line)):
        if line[i] == 'B':
            benignArea.write(line)
        else:
            continue
for line in lines:
    words = line.split()[0]
    q6_B.add(words)
benignArea.close()
file.close()


q6_M = set()
malignantArea = open('q6_M.txt', 'w')
file = open('q6_gte_500.txt', 'r')
lines = file.readlines()
for line in lines:
    for i in range(len(line)):
        if line[i] == 'M':
            malignantArea.write(line)
        else:
            continue
for line in lines:
    words = line.split()[0]
    q6_M.add(words)
malignantArea.close()
file.close()

unionM = (q3_M | q4_M | q5_M | q6_M)

union = f""
SubsetMResult = open("SubsetMResult.txt", 'w')
for id in unionM:
    union += f"{id}\n"
SubsetMResult.write(union)
SubsetMResult.close()


#############################################################################

''' INTERSECTION '''

intThree = set()
file = open('q3_gte_13.txt', 'r')
lines = file.readlines()
for line in lines:
    words = line.split()[0]
    intThree.add(words)
file.close()

intFour = set()
file = open('q4_gte_18.txt', 'r')
lines = file.readlines()
for line in lines:
    words = line.split()[0]
    intFour.add(words)
file.close()

intFive = set()
file = open('q5_gte_85.txt', 'r')
lines = file.readlines()
for line in lines:
    words = line.split()[0]
    intFive.add(words)
file.close()

intSix = set()
file = open('q6_gte_500.txt', 'r')
lines = file.readlines()
for line in lines:
    words = line.split()[0]
    intSix.add(words)
file.close()

totalIntersect = (intThree & intFour & intFive & intSix)

intersect = f""
NewResult = open("NewResult.txt", 'w')
for id in totalIntersect:
    intersect += f"{id}\n"
NewResult.write(intersect)
NewResult.close()


################################################################################
'''Find the difference between NewResult and SubsetMResult'''

Difference_1 = unionM - totalIntersect

################################################################################
'''Find the difference between the OriginalResult and NewResult'''

filename = 'breastCancerData.csv'
file = open(filename, 'r')
dictOrigin = {}

lines = file.readlines()[1:]

#create a dictionary of {'id': ['diagnosis', 'radius', 'texture', 'perimeter', 'area']}
for line in lines:
    temp = line.strip('\n')
    tempList = temp.split(',')
    dictOrigin[tempList[0]] = tempList[1:]
file.close()

OriginalResult = open('OriginalResult.txt', 'w')
for key, value in dictOrigin.items():
    if value[0] == 'M':
        OriginalResult.write(key+'\n')
    else:
        continue
OriginalResult.close()

origin = set()
file = open('OriginalResult.txt', 'r')
lines = file.readlines()
for line in lines:
    words = line.split()[0]
    origin.add(words)
file.close()

Difference_2 = origin - totalIntersect
print("Difference_1 is:")
print(Difference_1)
print("")
print("Difference_2 is:")
print(Difference_2)
