while True:
    try:
        fraction = input("Enter fraction: ")
        x, z = fraction.split("/")
        x = int(x)
        z = int(z)

        if z == 0:
            raise ZeroDivisionError

        elif x > z:
            print("Numerator cannot be greater than denominator.")
            continue

        elif x == z or x / z == 0.99:
            print("F")
            break
        elif x == 0 or x / z == 0.01:
            print("E")
            break

        result = x / z
        percent = "{:.0%}".format(result)
        print(f"{percent}")
        break

    except ZeroDivisionError:
        print("Invalid input. Denominator cannot be zero.")
        continue

    except ValueError:
      print("Invalid input. Please enter a fraction in the form 'numerator/denominator'.")
