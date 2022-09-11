windchill_speed = [5,]

def windchill():
    return 35.74 + 0.6215 * temperature - 35.75 * (speed ** 0.16) + 0.4275 * temperature * (speed ** 0.16) 
    




temperature = float(input('What is the temperature? '))
temp_scales = input('Fahrenheit or Celsius (F/C)?')
speed = 5
windchill_value = ''
if temp_scales.lower() == 'f':
       temperature = temperature
elif temp_scales.lower() == 'c':
        temperature = temperature * 9/5 + 32
for _ in " "*11: 
    speed += 5
    windchill_speed.append(speed)
for spd in windchill_speed:
    speed = spd
    value = windchill()
    print(f'At temperature {temperature:.1f}F, and wind speed {speed} mph, the windchill is: {value:.2f}F')

