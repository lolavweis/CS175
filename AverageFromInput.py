#Lola Weis
#CS-175
#Average From Input


def main():
    totalsum=0
    numofnum=0
    txtfile= open('numbers.txt','r')
    try:
        for linenum in txtfile:
            try:
                num = float(linenum)
                numofnum += 1
                totalsum += num
                print(f"I read in {numofnum} number(s) Current number is: {num:.2f}Total is: {totalsum:.2f}")
            except ValueError:
                print("Error converting to number.")
        if numofnum > 0:
            avg = (totalsum/numofnum)
            print(f"Average: {avg:.1f}")
        else:
            print("Please check data that is in file.")
        txtfile.close()
    except IOError:
        print("Error Reading File.")
if __name__ == '__main__':
    main()

