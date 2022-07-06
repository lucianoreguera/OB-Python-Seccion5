def year_bisiesto(year: int) -> bool:
  if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
      return True
  
  return False

def main():
    year: int = int(input("Introducir año: "))

    if(year_bisiesto(year)):
        print("El año " + str(year) + " es bisiesto")
    else:
        print("El año " + str(year) + " no es bisiesto")

main()