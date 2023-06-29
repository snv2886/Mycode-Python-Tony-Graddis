def main():
    total = 0

    try:
        infile = open('numbers.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(f'{total:,.2f}')
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
