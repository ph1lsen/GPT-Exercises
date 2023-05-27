def main():
    age = int(input("Wie alt bist du? "))

    if age < 18:
        print("Du bist noch Minderjährig")
    elif 18 <= age <= 65:
        print("Du bist Volljährig")
    else:
        print("Du bist Rentner")


if __name__ == "__main__":
    main()