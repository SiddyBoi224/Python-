def main():
   while True:
      try:
         fuel = input("Fuel fraction: ")
         x,y = fuel.split("/")
         x=int(x)
         y=int(y)
         Cfuel=round(x/y*100)
         if x>y:
            pass
         elif Cfuel == 99 or Cfuel ==100:
            print("F")
            break
         elif Cfuel == 1 or Cfuel ==0:
            print("E")
            break
         else:
            print(f"{Cfuel}%")
            break
      except (ValueError, ZeroDivisionError):
         pass


main()
