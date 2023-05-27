def main():
    number = int(input("Wie ist deine Zahl? "))

    print(f"Deine Zahl {number} ist gerade") if number % 2 == 0 else print(f"Deine Zahl {number} ist ungerade")



if __name__ == "__main__":
    main()