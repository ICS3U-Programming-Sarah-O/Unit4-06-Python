#!/usr/bin/env python3
# Created By: Sarah OUAMOU
# Date: 11, 26, 2025
# writes out every RGB combination.


def main():


    for red in range(0,256,1):
            for green in range(0,256,1):
                    for blue in range(0,256,1):
                            print("The colors are:", {red},{green},{blue})




                           
if __name__ == "__main__":
    main()
