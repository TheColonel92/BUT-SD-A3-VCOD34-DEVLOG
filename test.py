# Small test script

def main():
    try:
        a = int(input("Enter 1 to download data, 2 to generate data: "))
    except Exception:
        a = 1
    b = 2
    c = a + b
    print("Result:", c)

if __name__ == '__main__':
    main()
