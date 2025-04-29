#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adnaan
#
# Created:     28/02/2024
# Copyright:   (c) Adnaan 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n = int(input().strip())
if n % 2 == 1:
    print("weird")

if n % 2 == 0:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Not Weird")
    elif n>20:
        print("Not Weird")