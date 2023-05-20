f = int(input("Enter 1 for Conversion of temperature from celsius to fahrenheit, 2 for fahrenheit to celsius:-"))
if f == 1:
    def temperature(celsius, fahrenheit):
        return fahrenheit       
    celsius=int(input("Enter the tempurature in celsius:-"))
    fahrenheit=((celsius*(9/5))+32)
    t=temperature(celsius,fahrenheit)
    print(f"Your {celsius}°C temperature in fahrenheit is:-",t)    