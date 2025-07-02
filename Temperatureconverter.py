# Python temperature converter

temperature = float(input("Enter the temperature: "))
unit = input ("Celsius or Fahrenheit or Kelvin (C or F or K): ")

if unit == "C" :
    choose = input ("Do you want to convert it into Fahrenheit or Kelvin? (F or K) ")
    if choose == "F":
        temperature = ((9/5) * temperature) + 32
        print(f"It is {round(temperature,2)}℉ today")
    else :
        temperature = temperature + 273
        print(f"It is {round(temperature,2)}K")
elif unit == "F" :
    choose = input ("Do you want to convert it to Celsius or Kelvin? (C or K)")
    if choose == "C" :
        temperature = (5/9) * (temperature - 32)
        print(f"It is {round(temperature,2)}℃")
    else :
        temperature = ((temperature-32)/1.8) + 273
        print(f"It is {round(temperature,2)}K")
elif unit == "K" :
    choose = input("Do you want to convert it into Celsius or Fahrenheit? (C or F)")
    if choose == "C" :
        temperature = temperature -273
        print(f"It is {round(temperature,2)}℃")
    else :
        temperature = 1.8 * (temperature - 273) + 32
        print(f"It is {round(temperature,2)}℉")
else :
    print(f"Invalid {unit}")