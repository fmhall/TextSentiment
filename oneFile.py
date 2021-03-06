#!/usr/bin/env python

# Copyright (c) 2017 Mason Hall
# All rights reserved. No warranty, explicit or implicit, provided.
import os
from textblob import TextBlob
import numpy as np
import math
import sys
from datetime import datetime

path = "/Users/masonhall/Documents/Github/RecordsCleaned/"
fileName = "+16107152704"
contact_avgs = []
my_avgs = []
numbers = []

def parseFile(path):

    number = "Couldnt get number"
    with open(path) as file :
        line = file.readline()
        while line != "" :
            if line.startswith("+") :
                number = line[2:12]
                break
            line = file.readline()

    with open(path) as file :
        contact_texts = []
        contact_sentiments = []
        my_texts = []
        my_sentiments = []
        contact_dates = []
        my_dates = []
        for line in file :
            if line.startswith("+") :
                for index, char in enumerate(line) :
                    if char == ":" :
                        text = line[index+2:].strip("\n")
                        break
                contact_texts.append(text)
                blobObj = TextBlob(text)
                contact_sentiments.append(blobObj.sentiment.polarity)
                line = file.readline()
                while line != "" :
                    if line.startswith("+") :
                        number = line[2:12]
                        break
                    line = file.readline()
                inDate = file.readline()[3:21]
                d = datetime.strptime(inDate, "%Y-%m-%d %H:%M:%S")
                contact_dates.append(d)
            elif line.startswith("Me:") :
                text = line[4:]
                my_texts.append(text)
                blobObj = TextBlob(text)
                my_sentiments.append(blobObj.sentiment.polarity)
                inDate = file.readline()[3:21]
                d = datetime.strptime(inDate, "%Y-%m-%d %H:%M:%S")
                my_dates.append(d)

    contact_sentiments = list(filter((0.0).__ne__, contact_sentiments))
    my_sentiments = list(filter((0.0).__ne__, my_sentiments))
    if len(contact_sentiments) != 0 :
        contact_avg = np.mean(contact_sentiments) 
        contact_avgs.append(contact_avg)
    if len(my_sentiments) != 0 :
        my_avg = np.mean(my_sentiments) 
        my_avgs.append(my_avg)
    
    numbers.append(number)
    # print("------------------")
    # print("Analysis of texts with {0}:\n".format(number))
    # print("Average of their sentiments: {:.4}".format(contact_avg))
    # print("Average of my sentiments: {:.4}".format(my_avg))
    # print("------------------")
    print(my_dates)
    print(contact_dates)



#readAllFiles(path)
parseFile(path+fileName)












#def readAllFiles(path):

#     #List all files in the directory and read points from text files one by one

#     for filePath in os.listdir(path):
#         if filePath.startswith("+"):
#             size = os.path.getsize(path+filePath)
#             if (size > 25000) :
#                 parseFile(path+filePath)

#     contact_min = min(contact_avgs)
#     contact_max = max(contact_avgs)
#     contact_min_index = contact_avgs.index(contact_min)
#     contact_max_index = contact_avgs.index(contact_max)
    
#     my_min = min(my_avgs)
#     my_max = max(my_avgs)
#     my_min_index = my_avgs.index(my_min)
#     my_max_index = my_avgs.index(my_max)

#     print("\n\n--------")
#     print("Contact Sentiments:")
#     print("Minimum: {:.5}".format(min(contact_avgs)))
#     print("--Number: {0}".format(numbers[contact_min_index]))
#     print("Maximum: {:.5}".format(max(contact_avgs)))
#     print("--Number: {0}".format(numbers[contact_max_index]))
#     print("Mean: {:.5}".format(np.mean(contact_avgs)))
#     print("\nMy Sentiments:")
#     print("Minimum: {:.5}".format(min(my_avgs)))
#     print("--Number: {0}".format(numbers[my_min_index]))
#     print("Maximum: {:.5}".format(max(my_avgs)))
#     print("--Number: {0}".format(numbers[my_max_index]))
#     print("Mean: {:.5}".format(np.mean(my_avgs)))


