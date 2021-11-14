'''
1.) Write a function, called wrapLines, that takes a file name and a length integer k.
2.) The function wraps the lines longer than width k by splitting them into lines of length less than
or equal to k, just like resizing a text editor window.
3.) Make sure not to break in the middle of a word.
4.) If the word is longer than k, you may split it using a hyphen or leaving the entire
word on a single line.
5.) Create a try and except clause to catch the error where the file name
passed into the function is not found (this might happen either because the name of the file
is misspelled or does not exist in the directory given).
6.) Prompt the user to enter the correct file name until successful.
Hint: You will need to read the file line by line then write the result back to the same file.
'''
while True:
    try:
        fileName = input("Enter a txt file: ")
        fileName = f"{fileName}.txt"
        def wrapLines(fileName, k):
            string = f""
            list = []
            listTwo = []
            file = open(fileName, "r")
            lines = file.readlines()
            for line in lines:
                words = line.split()
                list.append(words)
            for i in range(len(list)):
                if len(list[i]) > k:
                    diff = k - len(list[i])
                    factor = len(list[i])//k
                    if factor >= 1:
                        count = 0
                        for j in range(factor):
                            tempA = list[i][(k*j):(k*(j+1))]
                            tempB = list[i][(k*(j+1)):(k*(j+2))]
                            if count > 0:
                                if tempB != a:
                                    listTwo.append(list[i][(k*(j+1)):(k*(j+2))])
                                    a = tempA
                                    b = tempB
                                    count += 1
                                else:
                                    continue
                            else:
                                listTwo.append(list[i][(k*j):(k*(j+1))])
                                listTwo.append(list[i][(k*(j+1)):(k*(j+2))])
                                a = tempA
                                b = tempB
                                count += 1
                    else:
                        listTwo.append(list[i][:diff])
                        listTwo.append(list[i][diff:])
                else:
                    listTwo.append(list[i])
            file.close()
            file = open(fileName, "w")
            for i in range(len(listTwo)):
                string += f"{' '.join(listTwo[i])}\n"
            file.write(string)
            file.close()

        wrapLines(fileName, int(input("Enter a value for 'k': ")))
        break
    except FileNotFoundError:
        print("The file you entered does not exist.")
        print("Please re-enter an existing file.")
        continue
