# CSC 122
# Prime Number Checker
# By <Your Name>

"""
Inputs, Processes, Outputs (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s): Number
Processes: Check number, Loop,
Output(s):
"""


def main():
    start = "y"
    print("Prime Number Checker")
    while (start == "y"):
        num = input("\nEnter an integer to test: ")
        prime = True
        try:
            n = int(num)
            if (n > 1):
                for r in range(2, n):
                    if ((n % r) == 0):
                        print(f"{n} is a composite number because it is divisible by {r}")
                        prime = False
                        break
                if prime:
                    print(f"{n} is a prime number")
                start = input("Do you want to test another integer (y/n): ")
                start = start.lower()
            elif (n == 1):
                print(f"{n} is not a prime number")
                start = input("Do you want to test another integer (y/n): ")
                start = start.lower()
            else:
                print("Invalid integer value! Try again")
                start = "y"
        except:
            print("Invalid integer value! Try again")
            start = "y"
    print("\nBye!")



if __name__ == "__main__":
    main()
