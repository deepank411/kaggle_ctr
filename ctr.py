import pandas as pd
import numpy as np
import string as stri
## data = pd.read_csv("Downloads/train")

from datetime import datetime

def csv_to_vw(loc_csv, loc_output, train = True):
    start = datetime.now()
    print("\nTurning %s into %s. Is_train_set? %s"%(loc_csv, loc_output, train))
    i = open(loc_csv, "r")
    j = open(loc_output, "wb")
    counter = 0
    with i as infile:
        line_count = 0
        for line in infile:
            if line_count == 0:
                line_count = 1
                continue
            categorical_features = ''
            counter += 1
            line = line.split(",")
            if train:
                a = line[2]
                new_date = datetime(int("20" + a[0:2], int(a[2:4]), int(a[4:6]))
                day = new_date.strftime("%A")
                hour = a[6:8]
                categorical_features += " |hr %s" % hour
                categorical_features += " |day %s" % day
                for i in range(3,24):
                    if line[i] != "":
                        categorical_features += "|c%s %s" % (str(i),line[i])
            else:
                a = line[1]
                new_date= datetime(int("20"+a[0:2]),int(a[2:4]),int(a[4:6]))
                day = new_date.strftime("%A")
                hour= a[6:8]
                categorical_features += " |hr %s" % hour
                categorical_features += " |day %s" % day
                for i in range(2,23):
                    if line[i] != "":
                        categorical_features += " |c%s %s" % (str(i+1),line[i])

            if train:
                if line[1] == '1':
                    label = 1
                else:
                    label = -1
                j.write("%s '%s %s\n" % (label,line[0],categorical_features))
            else:
                j.write("1 '%s %s\n" % (line[0],categorical_features))

            if counter % 1000000 == 0:
                print("%s\t%s"%(counter, str(datetime.now() - start)))

    print("\n %s Task execution time:\n\t%s"%(counter, str(datetime.now() - start)))
                                    
