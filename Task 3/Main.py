from Airplane import Airplane

airplane1 = Airplane("Boeing 737", 180, 100)
airplane2 = Airplane("Airbus A320", 180, 150)
airplane3 = Airplane("Boeing 737", 200, 50)

print(airplane1 == airplane3)

airplane1 += 50
print(airplane1.current_passengers)

airplane1 -= 30
print(airplane1.current_passengers)

print(airplane1 > airplane2)
print(airplane1 < airplane3)