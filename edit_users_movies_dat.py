import re
import os

def deal_dat_file(filename):
    newfile = open(os.getcwd() + "/" + filename + "_clean.dat", "w", encoding = "utf-8")
    oldfile = open(os.getcwd() + "/" + filename + ".dat", "r", encoding = "utf-8")
    for line in oldfile:
        line = re.sub(r"::", "=", line)
        newfile.writelines(line)
    oldfile.close()
    newfile.close()

deal_dat_file("users")
deal_dat_file("movies_utf8")
