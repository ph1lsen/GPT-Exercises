def main():
    base = float(input("Wie lang ist dein Dreieck (in cm)? "))
    height = float(input("Wie breit ist dein Dreieck (in cm)? "))

    area = base * height / 2

    print(f"Die Fläche deines Dreiecks beträgt {area} cm²")



if __name__ == "__main__":
    main()